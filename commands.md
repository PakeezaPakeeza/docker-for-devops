
# Docker and Git Commands

## System Setup
```bash
sudo apt-get update
sudo apt-get install docker.io
docker --version
```

## Docker Service
```bash
systemctl status docker
sudo gpasswd -a ubuntu docker && newgrp docker
```
### List running containers:
```bash
docker ps
```

### Run an Nginx container:
```bash
docker run -d nginx:latest
docker run -d -p 80:80 nginx:latest
```
### Run a mysql container:
```bash
docker pull mysql
docker run -e  MYSQL_ROOT_PASSWORD=test123 mysql:latest
´´´´
### Execute bash inside a running container(in our case mysql):
```bash
docker exec -it <container_id> bash
mysql -u root -p 
```

### Kill a running container:
```bash
docker kill <container_id>
```

### View container ports:
```bash
docker port <container_id>
```

### Build and Run Custom Images:

#### Build an image:
```bash
docker build -t my-counter-final .
```

#### Run the image:
```bash
docker run -d -p 8000:8000 my-counter-final:latest
```

### Remove images:
```bash
docker rmi <image_id>
docker rmi -f <image_id>
```

## Docker Logs:

### View logs for a specific container:
```bash
docker logs <container_id>
```

## Git Commands:

### Clone repositories:
```bash
git clone https://github.com/LondheShubham153/simple-java-docker.git
git clone https://github.com/deparkes/simple-django-app.git
```

### Git Status:
```bash
git status
```

## Folder and File Management:

### Create directories and manage files:
```bash
mkdir github
rm -v Dockerfile
```


## Stopping and Removing Containers

### Stop all running containers:
```bash
docker stop $(docker ps -a -q)
```

### Remove all stopped containers:
```bash
docker rm $(docker ps -a -q)
```

### List all containers:
```bash
docker ps -a
```

## Remove All Images

### Force remove all Docker images:
```bash
docker rmi -f $(docker images -q)
```
