@echo off

:: Define paths relative to the batch file's location
set "MENU_DIR=Editor\UI\EditorStartupMenu"
set "MENU_FILE=%MENU_DIR%\EditorStartupMenu.py"

goto verifySetup

:verifySetup
:: ENSURE DEPENDENCIES ARE INSTALLED
echo.
echo Checking for required Python packages...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to install Python dependencies. Please check your internet connection and requirements.txt.
    goto end
)


goto runMenu

:runMenu
:: CREATE DIRECTORY AND MENU SCRIPT IF THEY DON'T EXIST
echo.
echo Verifying menu script...
if not exist "%MENU_DIR%" (
    echo Creating directory %MENU_DIR%
    mkdir "%MENU_DIR%"
)

if not exist "%MENU_FILE%" (
    echo Menu script not found. Creating a blank file...
    echo.> "%MENU_FILE%"
)

:: NAVIGATE TO THE MENU DIRECTORY AND LAUNCH THE SCRIPT
cd "%MENU_DIR%"
python EditorStartupMenu.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to run the startup menu.
)
goto end

:end