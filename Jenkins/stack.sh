ssh jenkins@master-vm << EOF
cd /home/hmatthews/PracticalProject
env SECRET_KEY=${SECRET_KEY} env DATABASE_URI=${DATABASE_URI} docker stack deploy --compose-file docker-compose.yaml app
EOF