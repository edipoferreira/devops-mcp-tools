# MCP DevOps Tools

This repository contains a set of tools to be used with a Model Context Protocol (MCP) server.

## Prerequisites

* Python 3.10+
* Docker
* Kubernetes CLI (kubectl)

## Environment Variables

Create a `.env` file in the root of the project with the following variables:

```
PORT=8000
JENKINS_TOKEN=your_jenkins_token_here
JENKINS_URL=http://your_jenkins_url_here
```

## Installation

```bash
pip install -r code/mcp-devops-python/requirements.txt
```

## Running the server

```bash
python code/mcp-devops-python/server-mcp.py
```

## Documentation

To view the documentation, run:

```bash
mkdocs serve
```

Then open your browser to `http://127.0.0.1:8000`.

To deploy the documentation to GitHub Pages, run:

```bash
mkdocs gh-deploy
```
