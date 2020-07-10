pipeline{
		agent any
		stages{
			stage('Clone Repo'){
				steps{
					sh "git clone https://github.com/HMatthewsQA/PracticalProject/tree/development"
				}
			}
			stage('Testing'){
				steps{
					sh "cd PracticalProject/tree/development/app1 && pytest"
					sh "cd PracticalProject/tree/development/app2 && pytest"
					sh "cd PracticalProject/tree/development/app3 && pytest"
					sh "cd PracticalProject/tree/development/app4 && pytest"
				}
			}
			stage('Install Docker'){
				steps{
					sh "sudo apt update && sudo apt install -y curl jq"
					sh "curl https://get.docker.com | sudo bash"
					sh "version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')"
					sh "sudo curl -L 'https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)' -o /usr/local/bin/docker-compose"
					sh "sudo chmod +x /usr/local/bin/docker-compose"
				}
			}
			stage('Build Images and Push'){
				steps{
					sh "docker-compose build"
					sh "docker-compose push"
				}
			}
			stage('Deploy Ansible'){
				steps{
					sh "cd PracticalProject/tree/development && ansible-playbook playbook.yaml"
				}
			}
		}    
}
