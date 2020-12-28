#!/bin/bash
file=./credentials.json
file2=./pass.txt
[[ "$(python3 -V)" =~ "Python 3" ]] && echo "Python 3 is installed"
echo "Installing dependencies"
pip install --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv .
source Scripts/activate
pip install -r requirements.txt
if [ -e "$file" ]; then
    echo "Google Api Credentials found"
else
    echo "Google Api Credentials does exist. Please down Credentials from https://developers.google.com/calendar/quickstart/python"
fi
if [ -e "$file2" ]; then
    echo "Pass.txt exists"
else
    echo "Pass.txt does not exist"
fi
