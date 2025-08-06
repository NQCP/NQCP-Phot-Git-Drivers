# Check status of all matching git repos
Get-ChildItem -Path $baseRepoPath -Directory | Where-Object { $_.Name -like "$repoPrefix*" } | ForEach-Object {
    $repoDir = $_.FullName
    Push-Location -Path $repoDir

    if (-not (Test-Path -Path ".git" -PathType Container)) {
        Pop-Location
        return
    }

    # Check for uncommitted/untracked changes
    $statusOutput = git status --porcelain

    if (-not [string]::IsNullOrWhiteSpace($statusOutput)) {
        Write-Host "${repoDir} has local changes" -ForegroundColor Red
        Pop-Location
        return
    }

    # Clean locally — now check remote status
    git fetch >$null 2>&1  # update remote info silently

    $statusSummary = git status -uno

    if ($statusSummary -match "Your branch is behind") {
        Write-Host "${repoDir} is clean but behind remote" -ForegroundColor Yellow
    } elseif ($statusSummary -match "Your branch is up to date") {
        Write-Host "${repoDir} is clean and up-to-date" -ForegroundColor Green
    } else {
        Write-Host "${repoDir} has unknown status" -ForegroundColor Gray
    }

    Pop-Location
}

Write-Host "`nFinished checking all repositories."

