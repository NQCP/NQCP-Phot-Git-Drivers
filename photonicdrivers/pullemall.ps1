# Configuration
$baseRepoPath = Get-Location
$repoPrefix = "NQCP-Phot-Git"

# Find matching directories and attempt pull
Get-ChildItem -Path $baseRepoPath -Directory | Where-Object { $_.Name -like "$repoPrefix*" } | ForEach-Object {
    $repoDir = $_.FullName
    Push-Location -Path $repoDir # Change to repo dir, remember original

    # Check if a .git directory exists
    if (-not (Test-Path -Path ".git" -PathType Container)) {
        Pop-Location # Return to original directory
        continue
    }

    # Attempt fast-forward only pull, suppress Git's output
    git pull --ff-only >$null 2>&1

    # Check the result and print the appropriate message
    if ($LASTEXITCODE -ne 0) {
        Write-Host "failed to pull $repoDir" -ForegroundColor Red
    }
    else {
        Write-Host "pulled $repoDir successfully" -ForegroundColor Green
    }

    Pop-Location # Return to original directory
}

Write-Host "Script finished."