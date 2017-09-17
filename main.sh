#!/bin/bash

cd src
python weather.py
cd ..
./talk.sh
cd src
python gui.py
