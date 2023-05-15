from app.util.clipboard_util import generate_uri
import sqlite3
import base64
import json

class ClipboardService:
    def __init__(self):
        self.conn = sqlite3.connect('clipboard.db', check_same_thread=False)
        #self.conn.execute("DROP TABLE NOTES")
        self.conn.execute('''CREATE TABLE IF NOT EXISTS NOTES
            (ID INT PRIMARY KEY,
            URI VARCHAR(10) NOT NULL,
            DATA TEXT NOT NULL
            );'''
        )
    
    def get_notes_by_uri(self, uri):
        """
        Fetches notes based on the unique uri
        """
        cursor = self.conn.execute(f"SELECT DATA from NOTES WHERE URI='{uri}'")
        row = cursor.fetchone()
        print(row)
        if row is None:
            return None
        encoded_string = row[0]
        base64_bytes = encoded_string.encode("UTF-8")
  
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode("ascii")
        return {
            "uri": uri,
            "data": json.loads(decoded_string)
        }

    def insert_note(self, data, uri):
        json_string = json.dumps(data)
        encoded = base64.b64encode(json_string.encode('utf-8'))
        encoded_string = encoded.decode('utf-8') 
        query = f"INSERT INTO NOTES (URI, DATA) values ('{uri}', '{encoded_string}')"
        print(query)
        self.conn.execute(query)
        self.conn.commit()

    def create_note(self, data):
        """
        Creates a note entry and returns a response containing the unique id
        """
        uri = generate_uri()
        # check if uri is already used by a file
        notes = self.get_notes_by_uri(uri)
        if notes is not None:
            uri = generate_uri()
        
        #insert the note
        self.insert_note(data, uri)
        return {"status": True, "uri": uri}
