#!/usr/bin/env python


from fastmcp import FastMCP
from dotenv import load_dotenv
import subprocess
import json
import os



mcp = FastMCP('DevOpsUtilityCommands')
load_dotenv()

jenkins_token = os.getenv("JENKINS_TOKEN")
jenkins_url = os.getenv("JENKINS_URL", "http://localhost:8081")


@mcp.tool()
def jenkins_api_get(endpoint: str) -> dict:
    """
    Performs a GET request to the Jenkins API at the specified endpoint.

    Args:
        endpoint (str): The endpoint to call on the Jenkins API.

    Returns:
        dict: The JSON response from the Jenkins API.

    Raises:
        subprocess.CalledProcessError: If the command fails.
        json.JSONDecodeError: If the output cannot be parsed as JSON.
    """
    if not jenkins_token:
        raise ValueError("JENKINS_TOKEN environment variable not set.")

    user = "admin"
    base_url = jenkins_url
    
    command = [
        "curl",
        "-s",
        "-u", f"{user}:{jenkins_token}",
        f"{base_url}/{endpoint}"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        if not result.stdout.strip():
            return {"status": "success", "message": "Empty response from Jenkins."}
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error calling Jenkins API: {e.stderr}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from Jenkins API. Response: {result.stdout}")
        raise

@mcp.tool()
def jenkins_api_post(endpoint: str, data: str, content_type: str = "application/xml") -> dict:
    """
    Performs a POST request to the Jenkins API at the specified endpoint.

    Args:
        endpoint (str): The endpoint to call on the Jenkins API.
        data (str): The data to send in the request body.
        content_type (str): The content type of the request.

    Returns:
        dict: The JSON response from the Jenkins API.

    Raises:
        subprocess.CalledProcessError: If the command fails.
        json.JSONDecodeError: If the output cannot be parsed as JSON.
    """
    if not jenkins_token:
        raise ValueError("JENKINS_TOKEN environment variable not set.")

    user = "admin"
    base_url = "http://localhost:8081"
    
    command = [
        "curl",
        "-s",
        "-X", "POST",
        "-u", f"{user}:{jenkins_token}",
        "-H", f"Content-Type: {content_type}",
        "--data", data,
        f"{base_url}/{endpoint}"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        if not result.stdout.strip():
            return {"status": "success", "message": "Empty response from Jenkins."}
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error calling Jenkins API: {e.stderr}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from Jenkins API. Response: {result.stdout}")
        raise

@mcp.tool()
def docker_compose_up(path: str) -> str:
    """
    Runs 'docker compose up' command with the specified path to the Docker Compose YAML file.

    Args:
        path (str): The path to the Docker Compose YAML file.

    Returns:
        str: The output of the 'docker compose up' command.

    Raises:
        subprocess.CalledProcessError: If the command fails.
    """
    output = subprocess.check_output(
        ["docker", "compose", "-f", path, "up", "-d"],
        text=True
    )
    return output.strip()


@mcp.tool()
def docker_compose_down(path: str) -> str:
    """
    Runs 'docker compose down' command with the specified path to the Docker Compose YAML file.

    Args:
        path (str): The path to the Docker Compose YAML file.

    Returns:
        str: The output of the 'docker compose down' command.

    Raises:
        subprocess.CalledProcessError: If the command fails.
    """
    output = subprocess.check_output(
        ["docker", "compose", "-f", path, "down"],
        text=True
    )
    return output.strip()


@mcp.tool()
def docker_compose_logs(path: str, lines: int = 100) -> str:
    """
    Retrieves logs from a Docker Compose service.

    Args:
        path (str): The path to the Docker Compose YAML file.
        lines (int): The number of lines of logs to retrieve. Defaults to 100.

    Returns:
        str: The output of the 'docker compose logs' command.

    Raises:
        subprocess.CalledProcessError: If the command fails.
    """
    output = subprocess.check_output(
        ["docker", "compose", "-f", path, "logs", "--tail", str(lines)],
        text=True
    )
    return output.strip()



@mcp.tool()
def docker_ps() -> list[dict]:
  """
  Runs the 'docker ps' command with JSON output format and returns the parsed result.

  Returns:
    list[dict]: A list of dictionaries, where each dictionary represents a running Docker container.

  Raises:
    subprocess.CalledProcessError: If the 'docker ps' command fails.
    json.JSONDecodeError: If the output cannot be parsed as JSON.
  """
  output = subprocess.check_output(
    ["docker", "ps", "--format", "json"],
    text=True
  )
  output = output.strip()
  if not output:
    return []
  return [json.loads(line) for line in output.split('\n')]

@mcp.tool()
def get_pods_namespace(ns: str) -> dict:
  """
  Retrieves all pods in the specified Kubernetes namespace.

  Args:
    ns (str): The name of the Kubernetes namespace.

  Returns:
    dict: A dictionary representing the JSON output of the pods in the given namespace.

  Raises:
    subprocess.CalledProcessError: If the kubectl command fails.
    json.JSONDecodeError: If the output is not valid JSON.
  """
  output = subprocess.check_output(
    ["kubectl", "get", "pods", "-n", ns, "-o", "json"],
    text=True
  )
  return json.loads(output)  


@mcp.tool()
def get_namespaces() -> dict:
  """
  Retrieves the list of Kubernetes namespaces as a dictionary.

  Uses the 'kubectl' command-line tool to fetch all namespaces in the current Kubernetes context,
  parsing the output as JSON.

  Returns:
    dict: A dictionary representation of the namespaces as returned by 'kubectl'.

  Raises:
    subprocess.CalledProcessError: If the 'kubectl' command fails.
    json.JSONDecodeError: If the output cannot be parsed as JSON.
  """
  output = subprocess.check_output(
    ["kubectl", "get", "namespace","-o", "json"],
    text=True
  )
  return json.loads(output)  


@mcp.tool()
def divide(a:float, b:float) -> str | float:
    """Divides 2 numbers
        Args:
        a: Dividend
        b: Divisor"""

    if b == 0:
        return "Cannot divide by zero."
    else:
        return a/b


if __name__ == "__main__":
  mcp.run(transport="stdio")