#!/bin/bash

echo "Provisioning VM with Python 3.5.1 stack"
echo "=============================================================================="

echo "Updating packages"
sudo apt-get update

echo "Installing pip"
sudo apt-get -y install python-pip

echo "Installing Flask"
sudo pip install Flask

echo ""
echo "=============================================================================="

echo "Python setup: "
python3 --version

echo "Pip setup: "
pip --version

echo "Provision finished"