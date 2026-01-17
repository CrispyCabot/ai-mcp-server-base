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

### Running the Server

To start the FastAPI server with hot-reloading enabled:

```bash
uvicorn app.main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.
You can access the API documentation at `http://127.0.0.1:8000/docs`.
