from contextlib import asynccontextmanager
from typing import AsyncIterator

import asyncpg
from mcp.server.fastmcp import FastMCP, Context

# Placeholder database credentials - USER TO REPLACE
DB_DSN = "postgresql://user:password@localhost:5432/dbname"

@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[dict]:
    """
    Lifespan context manager for the MCP server.
    Handles database connection setup and teardown.
    """
    try:
        # In a real scenario, you might want to use a connection pool
        # pool = await asyncpg.create_pool(DB_DSN)
        # yield {"pool": pool}
        # await pool.close()
        
        # For this sample, we'll just simulate a connection or try to connect
        # If no DB is available, this might fail, so we'll wrap it gracefully for the sample
        print(f"Attempting to connect to database at {DB_DSN}...")
        # conn = await asyncpg.connect(DB_DSN) 
        # yield {"conn": conn}
        # await conn.close()
        
        # MOCKING the connection for the sample to ensure it runs without a real DB
        # In production, uncomment the lines above and remove the mock
        mock_conn = {"status": "connected", "mock": True}
        yield {"conn": mock_conn}
        
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        yield {"conn": None}

mcp = FastMCP("base-mcp-server", lifespan=server_lifespan, host="0.0.0.0", port=8000)

@mcp.tool()
async def query_sample_db(query: str, ctx: Context) -> str:
    """
    Executes a read-only query against the sample database.
    """
    conn = ctx.request_context.lifespan_context.get("conn")
    
    if not conn:
        return "Error: No database connection available."
        
    if conn.get("mock"):
        return f"Mock Result for query '{query}': [{{'id': 1, 'name': 'Alice'}}, {{'id': 2, 'name': 'Bob'}}]"

    # Real implementation would look like:
    # try:
    #     results = await conn.fetch(query)
    #     return str(results)
    # except Exception as e:
    #     return f"Database error: {e}"

@mcp.resource("db://status")
async def get_db_status(ctx: Context) -> str:
    """
    Returns the current status of the database connection.
    """
    conn = ctx.request_context.lifespan_context.get("conn")
    if conn:
        return "Database is CONNECTED."
    else:
        return "Database is DISCONNECTED."

@mcp.prompt()
def sql_helper(table_name: str) -> str:
    """
    Returns a template for writing a SQL query for a specific table.
    """
    return f"Please write a SQL query to select all columns from the table '{table_name}' where the created_at date is after 2024-01-01."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")