@echo off

REM Set the virtual environment directory
set VENV_DIR=%~dp0..\venv

REM Activate the virtual environment
call "%VENV_DIR%\Scripts\activate.bat"

REM Check if activation was successful
if "%VIRTUAL_ENV%" == "" (
    echo Failed to activate the virtual environment. Run install.
    exit /b
)

REM Run main.py with CLI arguments
cd ..
python main.py %*
