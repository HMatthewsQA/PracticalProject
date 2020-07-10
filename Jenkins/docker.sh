#!/bin/bash
cd PracticalProject
cp /home/jenkins/.env var/lib/jenkins/workspace/PracticalProject/.env
docker-compose build
docker-compose push