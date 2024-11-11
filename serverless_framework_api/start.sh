#!/bin/sh
#
## Start Gunicorn processes
## port: 8081
#python3 -m uvicorn main:app --reload --port 8081   --host 0.0.0.0   --log-config conf/logging.conf
uvicorn --port 8081  main:app --host 0.0.0.0  --reload --log-config conf/logging.conf
