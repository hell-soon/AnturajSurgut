#!/usr/bin/env bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn backend.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --chdir backend
