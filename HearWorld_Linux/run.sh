#!/bin/bash
# Получаем абсолютный путь к папке, где лежит этот скрипт
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
cd "$SCRIPT_DIR"

# Запускаем Python из нашего локального окружения venv, игнорируя системный Python ПК
./venv/bin/python3 main.py
