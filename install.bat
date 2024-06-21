@echo off

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    exit /b
)

REM Set the virtual environment directory
set VENV_DIR=%~dp0venv

REM Check if venv exists in the current directory
if not exist "%VENV_DIR%\" (
    echo Virtual environment does not exist. Creating one...
    python -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo Failed to create a virtual environment.
        exit /b
    )
)

REM Activate the virtual environment
call "%VENV_DIR%\Scripts\activate.bat"

REM Check if activation was successful
if "%VIRTUAL_ENV%" == "" (
    echo Failed to activate the virtual environment.
    exit /b
)

REM Install requirements
python -m pip install --upgrade pip > pip_log.txt 2>&1
if errorlevel 1 (
    echo Failed to upgrade pip. Check pip_log.txt for details.
    exit /b
)

python -m pip install -r requirements.txt > pip_log.txt 2>&1
if errorlevel 1 (
    echo Failed to install requirements. Check pip_log.txt for details.
    exit /b
)

echo Requirements installed successfully.