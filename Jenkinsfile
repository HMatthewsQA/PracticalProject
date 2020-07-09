pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                }
            }
            stage('Build Images'){
                steps{
			image = docker.build("hmattthews/practicalproj-app1")
			image = docker.build("hmattthews/practicalproj-app2")
			image = docker.build("hmattthews/practicalproj-app3")
			image = docker.build("hmattthews/practicalproj-app4")
                }
            }
	    stage('Push to DockerHub'){
		steps{
		}
	    }
	    stage('Deploy Ansible'){
                steps{
                }
            }
        }    
}
