from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CountRequest(BaseModel):
    number: int

@app.post("/count")
def count_up(request: CountRequest):
    if request.number < 1:
        raise HTTPException(status_code=400, detail="Number must be >= 1")

    result = "".join(str(i) for i in range(1, request.number + 1))
    print(result)
    return {"result": result}
