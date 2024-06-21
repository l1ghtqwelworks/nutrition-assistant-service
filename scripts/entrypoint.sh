#!/bin/bash


set -e

# Start Gunicorn
exec python -m gunicorn -k uvicorn.workers.UvicornWorker -c /home/python/scripts/gunicorn_config.py application.main:app
