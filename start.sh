#!/bin/bash

echo "Installing httpx..."

curl -L https://github.com/projectdiscovery/httpx/releases/latest/download/httpx_linux_amd64.zip -o httpx.zip
unzip httpx.zip
chmod +x httpx
mv httpx /usr/local/bin/httpx

echo "Starting bot..."
python bot.py
