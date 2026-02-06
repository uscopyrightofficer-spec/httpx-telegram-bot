#!/bin/bash

curl -L https://github.com/projectdiscovery/httpx/releases/download/v1.6.5/httpx_1.6.5_linux_amd64.zip -o httpx.zip
unzip httpx.zip
chmod +x httpx
mv httpx /usr/local/bin/

python bot.py
