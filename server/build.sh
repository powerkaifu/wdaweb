#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
if [ -f "../cms_data_backup.json" ]; then
    python manage.py loaddata ../cms_data_backup.json || true
fi

python seed_data.py
