import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/addition/")
def addition(a: int = 0, b: int = 0):
    return {"result": a+b}

@app.get("/subtraction/")
def subtraction(a: int = 0, b: int = 0):
    return {"result": a-b}

@app.get("/multiplication/")
def multiplication(a: int = 0, b: int = 0):
    return {"result": a*b}

@app.get("/division/")
def division(a: int = 0, b: int = 0):
    if b == 0:
        raise HTTPException(status_code=400, detail="На ноль делить нельзя")
    return {"result": a/b}

@app.get("/calculate_expression")
def calculate_expression(expr: str):
    allowed_chars = "0123456789+-*/(). "
    
    for ch in expr:
        if ch not in allowed_chars:
            raise HTTPException(status_code=400, detail="Есть неразрешенные символы")
    try:
        result = eval(expr)
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="На ноль делить нельзя")
    except Exception:
        raise HTTPException(status_code=400, detail="Ошибка синтаксиса")
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload = True,
    )

