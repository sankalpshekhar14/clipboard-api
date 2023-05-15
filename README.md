# Setup Instructions

```
pip install -r requirements.txt

```

## To Run

```
uvicorn app.main:app --reload
```

## Test

To create a note, make a POST request to ```http://localhost:8000/api/notes```
with a JSON payload.

Sample Payload: 

```json
{
    "testKey": "testValue"
}
```

To retrieve a note, make a GET request to ```http://localhost:8000/api/notes/{uri}``` where the uri is the 6-digit code of the note you want to retrieve.

Example:

```
http://localhost:8000/api/notes/AbcDeF
```