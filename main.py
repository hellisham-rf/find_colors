from fastapi import FastAPI
from pydantic import BaseModel
from utils import generator
app = FastAPI()


class Text(BaseModel):
    context: str

@app.post("/color")
def ColorGR(text: Text):
    color = generator(f"Given text: {text.context}")
    return {"Text Colors": color}



