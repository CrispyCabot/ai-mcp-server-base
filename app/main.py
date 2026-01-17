from fastapi import FastAPI
from app.api.v1.endpoints import sample_endpoint

app = FastAPI(title="AI MCP Server")

app.include_router(sample_endpoint.router, prefix="/api/v1", tags=["sample"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI MCP Server"}
