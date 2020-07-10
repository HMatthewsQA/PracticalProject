#!/bin/bash
cp /home/jenkins/.env var/lib/jenkins/workspace/PracticalProjectPipeline/.env
docker-compose build
docker-compose push