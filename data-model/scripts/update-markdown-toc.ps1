param(
  [Parameter(Mandatory = $false)]
  [string[]]$Paths = @("."),

  [Parameter(Mandatory = $false)]
  [switch]$StagedOnly,

  [Parameter(Mandatory = $false)]
  [switch]$InsertMissing,

  [Parameter(Mandatory = $false)]
  [int]$MaxHeadingLevel = 3
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-AnchorSlug {
  param([Parameter(Mandatory = $true)][string]$Heading)

  $slug = $Heading.ToLowerInvariant()
  $slug = $slug -replace '<[^>]+>', ''
  $slug = $slug -replace '[`*_~\[\]\(\)!?.,:;''"\\/|{}@#$%^&+=]', ''
  $slug = $slug -replace '\s+', '-'
  $slug = $slug -replace '-+', '-'
  return $slug.Trim('-')
}

function Get-MarkdownFiles {
  if ($StagedOnly) {
    $staged = git diff --cached --name-only --diff-filter=ACM
    if ($LASTEXITCODE -ne 0) {
      throw "Failed to read staged files from git."
    }

    return $staged |
      Where-Object { $_ -match '\.md$' } |
      ForEach-Object { (Resolve-Path -LiteralPath $_).Path }
  }

  $all = New-Object System.Collections.Generic.List[string]
  foreach ($path in $Paths) {
    if (Test-Path -LiteralPath $path -PathType Leaf) {
      if ($path -match '\.md$') {
        $all.Add((Resolve-Path -LiteralPath $path).Path)
      }
      continue
    }

    if (Test-Path -LiteralPath $path -PathType Container) {
      $files = Get-ChildItem -LiteralPath $path -File -Recurse -Filter "*.md"
      foreach ($file in $files) {
        $all.Add($file.FullName)
      }
    }
  }

  return $all | Sort-Object -Unique
}

function Get-HeadingsForToc {
  param(
    [Parameter(Mandatory = $true)]
    [AllowEmptyString()]
    [string[]]$Lines
  )

  $headings = New-Object System.Collections.Generic.List[object]
  $anchorCounts = @{}
  $inCodeBlock = $false

  foreach ($line in $Lines) {
    if ($line -match '^\s*```') {
      $inCodeBlock = -not $inCodeBlock
      continue
    }
    if ($inCodeBlock) {
      continue
    }

    $match = [regex]::Match($line, '^(#{2,6})\s+(.+?)\s*$')
    if (-not $match.Success) {
      continue
    }

    $level = $match.Groups[1].Value.Length
    if ($level -gt $MaxHeadingLevel) {
      continue
    }

    $title = $match.Groups[2].Value
    $title = [regex]::Replace($title, '\s+#+\s*$', '').Trim()
    if ($title -ieq "Table of contents") {
      continue
    }

    $slugBase = Get-AnchorSlug -Heading $title
    if ([string]::IsNullOrWhiteSpace($slugBase)) {
      continue
    }

    if ($anchorCounts.ContainsKey($slugBase)) {
      $anchorCounts[$slugBase]++
      $slug = "$slugBase-$($anchorCounts[$slugBase])"
    }
    else {
      $anchorCounts[$slugBase] = 0
      $slug = $slugBase
    }

    $headings.Add([pscustomobject]@{
        Level = $level
        Title = $title
        Anchor = $slug
      })
  }

  return $headings
}

function New-TocSectionLines {
  param([Parameter(Mandatory = $true)]$Headings)

  $section = New-Object System.Collections.Generic.List[string]
  $section.Add("## Table of contents")
  $section.Add("")
  $section.Add("<!-- toc:start -->")

  foreach ($heading in $Headings) {
    $indent = "  " * [Math]::Max(0, $heading.Level - 2)
    $section.Add("$indent- [$($heading.Title)](#$($heading.Anchor))")
  }

  $section.Add("<!-- toc:end -->")
  $section.Add("")
  return $section
}

function Update-TableOfContents {
  param([Parameter(Mandatory = $true)][string]$FilePath)

  $raw = Get-Content -LiteralPath $FilePath -Raw
  if ([string]::IsNullOrWhiteSpace($raw)) {
    return $false
  }

  $newline = if ($raw.Contains("`r`n")) { "`r`n" } else { "`n" }
  $trimmedRaw = $raw.TrimEnd("`r", "`n")
  $lines = [string[]]($trimmedRaw -split "\r?\n")

  $hasToc = $lines -match '^\s*##\s+Table of contents\s*$'
  if (-not $hasToc -and -not $InsertMissing) {
    return $false
  }

  $headings = Get-HeadingsForToc -Lines $lines
  $tocSection = New-TocSectionLines -Headings $headings
  $result = New-Object System.Collections.Generic.List[string]

  $tocIndex = -1
  for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '^\s*##\s+Table of contents\s*$') {
      $tocIndex = $i
      break
    }
  }

  if ($tocIndex -ge 0) {
    $nextH2 = $lines.Length
    for ($j = $tocIndex + 1; $j -lt $lines.Length; $j++) {
      if ($lines[$j] -match '^\s*##\s+') {
        $nextH2 = $j
        break
      }
    }

    for ($i = 0; $i -lt $tocIndex; $i++) {
      $result.Add($lines[$i])
    }
    foreach ($line in $tocSection) {
      $result.Add($line)
    }
    for ($i = $nextH2; $i -lt $lines.Length; $i++) {
      $result.Add($lines[$i])
    }
  }
  else {
    $h1Index = -1
    for ($i = 0; $i -lt $lines.Length; $i++) {
      if ($lines[$i] -match '^\s*#\s+') {
        $h1Index = $i
        break
      }
    }

    if ($h1Index -lt 0) {
      return $false
    }

    for ($i = 0; $i -le $h1Index; $i++) {
      $result.Add($lines[$i])
    }
    $result.Add("")
    foreach ($line in $tocSection) {
      $result.Add($line)
    }
    for ($i = $h1Index + 1; $i -lt $lines.Length; $i++) {
      $result.Add($lines[$i])
    }
  }

  $newContent = (($result -join $newline).TrimEnd("`r", "`n")) + $newline
  if ($newContent -eq $raw) {
    return $false
  }

  $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
  [System.IO.File]::WriteAllText($FilePath, $newContent, $utf8NoBom)
  return $true
}

$mdFiles = Get-MarkdownFiles
if (($null -eq $mdFiles) -or ($mdFiles.Count -eq 0)) {
  Write-Host "No markdown files to process."
  exit 0
}

$changedFiles = New-Object System.Collections.Generic.List[string]
foreach ($file in $mdFiles) {
  if (Update-TableOfContents -FilePath $file) {
    $changedFiles.Add($file)
  }
}

if ($changedFiles.Count -eq 0) {
  Write-Host "TOC is up to date."
  exit 0
}

Write-Host "Updated TOC in:"
foreach ($file in $changedFiles) {
  Write-Host "- $file"
}
