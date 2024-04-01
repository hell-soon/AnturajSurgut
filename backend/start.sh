#!/usr/bin/env bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn backend.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
<<<<<<< HEAD
    --chdir backend
=======
    --chdir backend
>>>>>>> db58ad547cd72490e0bb3be125e907c615ceb510
