pipeline{
		agent any
		stages{
			stage('Clone Repo'){
				steps{
					sh "git clone -b development https://github.com/HMatthewsQA/PracticalProject"
				}
			}
			stage('Install Requirements'){
				steps{
					sh "sudo apt update && sudo apt install -y curl jq"
					sh "curl https://get.docker.com | sudo bash"
					sh "version=\$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')"
					sh "sudo curl -L 'https://github.com/docker/compose/releases/download/\${version}/docker-compose-\$(uname -s)-\$(uname -m)' -o /usr/local/bin/docker-compose"
					sh "sudo chmod +x /usr/local/bin/docker-compose"
					sh "sudo apt-get python-pip -y"
					sh "sudo apt-get python3-pip -y"
					sh "cd PracticalProject/app1 && pip install -r requirements.txt"
				}
			}
			stage('Testing'){
				steps{
					sh ""
					sh "cd PracticalProject/app1 && pytest"
					sh "cd PracticalProject/app2 && pytest"
					sh "cd PracticalProject/app3 && pytest"
					sh "cd PracticalProject/app4 && pytest"
				}
			}
			stage('Build Images and Push'){
				steps{
					sh "cd PracticalProject && docker-compose build"
					sh "cd PracticalProject && docker-compose push"
				}
			}
			stage('Deploy Ansible'){
				steps{
					sh "cd PracticalProject && ansible-playbook playbook.yaml"
				}
			}
		}    
}
