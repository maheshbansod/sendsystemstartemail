# send system startup email
The script sendSystemStartEmail.py emails yourself using the credentials you store in a file called creds.data. The commands iw, ip and w are invoked and the output is sent as the email body.  

You can edit this script and use the commands your system supports.  

## Installation
Systemd is used to invoke the script at startup. Modify the files accordingly if you do not use systemd

```
sh setup.sh
```

## Usage
If you have installed this then the script will be run everytime your system boots. To run the python file without installation, edit the file so that it takes `creds.data` from a different location(current directory) instead of `/root/scripts` and make sure to create creds.data(first line has email address, second line has password).

## License
See LICENSE

## Credits
http://github.com/maheshbansod
