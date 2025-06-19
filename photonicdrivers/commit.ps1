# Show status and staged changes
Write-Host "`n===== git status ====="
git status

# Ask to pull
$doPull = Read-Host "Do you want to pull? [y/n]"
if ($doPull -eq 'y') {
    git pull --ff-only
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Pull failed!"
    } else {
        Write-Host "Pull successful."
    }
} else {
    Write-Host "Skipping pull."
}

# Ask to add changes
$addAll = Read-Host "Do you want to add all changes? [y/n]"
if ($addAll -eq 'y') {
    git add -A
    Write-Host "Added all changes."
} else {
    Write-Host "Skipping git add."
}

# Ask for user info and commit message
$userName = Read-Host "Enter author username for this commit"
$userEmail = Read-Host "Enter author email for this commit"
$commitMessage = Read-Host "Enter commit message"

# Commit with inline user config
git -c user.name="$userName" -c user.email="$userEmail" commit -m "$commitMessage"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Commit failed or nothing to commit."
} else {
    Write-Host "Commit successful."
}

# Ask to push
$doPush = Read-Host "Do you want to push changes? [y/n]"
if ($doPush -eq 'y') {
    git push
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Push failed!"
    } else {
        Write-Host "Push successful."
    }
} else {
    Write-Host "Skipping push."
}

Write-Host "`n===== git status ====="
git status