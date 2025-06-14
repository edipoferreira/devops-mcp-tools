# Welcome to MCP DevOps Tools

This is the documentation for the MCP DevOps Tools.

## Available Tools

The following tools are available in the `DevOpsUtilityCommands` MCP server:

### Jenkins

These tools require the following environment variables to be set:

* `JENKINS_TOKEN`: Your Jenkins API token.
* `JENKINS_URL`: The base URL of your Jenkins instance (e.g., `http://localhost:8080`).

* `jenkins_api_get(endpoint: str) -> dict`: Performs a GET request to the Jenkins API.
* `jenkins_api_post(endpoint: str, data: str, content_type: str = "application/xml") -> dict`: Performs a POST request to the Jenkins API.

### Docker

* `docker_compose_up(path: str) -> str`: Runs `docker compose up -d` for a given Docker Compose file.
* `docker_compose_down(path: str) -> str`: Runs `docker compose down` for a given Docker Compose file.
* `docker_compose_logs(path: str, lines: int = 100) -> str`: Retrieves logs from a Docker Compose service.
* `docker_ps() -> list[dict]`: Lists running Docker containers.

### Kubernetes

* `get_pods_namespace(ns: str) -> dict`: Retrieves all pods in a given Kubernetes namespace.
* `get_namespaces() -> dict`: Retrieves the list of Kubernetes namespaces.

### Other

* `divide(a: float, b: float) -> str | float`: Divides two numbers.
