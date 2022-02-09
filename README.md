# Cloud Native Application Architecture Nanodegree

## TechTrends Project

###Background
TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.

Imagine the following scenario: you joined a small team as a Platform Engineer. The team is composed of 2 developers, 1 platform engineer (you), 1 project manager, and 1 manager. The team was assigned with the TechTrends project, aiming to build a fully functional online news sharing platform. The developers in the team are currently working on the first prototype of the TechTrends website. As a platform engineer, you should package and deploy TechTrends to Kubernetes using a CI/CD pipeline.

The web application is written using the Python Flask framework. It uses SQLite, a lightweight disk-based database to store the submitted articles.

### Submission Requirements


1. Apply the best development practices and develop the status and health check endpoints for the TechTrends application.
        
2. Package the TechTrends application by creating a Dockerfile and Docker image.
        
3. Implement the Continuous Integration practices, by using GitHub Actions to automate the build and push of the Docker image to DockerHub.

4. Construct the Kubernetes declarative manifests to deploy TechTrends to a sandbox namespace within a Kubernetes cluster. The cluster should be provisioned using k3s in a vagrant box.
Template the Kubernetes manifests using a Helm chart and provide the input configuration files for staging and production environments.
Implement the Continuous Delivery practices, by deploying the TechTrends application to staging and production environments using ArgoCD and the Helm chart.

## Tech Stack

### Web App
* [Python](https://www.python.org/downloads/)
* [Flask](https://flask.palletsprojects.com/)
* [SQLite](https://www.sqlite.org/)

### Containerization & Virtualization
* [Docker](https://www.docker.com/)
* [Vagrant](https://www.vagrantup.com/)

### CI/CD 
* [Github Actions](https://github.com/features/actions)
* [ArgoCD](https://argoproj.github.io/argo-cd/)

### Deployment & Management of Containers
* [K3S](https://k3s.io/)

## Running TechTrends Project

### Building TechTrends Image

From the repository's root folder, build the app image:

```
$docker build -t lynettemidy/techtrends .
```

The build process will install all dependencies and start the SQLite DB, then expose port `3111` for this image.

### Running the Image

Run a container and test it locally:

```
docker run -d --name techtrends -p HOST_PORT:3111 lynettemidy/techtrends
```

### Screenshot of TechTrends Running


![TechTrends running on localhost!](https://github.com/lmidy/TechTrends/blob/main/screenshots/TechTrends-Running.png)
