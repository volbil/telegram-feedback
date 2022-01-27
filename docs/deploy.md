[Unit]
Description=Gunicorn instance for feedback service
After=network.target

[Service]
User=user
Group=www-data
WorkingDirectory=/home/user/telegram-feedback
Environment="PATH=/home/user/telegram-feedback/venv/bin"
ExecStart=/home/user/telegram-feedback/venv/bin/gunicorn app:app --worker-class gevent -w 1 --bind 0.0.0.0:4321 --reload

[Install]
WantedBy=multi-user.target

sudo nano /etc/systemd/system/feedback.service

server {
    server_name example.com;

    location / {
        proxy_pass http://localhost:4321;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    listen 80;
}

sudo nano /etc/nginx/sites-available/example.com.conf
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled
