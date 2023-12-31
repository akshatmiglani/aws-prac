install mysql client on EC2 instance

sudo apt-get install mysql-server
sudo apt-get install mysql-client

access amazon RDS using mysql -h <endpoint> -u <user> -p

for python
sudo apt-get install python3
sudo apt-get install python3-flask
sudo apt-get install python3-pymysql

for automating service on startup

sudo apt install gunicorn

test working
gunicorn -w 5 -b 0.0.0.0:80 record:app

create a service
sudo nano /etc/systemd/system/proj.service

[Unit]
Description=Gunicorn instance for a simple hello world app
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/aws-prac
ExecStart=/user/bin/gunicorn -b 0.0.0.0:80 record:app
Restart=always
[Install]
WantedBy=multi-user.target


sudo systemctl daemon-reload
sudo systemctl start proj
sudo systemctl enable proj

use ngnix for reverse-proxy

sudo apt-get nginx

sudo systemctl start nginx
sudo systemctl enable nginx

-> add below to ngnix/sites-available/default
upstream dothis{
    server 0.0.0.0:80;
}

location / {
    proxy_pass http://dothis;
    include proxy_params;
    proxy_redirect off;
}

location /submit_feedback {
    proxy_pass http://dothis;
    include proxy_params;
    proxy_redirect off;
}
