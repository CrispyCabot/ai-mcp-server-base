FROM python:3-slim

WORKDIR /app

# Install system dependencies (if any needed for asyncpg or others)
# RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Default command to run the MCP server
CMD ["python", "app/mcp_server/main.py"]
