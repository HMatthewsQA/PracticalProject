# PracticalProject

## My Resources:
* Trello: https://trello.com/b/oBvMPLWJ/practical-project

## Contents
* [Brief](#brief)
   * [Additional Requirements](#additional-requirements)
   * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Database Structure](#database-structure)
   * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Authors](#authors)

## Brief

You are required to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together, you are creating an application that generates “Objects” upon a set of predefined rules.

For services #2, #3 and #4 you need to create 2 different implementations, you must be able to demonstrate swapping these implementations out for each other seamlessly, without disrupting the user experience.

### Additional Requirements

* Github webhook for automation
* Testing
* NGINX reverse proxy
* Jenkins Pipeline
* Ansible Configuration Management
* Docker swarm
* Feature Branch version control

### My approach



## Architecture

### Database Structure

The database in this project has a very simple structure as there is only one table required to use the service. Therefore there are no relationships to model.

![ERD][erd]

### CI Pipeline

Below is a diagram to demonstrate the Continous Integration Pipeline that was used to operate and deploy this project.


![CI][ci]



Here is an image that displays my jenkins pipeline process

![Jenkins][jenkins]

The progress of this pipeline can be seen inside the documents folder.

Jenkins logs

## Project Tracking

A Trello board was used to manage project development. Below is an image of this board towards the end of development. The progress of this board can be seen inside the documents folder.

![Trello][trello]

## Risk Assessment

## Testing

## Known Issues

## Future Improvements

## Authors

Harry Matthews

[trello]: https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/Trello/Trello3.png?raw=true "Trello Board"
[jenkins]:https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/Jenkins/JenkinsPipeline3.png?raw=true "Jenkins Pipeline"
[ci]: https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/CIPipeline.png?raw=true "CI Pipeline"