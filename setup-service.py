import os

if __name__ == "__main__":
    command = """cat > /etc/systemd/system/homesolar.service <<EOF
[Unit]
Description=Monitoring and Controls for Solar Energy Systems
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/homesolar/main.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target"""
    
    os.system(command)
    os.system("systemctl daemon-restart")
    os.system("systemctl enable homesolar.service")
    os.system("systemctl start homesolar.service")