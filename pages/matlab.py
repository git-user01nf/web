import flet as ft
import os

# ── YOUR EXACT COLORS ─────────────────────────────────────────────────────────
GLASS_BG = "#C4B8B8"
GLASS_BLUR = ft.Blur(96, 96)
TEXT_PRIMARY = "#69280A"
TEXT_SECONDARY = "#533535"
ACCENT_CYAN = "#3d3d3b"
ACCENT_CORAL = "#350707"
SUCCESS_GLOW = "#0e0494"

# Assets directory
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
CERTIFICATES_DIR = os.path.join(ASSETS_DIR, "certificates")

class MatlabPage:
    def __init__(self):
        self._page = None

    def _show_certificate_dialog(self, file_name, display_name, page):
        """Show a dialog with certificate info and download link"""
        file_path = os.path.join(CERTIFICATES_DIR, file_name)
        
        if os.path.exists(file_path):
            # Create a dialog with a link to view the certificate
            dlg = ft.AlertDialog(
                title=ft.Text("Certificate", color=ACCENT_CYAN, size=18, weight=ft.FontWeight.W_700),
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(display_name, size=16, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
                        ft.Text(f"File: {file_name}", size=12, color=TEXT_SECONDARY),
                        ft.Divider(height=1, color=ACCENT_CYAN),
                        ft.Text("Certificate is available on the server.", size=12, color=ACCENT_CYAN),
                        ft.Icon(ft.Icons.WORKSPACE_PREMIUM, size=60, color=SUCCESS_GLOW),
                    ], spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    width=350,
                    padding=20,
                ),
                actions=[
                    ft.TextButton("Close", on_click=lambda _: setattr(dlg, 'open', False) or page.update()),
                ],
            )
            page.dialog = dlg
            dlg.open = True
            page.update()
        else:
            # File not found dialog
            dlg = ft.AlertDialog(
                title=ft.Text("Certificate Not Found", color=ACCENT_CORAL),
                content=ft.Text(f"File not found: {file_name}\n\nCertificate may not be uploaded yet.", color=TEXT_PRIMARY),
                actions=[ft.TextButton("OK", on_click=lambda _: setattr(dlg, 'open', False) or page.update())],
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

    def _build_certificate_card(self, file_name, display_name, phase_name, course_id):
        accent_color = ACCENT_CYAN
        icon = ft.Icons.IMAGE
        action_text = "VIEW CERTIFICATE"
        media_type = "CERTIFICATE"
        
        # Preview container
        preview_container = ft.Container(
            content=ft.Column([
                ft.Icon(icon, size=48, color=accent_color),
                ft.Text(media_type, size=12, color=accent_color, weight=ft.FontWeight.W_600),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
            width=300,
            height=180,
            bgcolor=ft.Colors.with_opacity(0.15, accent_color),
            border_radius=16,
        )
        
        # Load image preview if it's an image file
        file_path = os.path.join(CERTIFICATES_DIR, file_name)
        if os.path.exists(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                preview_container = ft.Image(src=file_path, width=300, height=180, fit="contain", border_radius=16)
            except:
                pass
        
        def on_click(e):
            self._show_certificate_dialog(file_name, display_name, e.page)
        
        # Build card content with CENTERED text
        card_content = ft.Column([
            preview_container,
            ft.Container(
                content=ft.Text(display_name, size=14, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY, text_align=ft.TextAlign.CENTER),
                width=280,
            ),
            ft.Container(
                content=ft.Text(phase_name, size=11, color=ACCENT_CYAN, text_align=ft.TextAlign.CENTER),
                width=280,
            ),
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.VERIFIED, size=14, color=SUCCESS_GLOW),
                    ft.Text(action_text, size=11, color=accent_color, weight=ft.FontWeight.W_600),
                ], spacing=6, alignment=ft.MainAxisAlignment.CENTER),
                bgcolor=ft.Colors.with_opacity(0.15, accent_color),
                border_radius=20,
                padding=ft.Padding(12, 6, 12, 6),
            ),
        ], spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        return ft.Container(
            content=card_content,
            bgcolor=GLASS_BG,
            border_radius=20,
            padding=16,
            border=ft.Border.all(1, ACCENT_CYAN + "66"),
            on_click=on_click,
        )

    def build(self, page=None):
        self._page = page
        
        # Hero section
        hero = ft.Container(
            content=ft.Column([
                ft.Text("▸ MATLAB ACHIEVEMENT HUB ◂", size=22, weight=ft.FontWeight.W_800, color=ACCENT_CYAN, text_align=ft.TextAlign.CENTER),
                ft.Text("MathWorks certified courses · interactive learning", size=14, color=TEXT_SECONDARY, text_align=ft.TextAlign.CENTER),
                ft.Container(width=60, height=3, bgcolor=ACCENT_CYAN, margin=ft.Margin(0, 12, 0, 0)),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
            margin=ft.Margin(0, 0, 0, 24),
        )
        
        # 8 courses (8/8 completed)
        certificate_files = [
            ("MATLAB Onramp.png", "MATLAB Onramp", "Core MATLAB syntax & commands", "01"),
            ("Calculations with Vectors and Matrices.png", "Calculations with Vectors and Matrices", "Vector operations & matrix math", "02"),
            ("Make and Manipulate Matrices.png", "Make and Manipulate Matrices", "Matrix creation & manipulation", "03"),
            ("Explore Data with MATLAB Plots.png", "Explore Data with MATLAB Plots", "Data visualization & plotting", "04"),
            ("Introduction to Solving Ordinary Differential Equations.png", "Introduction to Solving ODEs", "ODE solving techniques", "05"),
            ("Wireless Communications Onramp.png", "Wireless Communications Onramp", "Wireless systems & protocols", "06"),
            ("Simulink Onramp course.png", "Simulink Onramp", "System modeling & simulation", "07"),
            ("Wireless Communications Onramp.png", "Advanced MATLAB Programming", "Performance optimization & advanced techniques", "08"),
        ]
        
        # Progress value 8/8 = 1.0 (100%)
        progress_ring = ft.ProgressRing(value=1.0, stroke_width=6, color=SUCCESS_GLOW, bgcolor=ACCENT_CYAN + "44", width=80, height=80)
        
        progress_section = ft.Container(
            content=ft.Row([
                progress_ring,
                ft.Column([
                    ft.Text("ACHIEVEMENT MATRIX", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRIMARY),
                    ft.Text("8/8 courses completed", size=12, color=SUCCESS_GLOW),
                    ft.Text("MathWorks Learning Center", size=11, color=TEXT_SECONDARY),
                ], spacing=4),
            ], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
            margin=ft.Margin(0, 0, 0, 24),
        )
        
        # Certificate grid
        certificates_grid = ft.GridView(expand=True, max_extent=340, child_aspect_ratio=1.1, spacing=20, run_spacing=20)
        
        # Populate certificates grid (8 courses)
        for file_name, display_name, phase_name, course_id in certificate_files:
            card = self._build_certificate_card(file_name, display_name, phase_name, course_id)
            certificates_grid.controls.append(card)
        
        return ft.Column(
            [hero, progress_section, certificates_grid],
            spacing=20,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        )
