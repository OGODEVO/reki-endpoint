from fastapi import FastAPI
from pydantic import BaseModel
from mlx_lm import load, generate

app = FastAPI()

# Load the model and tokenizer
model, tokenizer = load("reki-1")

class InferenceRequest(BaseModel):
    prompt: str

@app.post("/inference")
async def infer(request: InferenceRequest):
    """
    This endpoint takes a prompt and returns the model's response.
    """
    response = generate(model, tokenizer, prompt=request.prompt, verbose=True)
    return {"response": response}