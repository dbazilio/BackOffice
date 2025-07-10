@echo off
cd /d %~dp0src\backend

REM Ativa o ambiente virtual, se existir
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo Ambiente virtual nao encontrado. Execute manualmente se desejar.
)

REM Instala as dependencias
pip install -r requirements.txt

REM Inicia a API Flask
python app.py
