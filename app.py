from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

sample_actions = [
    "Identify target market segments",
    "Craft positioning statement",
    "Define pricing strategy",
    "Plan launch marketing channels",
    "Set up sales enablement materials",
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(plan: Prompt):
    intro = f"GTM Plan for: {plan.prompt}\n\nKey actions:\n"
    actions = "\n".join(f"- {a}" for a in sample_actions)
    return {"plan": intro + actions}
