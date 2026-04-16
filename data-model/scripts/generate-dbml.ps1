param(
  [Parameter(Mandatory = $false)]
  [string]$DataModelPath = "data-model",

  [Parameter(Mandatory = $false)]
  [string]$OutFile = "build/desl.schema.dbml"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Convert-ToSnakeCase {
  param([Parameter(Mandatory = $true)][string]$Value)

  $withUnderscore = $Value -creplace '([a-z0-9])([A-Z])', '$1_$2'
  return $withUnderscore.ToLowerInvariant()
}

function Get-DbmlType {
  param([Parameter(Mandatory = $true)][string]$ColumnName)

  switch -Regex ($ColumnName) {
    '^is_' { return 'boolean' }
    '^retry_count$' { return 'int' }
    '^retry_max_attempts$' { return 'int' }
    '^retry_backoff_seconds$' { return 'int' }
    '^ordinal_position$' { return 'int' }
    '^progress_indicator$' { return 'decimal(5,2)' }
    '^error_message$' { return 'text' }
    '_dt$' { return 'timestamp' }
    '_timestamp_dt$' { return 'timestamp' }
    '_count$' { return 'bigint' }
    '^priority$' { return 'int' }
    '^levels_deep$' { return 'int' }
    '^sla_minutes$' { return 'int' }
    '^expected_capacity$' { return 'int' }
    '^late_time_seconds$' { return 'int' }
    '_id$' { return 'bigint' }
    default { return 'varchar(255)' }
  }
}

function Get-DbmlReference {
  param([Parameter(Mandatory = $true)][string]$ColumnName)

  switch ($ColumnName) {
    'obj_id' { return 'Obj.obj_id' }
    'parent_obj_id' { return 'Obj.obj_id' }
    'source_obj_id' { return 'Obj.obj_id' }
    'target_obj_id' { return 'Obj.obj_id' }
    'inherited_from_obj_id' { return 'Obj.obj_id' }
    'prop_id' { return 'Prop.prop_id' }
    'task_template_id' { return 'TaskTemplate.task_template_id' }
    'source_event_id' { return 'Event.event_id' }
    default { return $null }
  }
}

if (-not (Test-Path -LiteralPath $DataModelPath)) {
  Write-Error "Data model path not found: $DataModelPath"
  exit 1
}

$mdFiles = Get-ChildItem -LiteralPath $DataModelPath -File -Filter "*.md" |
  Where-Object { $_.Name -ne "readme.md" } |
  Sort-Object Name

if ($mdFiles.Count -eq 0) {
  Write-Error "No markdown files found in $DataModelPath"
  exit 1
}

$outDir = Split-Path -Parent $OutFile
if (-not [string]::IsNullOrWhiteSpace($outDir) -and -not (Test-Path -LiteralPath $outDir)) {
  New-Item -ItemType Directory -Path $outDir | Out-Null
}

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add('Project DESL {')
$lines.Add('  database_type: "GenericSQL"')
$lines.Add('  Note: "Generated from markdown files in data-model."')
$lines.Add('}')
$lines.Add('')

foreach ($file in $mdFiles) {
  $raw = Get-Content -LiteralPath $file.FullName -Raw

  $tableMatch = [regex]::Match($raw, '(?m)^#\s+([A-Za-z_][\w]*)\s*$')
  if (-not $tableMatch.Success) {
    Write-Warning "Skipping $($file.Name): no table heading found."
    continue
  }

  $tableName = $tableMatch.Groups[1].Value.Trim()
  $tableDescriptionMatch = [regex]::Match($raw, '(?m)^\s*#\s+[A-Za-z_][\w]*\s*$\r?\n\r?\n(.+?)\r?\n')
  $tableDescription = $null
  if ($tableDescriptionMatch.Success) {
    $tableDescription = $tableDescriptionMatch.Groups[1].Value.Trim().Replace('"', "'")
  }
  $columnMatches = [regex]::Matches($raw, '(?m)^-\s+`([^`]+)`:\s*(.+)\s*$')

  if ($columnMatches.Count -eq 0) {
    Write-Warning "Skipping $($file.Name): no column definitions found."
    continue
  }

  $primaryKey = "$(Convert-ToSnakeCase -Value $tableName)_id"

  $lines.Add("Table $tableName {")
  if (-not [string]::IsNullOrWhiteSpace($tableDescription)) {
    $lines.Add("  Note: ""$tableDescription""")
  }
  foreach ($columnMatch in $columnMatches) {
    $columnName = $columnMatch.Groups[1].Value.Trim()
    $description = $columnMatch.Groups[2].Value.Trim().Replace('"', "'")
    $columnType = Get-DbmlType -ColumnName $columnName
    $reference = Get-DbmlReference -ColumnName $columnName

    $attrs = New-Object System.Collections.Generic.List[string]
    if ($columnName -eq $primaryKey) {
      $attrs.Add('pk')
      $attrs.Add('increment')
    }
    if (($null -ne $reference) -and ($columnName -ne $primaryKey) -and (-not $reference.StartsWith("$tableName."))) {
      $attrs.Add("ref: > $reference")
    }
    $attrs.Add("note: ""$description""")

    $lines.Add("  $columnName $columnType [$($attrs -join ', ')]")
  }
  $lines.Add('}')
  $lines.Add('')
}

[System.IO.File]::WriteAllLines($OutFile, $lines)
Write-Host "Generated DBML: $OutFile"
