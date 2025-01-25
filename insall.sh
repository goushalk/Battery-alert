#!/bin/bash


#if id is 0 then it is exec as root 

if [ $(id -u) -ne 0 ]
  then echo Please run this script as root or using sudo!
  exit
fi

#write script under here 

read -p "Enter Your Username: " username

read -p "Enter Your Group: " groupname


#getting username and group of the user.....
echo $username
echo $groupname
working_dict=$(pwd) 

#installing depencies and updating (change it accroding to your os I was to lazy..... sorry )
echo "Installing dependencies for the program......"
sudo apt install python3
echo ""
sudo apt install python3-pip
echo ""
pip3 install psutil
pip3 install pytk 
sudo apt-get install python3-tkw
echo ""
sudo apt update 

#changing permision of the main program 
echo "Changing permissions "
chmod +x battery_alert.py

#creating the .service file
sudo touch /etc/systemd/system/battery_alert.service

#printng the cofig to the .service file
echo """[Unit]
Description=Battery Checker Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 $working_dict/battery_alert.py
Environment="DISPLAY=:0"
Environment="XAUTHORITY=/home/$username/.Xauthority"
WorkingDirectory=$working_dict
Restart=always
User=$username
Group=$groupname

[Install]
WantedBy=multi-user.target """ >> /etc/systemd/system/battery_alert.service

#reloding the deamon and starting the services and showing the user that it is enbled
sudo systemctl daemon-reload
echo ""
sudo systemctl enable battery_alert.service
echo ""
sudo systemctl start battery_alert.service
echo ""
sudo systemctl status battery_alert.service


