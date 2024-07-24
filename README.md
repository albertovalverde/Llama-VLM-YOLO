# llama3
LLaMa 3  lab



```markdown
# Docker Project: LLaMA 3 and Flask Application

This repository contains Dockerfiles and instructions to run two Docker containers: one for LLaMA 3 and another for a Python application with Flask that consumes the API exposed by LLaMA 3.

## Running the Containers

### Building and Running the LLaMA 3 Container

```bash
# Build and run the LLaMA 3 container
docker build -t ollama-container .
docker run -p 11434:11434 ollama-container
```

### Building and Running the Python and Flask Container to Consume the API

```bash
# Build and run the Python and Flask container
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

### Running Containers with Docker Compose

To run both containers together using Docker Compose:

1. Create a `docker-compose.yml` file in your project directory with the following content:

```yaml
version: '3.8'

services:
  llama3:
    build:
      context: .
      dockerfile: Dockerfile-ollama
    ports:
      - "11434:11434"

  flaskapp:
    build:
      context: .
      dockerfile: Dockerfile-flask
    ports:
      - "5000:5000"
    depends_on:
      - llama3
```

2. Run the following command in the directory containing `docker-compose.yml`:

```bash
docker-compose up
```

## Repository Structure

- `Dockerfile-ollama`: Dockerfile for the LLaMA 3 container.
- `Dockerfile-flask`: Dockerfile for the Python and Flask container.
- `app.py`: Script containing the Flask application that consumes LLaMA 3 API.
- Other necessary files and directories for your application.

## Contributions

If you wish to contribute improvements or fixes, feel free to do so through Pull Requests. Any suggestions are welcome.

