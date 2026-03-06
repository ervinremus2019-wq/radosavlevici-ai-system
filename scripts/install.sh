#!/bin/bash

# Radosavlevici AI System Installer
# © 2026 Ervin Remus Radosavlevici

# Check for root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run as root."
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
apt-get update
apt-get install -y python3 python3-pip git

# Clone the repository
echo "Cloning Radosavlevici AI System..."
git clone https://github.com/ervinremus2019-wq/radosavlevici-ai-system.git
cd radosavlevici-ai-system

# Install Python requirements
echo "Installing Python packages..."
pip3 install -r requirements.txt

# Set up environment
echo "Setting up environment..."
cp .env.example .env

# Verify installation
echo "Verification:"
python3 -c "from core.identity.author_metadata import AUTHOR_NAME; print(f'System author: {AUTHOR_NAME}')"

echo "Installation complete. Run with: python3 main.py"