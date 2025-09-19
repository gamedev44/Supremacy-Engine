@echo off

:: Change the current directory to the directory of this batch file
cd "%~dp0"

:: Navigate to the engine directory and run main.py
cd ..\..\..\Engine\Win64\PyEngine3D\

python main.py
