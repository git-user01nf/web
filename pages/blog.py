import flet as ft
import os
import webbrowser

# ── NEW MODERN COLOR SCHEME ──────────────────────────────────────────────────
BG_DARK = "#0a0a0f"
BG_GLASS = "rgba(20, 20, 35, 0.85)"
BLOG_BG = "#1a1a2e"

TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#c0c8e0"
TEXT_MUTED = "#8080a0"

ACCENT_PRIMARY = "#00d4ff"
ACCENT_SECONDARY = "#7c3aed"
ACCENT_SUCCESS = "#10b981"
ACCENT_WARNING = "#f59e0b"
ACCENT_DANGER = "#ef4444"

CARD_BG = "rgba(30, 30, 50, 0.7)"
CARD_BORDER = "#2a2a4a"

# Assets directory
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
SCREENSHOTS_DIR = os.path.join(ASSETS_DIR, "screenshots")

# Google Drive link for video
GOOGLE_DRIVE_LINK = "https://drive.google.com/file/d/1w4bgCcfBxDmOTmyU6mVbLCZeUZJupzhd/view?usp=drivesdk"

class BlogPage:
    def __init__(self):
        self._page = None

    def _open_file(self, file_path, file_name, page):
        if os.path.exists(file_path):
            webbrowser.open(f"file://{file_path}")
        else:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"File not found: {file_name}"), open=True))

    def _open_drive_link(self, page):
        webbrowser.open(GOOGLE_DRIVE_LINK)

    def _build_screenshot_card(self, file_name, display_name):
        file_path = os.path.join(SCREENSHOTS_DIR, file_name)
        is_video = file_name.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.webm'))
        
        if is_video:
            accent_color = ACCENT_DANGER
            icon = ft.Icons.PLAY_CIRCLE_FILLED
            action_text = "PLAY VIDEO"
            media_type = "VIDEO FILE"
        else:
            accent_color = ACCENT_PRIMARY
            icon = ft.Icons.IMAGE
            action_text = "VIEW IMAGE"
            media_type = "IMAGE FILE"
        
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
        if not is_video and os.path.exists(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                preview_container = ft.Image(src=file_path, width=300, height=180, fit="contain", border_radius=16)
            except:
                pass
        
        def on_click(e):
            self._open_file(file_path, file_name, e.page)
        
        # Build card content with CENTERED text
        card_content = ft.Column([
            preview_container,
            ft.Container(
                content=ft.Text(display_name, size=14, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY, text_align=ft.TextAlign.CENTER),
                width=280,
            ),
            ft.Container(
                content=ft.Text(action_text, size=11, color=accent_color, weight=ft.FontWeight.W_600),
                bgcolor=ft.Colors.with_opacity(0.15, accent_color),
                border_radius=20,
                padding=ft.Padding(12, 6, 12, 6),
            ),
        ], spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        return ft.Container(
            content=card_content,
            bgcolor=CARD_BG,
            border_radius=20,
            padding=16,
            border=ft.Border.all(1, CARD_BORDER),
            on_click=on_click,
        )

    def _build_video_card(self):
        """Dedicated video card for Google Drive link"""
        accent_color = ACCENT_DANGER
        
        # Video preview container
        preview_container = ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.PLAY_CIRCLE_FILLED, size=64, color=accent_color),
                ft.Text("CLICK TO WATCH VIDEO", size=14, color=accent_color, weight=ft.FontWeight.W_800, text_align=ft.TextAlign.CENTER),
                ft.Text("Project Demo Video", size=11, color=TEXT_SECONDARY, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=12),
            width=300,
            height=180,
            bgcolor=ft.Colors.with_opacity(0.2, accent_color),
            border_radius=16,
            border=ft.Border.all(2, accent_color),
        )
        
        def on_click(e):
            self._open_drive_link(e.page)
        
        # Build card content
        card_content = ft.Column([
            preview_container,
            ft.Text("📹 Project Demo Video", size=16, weight=ft.FontWeight.W_700, color=ACCENT_PRIMARY, text_align=ft.TextAlign.CENTER),
            ft.Text("Click to watch on Google Drive", size=11, color=TEXT_MUTED, text_align=ft.TextAlign.CENTER),
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.PLAY_ARROW, size=14, color=accent_color),
                    ft.Text("PLAY NOW", size=12, color=accent_color, weight=ft.FontWeight.W_700),
                ], spacing=6, alignment=ft.MainAxisAlignment.CENTER),
                bgcolor=ft.Colors.with_opacity(0.15, accent_color),
                border_radius=20,
                padding=ft.Padding(16, 8, 16, 8),
            ),
        ], spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        return ft.Container(
            content=card_content,
            bgcolor=CARD_BG,
            border_radius=20,
            padding=20,
            border=ft.Border.all(2, accent_color),
            on_click=on_click,
        )

    def _build_blog_card(self, title, date, summary, tags):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(title, size=18, weight=ft.FontWeight.W_700, color=ACCENT_PRIMARY, expand=True, text_align=ft.TextAlign.CENTER),
                    ft.Text(date, size=11, color=TEXT_MUTED),
                ], spacing=8),
                ft.Text(summary, size=13, color=TEXT_SECONDARY, height=50, text_align=ft.TextAlign.CENTER),
                ft.Row(
                    [ft.Container(
                        content=ft.Text(t, size=10, color=ACCENT_SECONDARY, weight=ft.FontWeight.W_500),
                        bgcolor=ft.Colors.with_opacity(0.15, ACCENT_SECONDARY),
                        border_radius=16,
                        padding=ft.Padding(10, 4, 10, 4),
                    ) for t in tags],
                    spacing=8, wrap=True, alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_FORWARD, size=14, color=ACCENT_PRIMARY),
                        ft.Text("READ FULL ARTICLE", size=12, color=ACCENT_PRIMARY, weight=ft.FontWeight.W_600),
                    ], spacing=6, alignment=ft.MainAxisAlignment.CENTER),
                    margin=ft.Margin(0, 12, 0, 0),
                ),
            ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=CARD_BG,
            border_radius=20,
            padding=18,
            border=ft.Border.all(1, CARD_BORDER),
        )

    def build(self, page=None):
        self._page = page
        
        # Hero section
        hero = ft.Container(
            content=ft.Column([
                ft.Text("▸ CONFIDENCE IN CONCEPTS ◂", size=22, weight=ft.FontWeight.W_800, color=ACCENT_PRIMARY, text_align=ft.TextAlign.CENTER),
                ft.Text("technical blog · screenshots · video insights", size=14, color=TEXT_SECONDARY, text_align=ft.TextAlign.CENTER),
                ft.Container(width=60, height=3, bgcolor=ACCENT_PRIMARY, margin=ft.Margin(0, 12, 0, 0)),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
            margin=ft.Margin(0, 0, 0, 24),
        )
        
        # Blog posts section (FIRST)
        blog_grid = ft.GridView(expand=True, max_extent=360, child_aspect_ratio=1.2, spacing=20, run_spacing=20)
        
        blog_posts = [
            ("SRS – 25 Pages of Engineering Logic", "25.04.2126", 
             "How I structured functional requirements, Firebase collections, and use case diagrams.",
             ["#documentation", "#srs", "#planning"]),
            ("Figma Prototyping in Hyperspeed", "30.05.2126", 
             "Coordinated 8‑screen prototype, design rationale, and export for GitHub.",
             ["#figma", "#ui/ux", "#designsystem"]),
            ("GitHub Pull Request Workflow", "10.06.2126", 
             "How we enforced code reviews and branch protection.",
             ["#git", "#collaboration", "#codequality"]),
            ("Final Presentation – Live Demo", "13.06.2126", 
             "Prepared the live demo script, user manual, and final APK submission.",
             ["#presentation", "#deployment", "#leadership"]),
            ("Firebase Data Model Design", "15.04.2126", 
             "Designing Firestore collections for users, reports, likes, and comments.",
             ["#firebase", "#database", "#backend"]),
            ("VS Code Development Environment", "10.03.2126", 
             "Setting up the development environment with VS Code and ESLint.",
             ["#vscode", "#tools", "#development"]),
        ]
        
        for title, date, summary, tags in blog_posts:
            blog_grid.controls.append(self._build_blog_card(title, date, summary, tags))
        
        blog_section = ft.Column([
            ft.Text("📝 BLOG POSTS", size=18, weight=ft.FontWeight.W_700, color=ACCENT_SECONDARY, text_align=ft.TextAlign.CENTER),
            ft.Text("Click any card to read the full article", size=12, color=TEXT_MUTED, text_align=ft.TextAlign.CENTER),
            blog_grid,
        ], spacing=16, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        # Screenshots section (SECOND)
        screenshots_grid = ft.GridView(expand=True, max_extent=340, child_aspect_ratio=1.1, spacing=20, run_spacing=20)
        
        screenshot_files = [
            ("commits history 2.png", "📊 GitHub Commits - Part 2"),
            ("commits history.png", "📈 GitHub Commits History"),
            ("commits.png", "💾 Commit Records"),
            ("committed files.png", "📁 Committed Files"),
            ("firebase management 1.jpg", "🔥 Firebase Setup - Part 1"),
            ("firebase management 2.jpg", "🔥 Firebase Setup - Part 2"),
            ("Vs code coding.png", "💻 VS Code Development"),
            ("vscode coding.png", "⌨️ Coding Workspace"),
        ]
        
        for file_name, display_name in screenshot_files:
            card = self._build_screenshot_card(file_name, display_name)
            screenshots_grid.controls.append(card)
        
        screenshots_section = ft.Column([
            ft.Text("📸 SCREENSHOTS & MEDIA", size=18, weight=ft.FontWeight.W_700, color=ACCENT_PRIMARY, text_align=ft.TextAlign.CENTER),
            ft.Text("Click any card to view image", size=12, color=TEXT_MUTED, text_align=ft.TextAlign.CENTER),
            screenshots_grid,
        ], spacing=16, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        # Video section (THIRD/LAST)
        video_section = ft.Column([
            ft.Text("🎬 PROJECT DEMO VIDEO", size=18, weight=ft.FontWeight.W_700, color=ACCENT_DANGER, text_align=ft.TextAlign.CENTER),
            ft.Text("Click the card below to watch the project demonstration", size=12, color=TEXT_MUTED, text_align=ft.TextAlign.CENTER),
            ft.Container(content=self._build_video_card()),
        ], spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        # Create containers for each section
        blog_container_obj = ft.Container(content=blog_section, visible=True, expand=True)
        screenshots_container_obj = ft.Container(content=screenshots_section, visible=False, expand=True)
        video_container_obj = ft.Container(content=video_section, visible=False, expand=True)
        
        # Create toggle buttons (BLOG first, then SCREENSHOTS, then VIDEO last)
        blog_btn = ft.ElevatedButton(
            content=ft.Text("📝 BLOG POSTS", size=13, color=ACCENT_SECONDARY, weight=ft.FontWeight.W_600),
            on_click=lambda e: toggle_view("blog"),
            bgcolor=ft.Colors.with_opacity(0.15, ACCENT_SECONDARY),
        )
        screenshots_btn = ft.ElevatedButton(
            content=ft.Text("📸 SCREENSHOTS", size=13, color=ACCENT_PRIMARY, weight=ft.FontWeight.W_600),
            on_click=lambda e: toggle_view("screenshots"),
            bgcolor=ft.Colors.with_opacity(0.1, ACCENT_PRIMARY),
        )
        video_btn = ft.ElevatedButton(
            content=ft.Text("🎬 VIDEO", size=13, color=ACCENT_DANGER, weight=ft.FontWeight.W_600),
            on_click=lambda e: toggle_view("video"),
            bgcolor=ft.Colors.with_opacity(0.15, ACCENT_DANGER),
        )
        
        toggle_buttons = ft.Row(
            [blog_btn, screenshots_btn, video_btn],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        )
        
        def toggle_view(view):
            blog_container_obj.visible = (view == "blog")
            screenshots_container_obj.visible = (view == "screenshots")
            video_container_obj.visible = (view == "video")
            page.update()
        
        content_stack = ft.Column(
            controls=[blog_container_obj, screenshots_container_obj, video_container_obj],
            expand=True,
        )
        
        return ft.Column(
            [hero, toggle_buttons, ft.Divider(height=20, color="transparent"), content_stack],
            spacing=20,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        )