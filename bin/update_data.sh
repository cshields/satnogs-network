#!/bin/bash

# Change to script directory
cd "$(dirname "$0")"

# Activate virtualenv
echo "========================="
echo "== Activate Virtualenv =="
echo "========================="
#. $VENV_PATH/bin/activate
. ../../venv/bin/activate
echo "done"

# Run update commands
cd ..
echo "============================"
echo "== Fetch data from DB API =="
echo "============================"
python manage.py fetch_data
echo "=========================="
echo "== Fetch data from TLEs =="
echo "=========================="
python manage.py update_all_tle
