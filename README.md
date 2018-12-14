PROMS Server
============

PROMS Server is a web server and database application consisting of a Python Flask RESTful API that enforces data policy according to the PROMS methodologies outlined at https://wiki.csiro.au/display/PROMS.

PROMS Server may be installed as per instructions in the installation/ subfolder.


Features
--------
Please see the CHANGELOG.md file for version notes.


Support
-------
More information is available on the project webpage: https://wiki.csiro.au/display/PROMS.



Add by fang
------------
Config here about uwsgi, nginx
Set the socket file on /run/uwsgi/proms.socket
Set Authtication 0777
The uwsgi run in mode of root
Set the nginx error log in /var/log/proms/nginx-error.log

I setted the process numbers to 2 , this is a debug mode
set the process numbers to your CPU core number , when this procedure is online 

