from fastapi import FastAPI, HTTPException
from brandforge import generate_branding_snippet, generate_keywords
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

MAX_INPUT_LENGTH = 32


@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}


@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}


@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}


def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400,
                            detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.")

# uvicorn brandforge_api:image --reload
