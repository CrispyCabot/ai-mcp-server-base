# AI MCP Server Base

## Project Setup

### Prerequisites
- Made with Python 3.14.2 but other versions may work

### Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

#### Create a virtual environment
```bash
py -m venv .venv
```

#### Activate the virtual environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate
```

**Windows (Command Prompt):**
```cmd
.\.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

#### Deactivate the virtual environment
```bash
deactivate
```

### Installation

1. Activate your virtual environment.
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the FastAPI Server

To start the FastAPI server with hot-reloading enabled:

```bash
uvicorn app.main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.
You can access the API documentation at `http://127.0.0.1:8000/docs`.

### Running the MCP Server

You can run the MCP server using the MCP CLI, which provides a developer inspector for testing tools and resources.

```bash
mcp dev app/mcp_server/main.py
```

This will start the MCP server and open the MCP Inspector in your browser.

Alternatively, you can run it directly with Python (useful for deployment or simple testing):

```bash
python app/mcp_server/main.py
```

### Connecting via Postman (Streamable HTTP)

The MCP server runs using Streamable HTTP (which uses SSE for events). To connect via Postman:

1.  Start the MCP server using `python app/mcp_server/main.py`.
2.  Open Postman and click "New" > "MCP".
3.  Enter the URL: `http://localhost:8000/mcp`.
4.  Send the request.

You should see an event stream open. The server will send an endpoint URL in the `endpoint` event, which you can use for subsequent POST requests (JSON-RPC) to interact with tools and resources.

### Deployment (Docker)

This project includes a `Dockerfile` and `compose.yaml` for easy deployment.

#### Run with Docker Compose

To run the MCP server:

```bash
docker compose up --build
```

The server will be available at `http://localhost:8000`.

#### Build Docker Image

To build the Docker image manually:

```bash
docker build -t mcp-server .
```

#### Run Docker Container

To run the container (you can provide the `DB_DSN` environment variable if you have an external database):

```bash
docker run -p 8000:8000 -e DB_DSN="postgresql://user:password@host:5432/dbname" mcp-server
```

### Deployment (Render)

1.  Push your code to a GitHub repository.
2.  Log in to [Render](https://render.com/).
3.  Click **New +** and select **Web Service**.
4.  Connect your GitHub repository.
5.  Render will automatically detect the `Dockerfile`.
6.  **Important**: In the configuration:
    *   **Runtime**: Docker
    *   **Environment Variables**: Add `DB_DSN` if you have a database connection string.
7.  Click **Create Web Service**.

Render will build your Docker image and deploy it. You will get a public URL (e.g., `https://your-app.onrender.com`) where your MCP server is accessible.
