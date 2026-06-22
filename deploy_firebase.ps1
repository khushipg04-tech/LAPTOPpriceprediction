# Firebase Deployment Script for Windows
# Run this script to deploy your Flask app to Firebase Functions

# Temporarily add Node.js and npm to path if not already there
$env:PATH = "C:\Program Files\nodejs;C:\Users\91932\AppData\Roaming\npm;" + $env:PATH

# 1. Login to Firebase
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host " 1. Authenticating with Firebase..." -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
& firebase login

# 2. Initialize project link (if not already done)
Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host " 2. Linking to your Firebase Project..." -ForegroundColor Cyan
Write-Host " You will select your active Firebase project." -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
& firebase use --add

# 3. Deploy
Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host " 3. Deploying Cloud Functions..." -ForegroundColor Cyan
Write-Host " This will upload and deploy the Python backend." -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
& firebase deploy --only functions
