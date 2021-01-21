# ELIZA@LINE
An implementation of ELIZA on a LINE chatbot.


## Getting Started
```bash
pipenv install
cd src
export FLASK_APP=bot.py
export FLASK_ENV=development
python -m flask run --host=0.0.0.0 --port=8080 --debug=True   
```