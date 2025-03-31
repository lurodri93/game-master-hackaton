from fastapi import FastAPI
from pydantic import BaseModel
from character_generator import generate_character

app = FastAPI()

class CreateCharacterRequest(BaseModel):
    player_id: str = "anon"

@app.post("/create-character")
def create_character(request: CreateCharacterRequest):
    character = generate_character(request.player_id)
    return character
