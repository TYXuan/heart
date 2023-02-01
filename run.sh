#!/bin/bash

python src/dataprocessing.py
python src/modelling.py < 'algorithm_used.txt'