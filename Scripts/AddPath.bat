@echo off
REM echo %0 %1
REM Uso: AddPath "path"
SET Key="HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
FOR /F "usebackq tokens=2*" %%A IN (`REG QUERY %Key% /v PATH`) DO Set CurrPath=%%B
cd %~dp0
ECHO %CurrPath% > PATH_Backup.txt
SETX PATH "%CurrPath%";%1 /M