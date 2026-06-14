import flet as ft
import os
import sys

# Add the current directory to path to ensure 'pages' can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from main import main as app_main
    print("Successfully imported main app logic.")
except ImportError as e:
    print(f"IMPORT ERROR: {e}")
    # Fallback to a simple text if main fails to load
    def app_main(page: ft.Page):
        page.add(ft.Text(f"Critical Load Error: {e}"))

if __name__ == "__main__":
    # Fly.io tells the app which port to use via the PORT environment variable
    port = int(os.getenv("PORT", 8080))
    
    print(f"Starting Flet server on port {port}...")
    
    ft.app(
        target=app_main,
        host="0.0.0.0",  # MUST be 0.0.0.0 for Fly.io
        port=port,
        view=None,       # None is correct for server-side hosting
        assets_dir="assets"
    )