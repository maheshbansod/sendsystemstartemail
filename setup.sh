#!/usr/bin/sh

sudo mkdir -p /root/scripts
sudo cp sendSystemStartEmail.py /root/scripts/
sudo cp boot.sh /root/scripts
sudo cp rootboot.service /etc/systemd/system/
sudo systemctl enable rootboot.service
if [ ! -f creds.data ]; then
  echo "creds.data not found in current directory."
  read -p "Enter your email address: " addr
  read -p "Enter your password/app password: " password
  echo -e "$addr\n$password" > creds.data
fi
sudo cp creds.data /root/scripts
