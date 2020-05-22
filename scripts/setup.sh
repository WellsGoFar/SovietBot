#!/bin/bash

echo "make sure you have python3 installed"
echo "Installing dependencies"

apt install python3-pip
pip install discord.py
pip install praw
pip install asyncio
pip install python-dotenv
pip install pymongo

echo "Setup complete"