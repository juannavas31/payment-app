#!/bin/bash

if [ ! -d "venv" ]; then
    if ! command -v python3; then
        python -m venv venv
    else
        python3 -m venv venv
    fi
fi

source venv/bin/activate

pip install -r requirements.txt

uvicorn src.app:app --reload --host 0.0.0.0 --port $PAYMENT_API_PORT

deactivate
