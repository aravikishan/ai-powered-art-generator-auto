#!/bin/bash
set -e
echo "Starting AI-Powered Art Generator..."
uvicorn app:app --host 0.0.0.0 --port 9013 --workers 1
