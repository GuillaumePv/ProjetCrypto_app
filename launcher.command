#!/bin/sh

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
DIR="./venv/"
if [ -d "$DIR" ]; then
  ### Take action if $DIR exists ###
  echo "all packages are installed"
  case "$OSTYPE" in
  darwin*)  
  echo "OSX"
  source venv/bin/activate 
  ;; 
  linux*)   
  echo "LINUX"
  echo "source venv/bin/activate" 
  ;;
  msys*)    
  echo "WINDOWS"
  .\venv\Scripts\activate 
  ;;
  *)        echo "unknown: $OSTYPE" ;;
    esac
else
  ###  Control will jump here if $DIR does NOT exists ###
  echo "Error: ${DIR} not found. You're installing all packages"
  python3 -m venv venv
  case "$OSTYPE" in
  darwin*)  
  echo "OSX"
  echo "source venv/bin/activate" 
  ;; 
  linux*)   
  echo "LINUX"
  echo "source venv/bin/activate" 
  ;;
  msys*)    
  echo "WINDOWS"
  echo ".\venv\Scripts\activate" 
  ;;
  *)        echo "unknown: $OSTYPE" ;;
    esac
  pip3 install . -r requirements.txt
fi
echo "suite du script"
open http://127.0.0.1:8050/
python3 main.py