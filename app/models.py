from pydantic import BaseModel, EmailStr


class Submission(BaseModel):
    """Base model for submission data."""
    
    name: str
    email: EmailStr
    message: str
