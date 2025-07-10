@echo off
cd /d %~dp0src\frontend

REM Instala as dependências do React
call npm install

REM Inicia o servidor de desenvolvimento React
call npm start
