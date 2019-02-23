#!/bin/bash

cd python
{
    python3 converter.py
    python3 main.py
    cd ..
    cd css_html
    sensible-browser index.html
    cd ..
    cd python

    python3 generate_img.py
}&>/dev/null

if [ $# -ne 0 ]
    then
    {
        python3 send_telegram.py $1
    }&>/dev/null
fi