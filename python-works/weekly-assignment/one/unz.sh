#!/bin/bash
echo "{+] Strated Unzipping $1";
unzip $1;

python3 attempt.py;

