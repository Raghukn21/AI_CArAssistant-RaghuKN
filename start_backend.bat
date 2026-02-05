@echo off
echo Starting AI Lease Assistant Backend...
cd backend
if exist .env echo Found .env file, loading API keys...
echo.
echo Installing dependencies just in case...
py -m pip install -r requirements.txt
echo.
echo Launching Server...
echo ---------------------------------------------------
echo When you see "Running on http://127.0.0.1:5001"
echo leave this window OPEN and go back to your browser.
echo ---------------------------------------------------
echo.
echo Opening Frontend...
echo Waiting 3 seconds for server to initialize...
timeout /t 3 /nobreak > nul
start "" "http://127.0.0.1:5001/"
echo.
py app.py
pause
