from fastapi import FastAPI, Request
from app.service.clipboard_service import ClipboardService
from fastapi import HTTPException, status
app = FastAPI()
service = ClipboardService()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/notes/{uri}")
def get_note(uri):
    """
    Retrieve the note via the URI.
    """
    print(uri)
    resp = service.get_notes_by_uri(uri)
    return resp
    

@app.post("/api/notes")
def create_note(data: dict):
    """
    Creates a note.
    """
    # try:
    response = service.create_note(data)
    return response
    # except Exception as e:
    #     print(e)
    #     raise HTTPException(
    #         status_code = 500,
    #         detail="Unable to create Note"
    #     )

