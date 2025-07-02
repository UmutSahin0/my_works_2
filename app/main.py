# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

fast_app = FastAPI()

class CountRequest(BaseModel):
    number: int

def count_logic(number: int) -> str:
    if number < 1:
        raise ValueError("Number must be >= 1")
    return "".join(str(i) for i in range(1, number + 1))

@fast_app.post("/count")
def count_up(request: CountRequest):
    try:
        result = count_logic(request.number)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    print(result)
    return {"result": result}
