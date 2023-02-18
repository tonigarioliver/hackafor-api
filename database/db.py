import os
from dotenv import load_dotenv
from supabase import Client
from supabase import create_client


load_dotenv()


#URL: str = os.environ.get("SUPABASE_URL")
#KEY: str = os.environ.get("SUPABASE_KEY")

URL: str = "https://aoombgglyswwhkqniife.supabase.co"
KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFvb21iZ2dseXN3d2hrcW5paWZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzY0MDE0NjksImV4cCI6MTk5MTk3NzQ2OX0.g_qldX2hxVzPkcXbBAUf5MW-qEnnOU6M4YuL4TWPpr8"

class DB:

    supabase: Client

    def __init__(self) -> None:
        self.supabase = create_client(URL, KEY)