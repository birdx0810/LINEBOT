#!/bin/bash

export FLASK_APP=bot.py
export FLASK_ENV=development
export FLASK_DEBUG=1

python -m flask run --host=0.0.0.0 --port=8080
