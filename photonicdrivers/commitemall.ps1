# Configuration
$baseRepoPath = Get-Location
$repoPrefix = "NQCP-Phot-Git"

# Get list of matching repo folders
$repos = Get-ChildItem -Path $baseRepoPath -Directory | Where-Object { $_.Name -like "$repoPrefix*" }

if ($repos.Count -eq 0) {
    Write-Host "No repositories found with prefix '$repoPrefix'." -ForegroundColor Yellow
    exit
}

foreach ($repo in $repos) {
    $repoDir = $repo.FullName
    Write-Host "`n============================================" -ForegroundColor Cyan
    Write-Host "Working in repository: $repoDir" -ForegroundColor Cyan
    Write-Host "============================================" -ForegroundColor Cyan

    Push-Location -Path $repoDir

    if (-not (Test-Path -Path ".git" -PathType Container)) {
        Write-Host "Skipped (not a Git repository)" -ForegroundColor Yellow
        Pop-Location
        continue
    }

    # Show git status
    Write-Host "`n[STATUS]" -ForegroundColor Magenta
    git status

    # Ask to continue (default No)
    $doContinue = Read-Host "Do you want to proced to staging changes? [y/N]"
    if ($doContinue -eq 'y') {
        Write-Host "Continuing to stage." -ForegroundColor Yellow
    } else {
        Write-Host "Skipping staging." -ForegroundColor Yellow
        continue
    }

    # Ask to pull (default No)
    $doPull = Read-Host "Do you want to pull? [y/N]"
    if ($doPull -eq 'y') {
        git pull --ff-only
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Pull failed!" -ForegroundColor Red
        } else {
            Write-Host "Pull successful." -ForegroundColor Green
        }
    } else {
        Write-Host "Skipping pull." -ForegroundColor Yellow
    }

    # Ask to add all changes (default No)
    $addAll = Read-Host "Do you want to add all changes? [y/N]"
    if ($addAll -eq 'y') {
        git add -A
        Write-Host "Added all changes." -ForegroundColor Green
    } else {
        Write-Host "Skipping git add." -ForegroundColor Yellow
    }

    # Show staged files
    $staged = git diff --cached --name-only
    if ($staged) {
        Write-Host "`n[STAGED FILES]" -ForegroundColor Magenta
        $staged | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }

        # Ask for commit info
        $userName = Read-Host "Enter author username for this commit"
        $userEmail = Read-Host "Enter author email for this commit"
        $commitMessage = Read-Host "Enter commit message"

        git -c user.name="$userName" -c user.email="$userEmail" commit -m "$commitMessage"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Commit failed!" -ForegroundColor Red
        } else {
            Write-Host "Commit successful." -ForegroundColor Green
        }
    } else {
        Write-Host "No staged changes to commit." -ForegroundColor Yellow
    }

    # Ask to push (default No)
    $doPush = Read-Host "Do you want to push changes? [y/N]"
    if ($doPush -eq 'y') {
        git push
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Push failed!" -ForegroundColor Red
        } else {
            Write-Host "Push successful." -ForegroundColor Green
        }
    } else {
        Write-Host "Skipping push." -ForegroundColor Yellow
    }

    Pop-Location
}

Write-Host "`nAll repositories processed." -ForegroundColor Cyan
