sudo apt update && sudo apt install -y curl jq
curl https://get.docker.com | sudo bash
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L 'https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)' -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo apt-get install python-pip -y
sudo apt-get install python3-pip -y
pip install pytest
pip install pytest-cov
pip install requests
pip install flask
pip install flask_sqlalchemy
pip install flask_wtf
pip install pymysql[rsa]
pip install Werkzeug