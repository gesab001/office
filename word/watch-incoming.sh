#!/bin/bash

echo hello

TARGET=/var/www/html/office/word/fonts/

inotifywait -m -e create -e moved_to --format "%f" $TARGET \
        | while read FILENAME
                do
                        echo Detected $FILENAME, adding new font
                        python3 addfonts.py
                done