param (
    [Parameter(Mandatory=$true)]
    [string]$DockerUsername
)

Write-Host "=========================================================="
Write-Host " Building & Pushing Anomaly Detection System to Docker Hub "
Write-Host " Username: $DockerUsername "
Write-Host "=========================================================="

$services = @(
    @{ Name = "user-service";    Path = "./user-service" },
    @{ Name = "order-service";   Path = "./order-service" },
    @{ Name = "payment-service"; Path = "./payment-service" },
    @{ Name = "api-gateway";     Path = "./api-gateway" },
    @{ Name = "ai-service";      Path = "./ai-service" },
    @{ Name = "portal";          Path = "../anomaly-detection-system-portal" }
)

foreach ($s in $services) {
    $imageName = "$DockerUsername/anomaly-$($s.Name):latest"
    Write-Host "`n---> Building $imageName from $($s.Path)..."
    docker build -t $imageName $($s.Path)

    if ($LASTEXITCODE -eq 0) {
        Write-Host "---> Pushing $imageName to Docker Hub..."
        docker push $imageName
    } else {
        Write-Host "Failed to build $($s.Name)" -ForegroundColor Red
    }
}

Write-Host "`n=========================================================="
Write-Host " All images successfully pushed to Docker Hub! "
Write-Host "=========================================================="
