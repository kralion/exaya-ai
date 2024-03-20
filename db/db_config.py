
import os
from supabase import create_client, Client

url: str = os.environ.get("https://xcglzhfdjsvxdncwhdln.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhjZ2x6aGZkanN2eGRuY3doZGxuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTA3ODgzMDEsImV4cCI6MjAyNjM2NDMwMX0.FsIJqrgaTy5B1ifm1T-QA1JwZQ-4xePkp8qyysSiAW8")
supabase: Client = create_client(url, key)