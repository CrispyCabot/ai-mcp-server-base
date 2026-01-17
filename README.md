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
