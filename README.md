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

- git clone <your-github-repo-url>  #wait to clone the repository
- cd interview_scheduler            #navigate to the project directory
- docker-compose build              #build the docker container
- docker-compose up                 #Run the docker container

#### Api EndPoints

Api Documentation : ( https://www.notion.so/API-Documentation-Interview-Scheduler-ac5e1d3feb434694ad5bf7580fe84147?pvs=4 )