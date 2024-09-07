from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/calculate")
def calculate(operation: str, operand1: float, operand2: float):
    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    elif operation == "*":
        result = operand1 * operand2
    elif operation == "/":
        if operand2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = operand1 / operand2
    elif operation == "%":
        if operand2 == 0:
            raise HTTPException(status_code=400, detail="Modulo by zero is not allowed")
        result = operand1 % operand2
    else:
        raise HTTPException(status_code=400, detail="Unsupported operation")

    return {"operation": operation, "operand1": operand1, "operand2": operand2, "result": result}
