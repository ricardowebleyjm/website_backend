from fastapi import FastAPI

app = FastAPI()
origins = ["https://api.ricardowebley.com",
           "https://ricardowebley.com",
        ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}