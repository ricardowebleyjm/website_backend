from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import csv
import os
from configparser import RawConfigParser
from pathlib import Path
from .models import Submission



config = RawConfigParser()
config.read("config/settings.ini")
origins = config.get('secrets', 'ALLOWED_ORIGINS').split(',')

DEBUG = config.getboolean('secrets', 'DEBUG')
if DEBUG:
    app = FastAPI()
else:
    app = FastAPI(title="My Awesome API", debug=False,docs_url=None, redoc_url=None,)
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

csv_file_path = Path("submissions.csv")
if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Message"])  # Write header
        
        
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/submit/")
async def submit_data(submission: Submission):
    print(submission)
    """
    Endpoint to accept data from frontend and save it to a CSV file using a model.
    """
    csv_file_path = "submissions.csv"
    try:
        # Save the submission data to the CSV file
        with open(csv_file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([submission.name, submission.email, submission.message])
        return {"message": "Thank you for Reaching out. I will get back to you soon."}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Failed to save data: {str(e)}")