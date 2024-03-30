@echo off
setlocal

rem Get the directory of the batch file
set "batch_dir=%~dp0"

python "%batch_dir%\testServer.py"
