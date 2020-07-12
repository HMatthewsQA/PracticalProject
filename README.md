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
* 2nd Implementation

### My approach

My approach to this project was quite direct and to the point. First I made sure I had a working flask application with the four services that were required with docker compose. Once I had done this I moved onto testing the application and the functions that it entails. Next was getting Jenkins setup so I could begin automating the deployment process and my pipeline. Once I had Jenkins operational I began the process of designing and implementing a working Pipeline job that was initialised by a webhook from my GitHub Repository. Upon recieving this, I then implemented the required steps in my pipeline to rigorously test, initialise and deploy my service using the industry tools set out in our requirements. Now that my service was functioning I could make use of an NGINX service to robustly protect our network using a HTTP reverse proxy configuration. All of these steps compose a completed service that operates funcitonally with automation, configuation management and containerisation within a stack as set out in the brief and requirements.

## Architecture

### Database Structure

The database in this project has a very simple structure as there is only one table required to use the service. Therefore there are no relationships to model.

![ERD][erd]

Above is a model of the table that was used to store and collect data for the services that composed the flask web app.

### CI Pipeline

Below is initial early concept diagram for the Continous Integration (CI) Pipeline that was used to operate and deploy this project.

![CI][ci]

Upon revision and development the CI pipeline became more fleshed out and thorough in its design. This new design can be seen in the more detailed image below.

![CI2][ci2]

Here is an image that displays my Jenkins pipeline process and the numerous stages that it undertakes in order to make sure that the service is deployed appropriately and functionally.

![Jenkins][jenkins]

During the design and implemation stage of the Jenkins process this pipeline underwent many developments, the progress of which can be seen inside the documents folder of this repository.

The logs of this pipeline job within Jenkins can also be used to view the processes and their results, including the outcome the of the pytest testing that is a part of the job.

## Project Tracking

A Trello board was used to manage project development. Below is an image of this board towards the end of development. The progress of this board can be seen inside the documents folder.

![Trello][trello]

## Risk Assessment


![RiskAssessment][riskassessment]

I have completed a risk assessment to help me understand the ways that my application and its resources might come under threat and how I can plan to mitigate or prevent these circumstances.

## Testing

## Known Issues

## Future Improvements

## Authors

Harry Matthews

[riskassessment]: https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/RiskAssessment.png?raw=true "Risk Assessment"
[erd]: https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/ERD/PPerd.png?raw=true "ERD"
[trello]: https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/Trello/Trello3.png?raw=true "Trello Board"
[jenkins]:https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/Jenkins/JenkinsPipeline3.png?raw=true "Jenkins Pipeline"
[ci1]: https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/CIPipeline.png?raw=true "CI Pipeline"
[ci2]: https://github.com/HMatthewsQA/PracticalProject/blob/development/Documents/CIPipeline2.png?raw=true "CI Pipeline"