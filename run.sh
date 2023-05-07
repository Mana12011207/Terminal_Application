#!/bin/bash

if command -v python &>/dev/null; then
    echo "Python is installed."
else
    echo "python is not installed."
fi


if [ -n "$VIRTUAL_ENV" ]; then
    echo "Virtual environment is activated."
else
    echo "Virtual environment is not activated."
fi



python3 -m venv 21game-venv
source 21game-venv/bin/activate
pip install -r requirements.txt
python3 counting_to21game.py
