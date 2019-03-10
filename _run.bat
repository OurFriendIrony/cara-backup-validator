REM Setup Environment
    set PYTHONHOME=C:\Python27
    set PYTHONPATH=%PYTHONHOME%\Lib;.
    set PATH=%PYTHONHOME%;%PATH%

REM Execute Validator
    ECHO ON
    python src\RoboCopyValidator.py
    PAUSE
