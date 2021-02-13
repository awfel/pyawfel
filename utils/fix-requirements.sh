#!/bin/bash

# Script takes a single argument which is the path... if it's nothing we
# assume that this is being run from the utils folder and use ../

if [[ ! -f "./setup.py" ]]
then
    echo "File setup.py not found"
    exit
fi

echo -e "\033[1;36mGenerating requirements.txt file for core dependencies.\033[0m"
echo "- Generating temp file"
pip freeze --exclude-editable >> ./temp-requirements.txt
echo "- Uninstalling existing packages"
pip uninstall -y -q -r ./temp-requirements.txt
echo "- Upgrading pip to latest version"
python -m pip install --quiet --upgrade pip
echo "- Installing core dependencies only"
pip install -q -e .
echo "- Freezing core dependencies and writing to ./requirements.txt"
pip freeze --exclude-editable >| ./requirements.txt

echo "- Restoring all packages"
pip install -q -r ./temp-requirements.txt

echo "- Removing temp file"
rm ./temp-requirements.txt

echo "- Finished! 🎉"
