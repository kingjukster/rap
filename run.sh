#!/bin/bash
# Install dependencies and run the rap generator
# Optional: pass --install-cron to schedule automatic runs every 6 hours
set -e

pip install --quiet --upgrade -r requirements.txt
python generate_rap.py

if [ "$1" == "--install-cron" ]; then
    PYTHON=$(command -v python3)
    SCRIPT_PATH=$(realpath generate_rap.py)
    CRON_JOB="0 */6 * * * $PYTHON $SCRIPT_PATH"
    (crontab -l 2>/dev/null | grep -Fv "$SCRIPT_PATH"; echo "$CRON_JOB") | crontab -
    echo "Cron job installed: $CRON_JOB"
fi
