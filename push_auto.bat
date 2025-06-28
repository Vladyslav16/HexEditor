@echo off
setlocal

:: Получить текущую дату и время для коммита
for /f "tokens=1-4 delims=/. " %%a in ("%date% %time%") do (
    set day=%%a
    set month=%%b
    set year=%%c
    set hour=%%d
)
set msg=Auto-commit %year%-%month%-%day% %time%

:: Команды Git
git add .
git commit -m "%msg%"
git push

pause
