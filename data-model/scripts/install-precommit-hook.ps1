Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path -LiteralPath "."
$sourceHook = Join-Path $repoRoot ".githooks/pre-commit"
$targetHook = Join-Path $repoRoot ".git/hooks/pre-commit"

if (-not (Test-Path -LiteralPath $sourceHook -PathType Leaf)) {
  throw "Source hook not found: $sourceHook"
}

$targetDir = Split-Path -Parent $targetHook
if (-not (Test-Path -LiteralPath $targetDir -PathType Container)) {
  throw "Git hooks directory not found: $targetDir"
}

if (Test-Path -LiteralPath $targetHook -PathType Leaf) {
  $backup = "$targetHook.backup.$([DateTime]::UtcNow.ToString('yyyyMMddHHmmss'))"
  Copy-Item -LiteralPath $targetHook -Destination $backup -Force
  Write-Host "Existing pre-commit hook backed up to: $backup"
}

Copy-Item -LiteralPath $sourceHook -Destination $targetHook -Force
Write-Host "Installed pre-commit hook: $targetHook"
Write-Host "The hook now auto-updates markdown TOCs before commit."
