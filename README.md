# Interview Scheduler

## Overview

    The **Interview Scheduler** is an API designed to help HR schedule and manage interviews efficiently. This application allows users to create interview slots, making it easier to track candidates and their interview status.

### Features

- Candidates and interviewers can register themselves.
- Candidates and interviewers can update their available time slots.
- HR can view all registered candidates and interviewers.
- HR can schedule interviews by viewing the common available time slots for a candidate and an interviewer by their ID.
- Built with Django and Docker for easy deployment.

## Technologies Used

- **Django**
- **Django REST Framework**
- **Docker**
- **SQLite**

## Prerequisites

Before running the project, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

Follow these steps to set up and run the Interview Scheduler project locally using Docker:

### 1. Clone the Repository

Open your terminal, navigate to the desired path and run the following command to clone the repository:

- git clone https://github.com/ajithanil0727/Interview_Scheduler.git    #wait to clone the repository
- cd interview_scheduler                                                #navigate to the project directory
- docker-compose build                                                  #build the docker container, make sure docker engine is runnig in the sysytem
- docker-compose up                                                     #Run the docker container

*If some error occure showing something like "Table not created", After "docker-compose up" command open another terminal with same root folder and run the below command else continue to use the api.

- docker-compose exec web python manage.py migrate

## Tool recommened to test Interview_Scheduler

- Postman: For testing and interacting with API endpoints.
- SQLite Studio: For viewing and managing the database.


### 2. Api EndPoints

Api Documentation : ( https://www.notion.so/API-Documentation-Interview-Scheduler-ac5e1d3feb434694ad5bf7580fe84147?pvs=4 )


