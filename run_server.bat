@echo off

@REM This file will start the flask server

@REM Note: It will run the server on debug mode, this way in case of an error you will have an interactive debugger in the browser
@REM and you can also make changes to the code and see the changes in the browser without restarting the server
@REM To run the server in production mode, remove the --debug flag

flask --app="dropstar_gui\app.py" run --host="0.0.0.0" --port=8000 --debug