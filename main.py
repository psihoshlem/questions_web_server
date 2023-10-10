from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routers import questions_routes


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions_routes.router)

if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True)