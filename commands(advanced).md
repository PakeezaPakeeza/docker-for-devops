# Docker Advanced Commands

## 1. Docker System and Image Management

- **Remove unused Docker data**:
  ```bash
  docker system prune
  ```
  *Cleans up unused images, containers, and networks.*

- **List all Docker images**:
  ```bash
  docker images
  ```
  *Displays all Docker images on your system.*

- **Remove a specific image by ID**:
  ```bash
  docker rmi <image_id>
  ```
  *Deletes the specified Docker image.*

## 2. Working with Docker Containers

- **Run MySQL container in detached mode with environment variables**:
  ```bash
  docker run -d -e MYSQL_ROOT_PASSWORD=root mysql:latest
  ```
  *Starts a MySQL container with the root password set to 'root' and runs in the background.*

- **Execute commands inside a running container**:
  ```bash
  docker exec -it <container_id> bash
  ```
  *Accesses the running container’s shell.*

- **Stop a running container**:
  ```bash
  docker stop <container_id>
  ```
  *Stops the specified container.*

- **Remove a stopped container**:
  ```bash
  docker rm <container_id>
  ```
  *Deletes the specified container from the system.*

## 3. Volume Management

- **Create a named volume**:
  ```bash
  docker volume create <volume_name>
  ```
  *Creates a new persistent Docker volume.*

- **List all volumes**:
  ```bash
  docker volume ls
  ```
  *Shows all Docker volumes on your system.*

- **Inspect a specific volume**:
  ```bash
  docker volume inspect <volume_name>
  ```
  *Displays details of a specific Docker volume.*

- **Remove a specific volume**:
  ```bash
  docker volume rm <volume_name>
  ```
  *Deletes the specified Docker volume.*

## 4. Docker Networking

- **Create a custom Docker network**:
  ```bash
  docker network create -d bridge twitier-bridge
  ```
  *Sets up a custom bridge network named 'twitier-bridge'.*

- **Inspect a Docker network**:
  ```bash
  docker network inspect <network_id>
  ```
  *Displays details of the specified Docker network.*

- **List all Docker networks**:
  ```bash
  docker network ls
  ```
  *Shows all Docker networks.*

## 5. Docker Compose

- **Check Docker Compose configuration**:
  ```bash
  docker compose config
  ```
  *Verifies and displays the Compose file configuration.*

- **Start services defined in Docker Compose file**:
  ```bash
  docker compose up
  ```
  *Launches all services as per `docker-compose.yml`.*

- **Rebuild and start services**:
  ```bash
  docker compose up --build
  ```
  *Rebuilds images and starts services with updated code.*

- **Stop and remove all services**:
  ```bash
  docker compose down
  ```
  *Stops and removes containers, networks, and volumes defined by Compose.*

## 6. Miscellaneous Commands

- **Inspect logs of a container**:
  ```bash
  docker logs <container_id>
  ```
  *Shows the log output of the specified container.*

- **Remove all stopped containers**:
  ```bash
  docker rm $(docker ps -a -q)
  ```
  *Deletes all stopped containers.*

- **Remove all unused images**:
  ```bash
  docker rmi -f $(docker images -q)
  ```
  *Forces deletion of all unused Docker images.*
