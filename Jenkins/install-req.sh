#!/bin/bash
sudo apt update && sudo apt install -y curl jq
sudo apt-get install python-pip -y
sudo apt-get install python3-pip -y
pip install pytest
pip install pytest-cov
pip install requests
pip install flask
pip install flask_sqlalchemy
pip install flask_wtf
pip install pymysql[rsa]
pip install Werkzeug