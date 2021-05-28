#!/bin/sh

DIR="./venv/"
echo "========================================================================="
echo "=========================== Launcher ===================================="
echo "========================================================================="
echo "Crypto Project is launching"
echo "If you do not installed all Python package, this script will intall all packages for you"
echo "Program could take several minute to run !!!"
echo "Enjoy our crypto dashboard !!!"
echo "========================================================================="
echo ""
if [ -d "$DIR" ]; then
  ### Take action if $DIR exists ###
  echo "all packages are installed"
  case "$OSTYPE" in
  darwin*)  
  #echo "OSX"
  source venv/bin/activate 
  ;; 
  linux*)   
  #echo "LINUX"
  source venv/bin/activate
  ;;
  msys*)    
  echo "WINDOWS"
  .\venv\Scripts\activate 
  ;;
  *)        echo "unknown: $OSTYPE" ;;
    esac
else
  echo "Error: ${DIR} not found. You're installing all packages"
  python3 -m venv venv
  case "$OSTYPE" in
  darwin*)  
  #echo "OSX"
  source venv/bin/activate
  ;; 
  linux*)   
  #echo "LINUX"
  source venv/bin/activate
  ;;
  msys*)    
  #echo "WINDOWS"
  .\venv\Scripts\activate
  ;;
  *)        echo "unknown: $OSTYPE" ;;
    esac
  pip3 install . -r requirements.txt
fi

case "$OSTYPE" in
  darwin*)  
  #echo "OSX"
  #open http://127.0.0.1:8050/ 
  ;; 
  linux*)   
  #echo "LINUX"
  #open http://127.0.0.1:8050/ 
  ;;
  msys*)    
  #echo "WINDOWS"
  #start http://127.0.0.1:8050/ 
  ;;
  *)        echo "unknown: $OSTYPE" ;;
    esac

echo "App is loading...."
python3 main.py

