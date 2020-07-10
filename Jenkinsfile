pipeline{
		agent any
		stages{
			stage('Clone Repo'){
				steps{
					sh "bash Jenkins/repo.sh"
				}
			}
			stage('Install Requirements'){
				steps{
					sh "bash Jenkins/install-req.sh"
				}
			}
			stage('Testing'){
				steps{
					sh "bash Jenkins/testing.sh"
					
				}
			}
			stage('Build Images and Push'){
				steps{
					sh "Jenkins/docker.sh"
				}
			}
			stage('Deploy Ansible'){
				steps{
					sh "bash Jenkins/ansible.sh"
				}
			}
		}    
}
