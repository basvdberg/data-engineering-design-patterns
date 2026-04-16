param(
  [Parameter(Mandatory = $false)]
  [string]$Path = "build/desl.schema.dbml"
)

if (-not (Test-Path $Path)) {
  Write-Error "DBML file not found: $Path"
  exit 1
}

Write-Host "Linting DBML file: $Path"

# dbml2sql parses/validates DBML. If parsing fails, it returns a non-zero exit code.
npx -y -p @dbml/cli dbml2sql "$Path" --postgres *> $null

if ($LASTEXITCODE -ne 0) {
  Write-Error "DBML lint failed for: $Path"
  exit $LASTEXITCODE
}

Write-Host "DBML lint passed: $Path"
