# Static Python App (Flask) – AWS EC2 Deployment

## Structure
```
static-python-app/
├── app.py
├── wsgi.py
├── requirements.txt
├── templates/   (base.html, index.html, about.html)
├── static/      (css/style.css, js/main.js)
└── deploy/      (flaskapp.service, nginx.conf, setup.sh)
```

## Run locally
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py                   # http://localhost:5000
```

## Deploy on EC2 (Ubuntu 22.04/24.04)
1. Launch an EC2 instance (t2.micro/t3.micro is fine, free tier eligible).
2. Security Group inbound rules: SSH (22) from My IP, HTTP (80) from 0.0.0.0/0.
3. Copy the project to the server:
   ```bash
   scp -i your-key.pem -r static-python-app ubuntu@<EC2_PUBLIC_IP>:~/
   ```
4. SSH in and run the setup script:
   ```bash
   ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>
   cd ~/static-python-app
   bash deploy/setup.sh
   ```
5. Open `http://<EC2_PUBLIC_IP>/`

## Useful commands
```bash
sudo systemctl status flaskapp
sudo journalctl -u flaskapp -f
sudo systemctl restart flaskapp
sudo systemctl restart nginx
sudo tail -f /var/log/nginx/error.log
```

## Update after code changes
```bash
cd ~/static-python-app && git pull   # or scp new files
sudo systemctl restart flaskapp
```

Note: if you use Amazon Linux instead of Ubuntu, change the user to `ec2-user`
in `flaskapp.service` and `nginx.conf` paths, and use `dnf` instead of `apt`.
