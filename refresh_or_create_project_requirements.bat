@echo off 

@REM Refreshes or creates the project requirements file

pip freeze > requirements.txt

PAUSE