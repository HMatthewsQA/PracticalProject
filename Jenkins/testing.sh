#!/bin/bash
sudo apt update -y
sudo apt install python3-pip python3-venv -y

cd PracticalProject
python3 -m venv vevnv
. ./venv/bin/activate
pip3 install flask flask-testing pytest pytest-cov requests Werkzeug==0.16.1 flask_sqlalchemy
pytest ./app1/tests/test_unit.py
pytest ./app2/tests/test_unit.py
pytest ./app3/tests/test_unit.py
pytest ./app4/tests/test_unit.py

deactivate
