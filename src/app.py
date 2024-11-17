from fastapi import FastAPI, HTTPException
import httpx
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update this with the frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dictionary API base URL
DICTIONARY_API_BASE = "https://api.dictionaryapi.dev/api/v2/entries/en/"

@app.get("/dictionary/{word}")
async def check_word(word: str):
    """
    Validate if a word exists in the dictionary.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DICTIONARY_API_BASE}{word}")
        if response.status_code == 200:
            return {"word": word, "valid": True}
        else:
            raise HTTPException(status_code=404, detail="Word not found")