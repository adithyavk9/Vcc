# Flask Docker Application

## Overview

This repository contains a sample web application built using Flask and deployed in a Docker container.

## Application Functionality

The application is a simple Flask web server that displays "time table for PGDE trimester 2" when accessed at the root URL.

## Steps to Deploy

1. **Set Up a Project Directory**
   Create a new directory for your project and navigate into it.

2. **Create a Flask Application**
   Add `app.py` to define a simple Flask app.

3. **Create a Requirements File**
   Add `requirements.txt` to list the required Python packages.

4. **Create a Dockerfile**
   Write a `Dockerfile` to build an image for the Flask application.

5. **Build the Docker Image**
   Run `docker build -t app .` to build the image.

6. **Run the Docker Container**
   Start the container with `docker run -p 5000:5000 app`.

## Author

-**Name**: Adithya V K

-**Roll Number**: G23AI2042









Docker is a set of Platforms as a service (PaaS) products by which you can pack your application and all its dependencies into a standardized unit called a container. Containers are light in weight which makes them portable and they are isolated from the underlying infrastructure and from each other container. You can run the docker image as a docker container in any machine where docker is installed without depending on the operating system.

Dockerfile: The Dockerfile uses DSL (Domain Specific Language) and contains instructions for generating a Docker image. Dockerfile will define the processes to quickly produce an image. 
Docker Image: It is a read-only template that is used for creating containers, containing the application code and dependencies.
Docker container is a runtime instance of an image. Allows developers to package applications with all parts needed such as libraries and other dependencies. 