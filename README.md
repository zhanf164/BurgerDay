

## Pip

# create virtual environment
python3 -m venv bd-env

# activate virtual environment
source bd-env/bin/activate

# install pip package
pip3 install flask

# list pip dependencies
pip3 list

# load requirements file dependencies
pip3 install -r requirements.txt

# generate requirements file
pip3 freeze > requirements.txt

# deactivate virtual environment
deactivate

## Run

# flask run
python3 -m flask run

