#!/bin/bash
source /home/www/articles/back/venv/bin/activate
cd /home/www/articles/back/
uvicorn server:app --host 0.0.0.0 --port 8888 --reload
