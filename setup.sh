#! /bin/bash

activate () {
    python3 -m venv venv
    . venv/bin/activate
}

activate
pip install -r config/requirements.txt