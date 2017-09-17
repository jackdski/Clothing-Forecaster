#!/bin/bash

cd src
python weather.py
python /src/gui.py
cd ..
./talk.sh
