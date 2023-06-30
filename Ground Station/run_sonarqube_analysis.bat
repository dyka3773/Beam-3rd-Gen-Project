@echo off
@REM This command will run the sonarqube analysis on the current project
@REM The sonarqube server must be running on the local machine
@REM The sonarqube server must have the project already created named "Beam-3rd-Gen" and the token must be generated
@REM This also assumes that the sonar-scanner is in the path
sonar-scanner.bat -D"sonar.projectKey=Beam-3rd-Gen" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_1a5d3b0120dd61a8f50624deb5264b93c4bb65b6"