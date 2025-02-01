from fastapi import Header, HTTPException

def process_api_key(api_key: str, valid_key: str):
    """
    Process the API key to check if it is valid.
    """
    if api_key != valid_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
        return False
    return True