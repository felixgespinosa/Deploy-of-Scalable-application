
# Creativa 2 for CDPS

This project aims to evaluate different technologies for the deployment of application services with the ultimate goal of making a reliable and scalable application.
The Google Cloud infrastructure will be used to deploy the technologies in different virtual machines bases on a Debian GNU/Linux 10 (buster) image.


## Types of deployments

###  Monolithic application using heavy virtual machine deployment
The first technology will be the deployment of the application in a Monolithic way directly on a VM within the Google Cloud infrastructure.
###  Monolithic application using Docker deployment
A VM like the one metioned above will be created again, but now lightweight virtualization will be used. To do this, a Docker container will be created inside where the service will be executed monolitically.
###  Microservices application using Docker-Compose deployment
The application has now been segmented into microservices, so each one works independtly. Each microserve is programmed in a different language.
The services are productpage, details, reviews, and ratings. With the Docker-Compose file they will each be deployed in a different container.
###  Microservices application using K8s deployment
This last section is the same than above but using Kubernetes instead.
For the deployment, the starting point is the images constructed in the previous sections. To be able to use them in a simple way, they have been saved in dockerhub, where they are publicly accessible.
