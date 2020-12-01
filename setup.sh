#!bin/bash
echo "Setting up..."
FILE=./.env
if [ -f "$FILE" ]; then
    echo "Downloading data files from s3 bucket..."
    python init_repo.py 
else 
    echo "Can't set up. You need to configure $FILE."
fi