import flet as ft
import os
from main import main as app_main

if __name__ == "__main__":
    # Fly.io tells the app which port to use via the PORT environment variable.
    # If not found, it defaults to 8080.
    port = int(os.getenv("PORT", 8080))
    
    print(f"--- STARTING SYSTEM ON PORT {port} ---")
    
    ft.app(
        target=app_main,
        host="0.0.0.0",   # MANDATORY: Allows external traffic
        port=port,        # MANDATORY: Must match fly.toml internal_port
        assets_dir="assets",
        view=None         # MANDATORY: Ensures it runs as a web server only
    )