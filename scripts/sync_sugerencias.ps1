# ==============================================================================
# Script de Sincronización Automática de Sugerencias con GitHub REST API
# ==============================================================================

param (
    [string]$LocalFilePath = "SUGERENCIAS.md",
    [string]$TargetRepoPath = "SUGERENCIAS.md",
    [string]$CommitMessage = "docs: actualizar sugerencias automaticamente"
)

$token = $env:GITHUB_PERSONAL_ACCESS_TOKEN
if (-not $token) {
    Write-Error "La variable de entorno GITHUB_PERSONAL_ACCESS_TOKEN no esta definida."
    exit 1
}

$owner = "Tavo-Ke"
$repo  = "antigravity-sugerencias"

$headers = @{
    "Authorization" = "token $token"
    "User-Agent"    = "Antigravity-Agent"
    "Accept"        = "application/vnd.github.v3+json"
}

if (-not (Test-Path $LocalFilePath)) {
    Write-Error "El archivo local '$LocalFilePath' no existe."
    exit 1
}

# 1. Obtener SHA del archivo en GitHub (si existe)
$sha = $null
try {
    $existingFile = Invoke-RestMethod -Uri "https://api.github.com/repos/$owner/$repo/contents/$TargetRepoPath" -Method Get -Headers $headers
    $sha = $existingFile.sha
} catch {
    $sha = $null
}

# 2. Convertir contenido local a Base64 manteniendo UTF-8
$fileBytes = [System.IO.File]::ReadAllBytes($LocalFilePath)
$base64Content = [System.Convert]::ToBase64String($fileBytes)

# 3. Preparar Body del Request
$bodyObject = @{
    message = $CommitMessage
    content = $base64Content
}
if ($sha) {
    $bodyObject["sha"] = $sha
}

$bodyJson = $bodyObject | ConvertTo-Json

# 4. Enviar actualización a GitHub API
$response = Invoke-RestMethod -Uri "https://api.github.com/repos/$owner/$repo/contents/$TargetRepoPath" -Method Put -Headers $headers -Body $bodyJson -ContentType "application/json"

Write-Host "✅ Archivo sincronizado con éxito:"
Write-Host $response.content.html_url
