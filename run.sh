#!/bin/bash
python3 -m venv 21game-venv
source 21game-venv/bin/activate
pip install -r requirements.txt
python3 counting_to21game.py
