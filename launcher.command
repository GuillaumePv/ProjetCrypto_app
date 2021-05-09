#!/bin/sh

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
source venv/bin/activate
open http://127.0.0.1:8050/
python3 main.py