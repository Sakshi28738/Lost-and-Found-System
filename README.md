# Lost and Found Item Management System

A web-based Campus Lost and Found Management System that helps students report, search, and manage lost and found items within a campus.

## Features

- Dashboard displaying total, lost, found, and resolved reports
- Report lost items
- Report found items
- Search items by name
- Filter reports by category and status
- Update report status between Open and Resolved
- Persistent SQLite database storage
- Responsive user interface

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Podman
- Linux

## Project Structure

```text
Lost_and_Found_System/
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── index.html
│   └── report.html
├── app.py
├── database.py
├── requirements.txt
├── Containerfile
└── README.md
```

## Run Using Podman

### 1. Pull the application image

```bash
podman pull docker.io/sakshi454/lost-found-app:v2
```

### 2. Create a network and volume

```bash
podman network create lost-found-network
podman volume create lost-found-data
```

### 3. Run the container

```bash
podman run -d \
  --name lost-found-app \
  --network lost-found-network \
  -p 5000:5000 \
  -v lost-found-data:/data \
  docker.io/sakshi454/lost-found-app:v2
```

### 4. Access the application

Open the following address in your browser:

http://localhost:5000

## Container Management

Check running containers:

```bash
podman ps
```

View application logs:

```bash
podman logs lost-found-app
```

Stop the container:

```bash
podman stop lost-found-app
```

Start the container:

```bash
podman start lost-found-app
```

Remove the container:

```bash
podman rm -f lost-found-app
```

The named Podman volume preserves database data independently of the container.

## Docker Hub

Application image:

https://hub.docker.com/r/sakshi454/lost-found-app

## GitHub Repository

https://github.com/Sakshi28738/Lost-and-Found-System

