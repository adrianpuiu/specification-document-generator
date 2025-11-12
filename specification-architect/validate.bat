@echo off
REM Specification Architect Validation Helper

setlocal enabledelayedexpansion
set SCRIPT_DIR=%~dp0
set SPEC_DIR=.
set VERBOSE=
set GENERATE=

:parse_args
if "%1"=="" goto run
if "%1"=="-p" (set SPEC_DIR=%2 & shift & shift & goto parse_args)
if "%1"=="--path" (set SPEC_DIR=%2 & shift & shift & goto parse_args)
if "%1"=="-v" (set VERBOSE=--verbose & shift & goto parse_args)
if "%1"=="--verbose" (set VERBOSE=--verbose & shift & goto parse_args)
if "%1"=="-g" (set GENERATE=--generate-validation & shift & goto parse_args)
if "%1"=="--generate" (set GENERATE=--generate-validation & shift & goto parse_args)
shift
goto parse_args

:run
echo Running specification validation...
python "%SCRIPT_DIR%validate_specifications.py" --path "%SPEC_DIR%" %VERBOSE% %GENERATE%
exit /b %ERRORLEVEL%
