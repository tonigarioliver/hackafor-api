from fastapi import FastAPI
from routes.products import products_router
from starlette.responses import RedirectResponse
import uvicorn
import os


app = FastAPI()

app.include_router(products_router)


@app.get("/")
def index() -> RedirectResponse:
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")