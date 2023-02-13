from supabase import create_client, Client

url = "https://mpriiaoimjjntvehtvsd.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1wcmlpYW9pbWpqbnR2ZWh0dnNkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY3NjI2Mzc5NywiZXhwIjoxOTkxODM5Nzk3fQ.JwD3VHCjsZwYSpQ1yDpD0-hTXeNiBef0vIzpMZrF_0E"
supabase: Client = create_client(url, key)
data = supabase.auth.sign_in_with_password({"email": "rajendrarajaramv@gmail.com", "password": "Zxasqw12!"})
print(data)
