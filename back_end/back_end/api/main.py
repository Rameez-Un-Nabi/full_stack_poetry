from fastapi import FastAPI # import: ignore
from fastapi.middleware.cors import CORSMiddleware # import:ignore

app = FastAPI()

# define CORS origins
origins=["http://localhost:3000", "localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# get request
@app.get("/", tags=["root"])
async def read_root()->dict:
    return {"message": "Welcome to your todo list."}
