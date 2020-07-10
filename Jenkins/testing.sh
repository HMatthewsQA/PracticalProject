#!/bin/bash
python3 -m venv vevnv
. ./venv/bin/activate

pytest ./PracticalProject/app1
pytest ./PracticalProject/app2
pytest ./PracticalProject/app3
pytest ./PracticalProject/app4

deactivate
