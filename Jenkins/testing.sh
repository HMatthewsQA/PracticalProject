#!/bin/bash
cd PracticalProject
python3 -m venv vevnv
. ./venv/bin/activate

pytest ./app1
pytest ./app2
pytest ./app3
pytest ./app4

deactivate
