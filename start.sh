#!/bin/bash
apt-get update
apt-get install -y golang-go
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
python bot.py
