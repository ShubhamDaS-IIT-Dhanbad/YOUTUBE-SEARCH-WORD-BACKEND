from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI(
    title="YouTube Transcript Search API",
    description="Search through YouTube video transcripts easily",
    version="1.0.0"
)

# Allow CORS for all origins (adjust if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to YouTube-Search-Video"}

# Include API routes
app.include_router(api_router, prefix="/api")
