from typing import Optional
from supabase import create_client, Client
from app.core.config import settings

_supabase_admin_client: Optional[Client] = None

def get_supabase_client() -> Client:
    """
    Returns the singleton administrative Supabase client configured with the server-side SUPABASE_KEY.
    """
    global _supabase_admin_client
    if _supabase_admin_client is None:
        if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
            raise RuntimeError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables.")
        _supabase_admin_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    return _supabase_admin_client

def get_user_supabase_client(access_token: str) -> Client:
    """
    Returns a Supabase client authenticated on behalf of a specific user token for RLS compliance.
    """
    client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    client.postgrest.auth(access_token)
    return client

# Maintain backwards compatibility with existing app/supabase.py
supabase = get_supabase_client()
