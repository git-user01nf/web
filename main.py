import flet as ft
from pages.timeline import TimelinePage
from pages.matlab import MatlabPage
from pages.blog import BlogPage
from pages.github import GithubPage
import time

# ── DARKER COLOUR SCHEME (deep space, no white cast) ─────────────────────────
BG_GRADIENT = ft.RadialGradient(
    center=ft.Alignment(0.5, 0.5),
    radius=0.8,
    colors=["#050a15", "#0a0f1a", "#0d1220"],
    stops=[0.0, 0.5, 1.0],
)
GLASS_BG = "#D2D6E7"
GLASS_BLUR = ft.Blur(95, 95)
ACCENT_CYAN = "#00e5ff"
ACCENT_CORAL = "#ff6b6b"
ACCENT_GOLD = "#775700"
TEXT_PRIMARY = "#3f0303"
TEXT_SECONDARY = "#00103b"
SUCCESS_GLOW = "#00ffaa"
ACTIVE_GLOW = "#925000"

def main(page: ft.Page):
    page.title = "NeoCodex Portfolio 2026"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.bgcolor = "transparent"
    page.scroll = ft.ScrollMode.AUTO

    # Static gradient (no animation thread for web compatibility)
    bg_container = ft.Container(expand=True, gradient=BG_GRADIENT)

    # Pages
    timeline_page = TimelinePage()
    matlab_page = MatlabPage()
    blog_page = BlogPage()
    github_page = GithubPage()

    # Content container
    content_container = ft.Container(
        expand=True,
        opacity=1,
        animate_opacity=300,
        padding=ft.Padding(30, 24, 30, 40),
        content=timeline_page.build(),
        bgcolor=GLASS_BG,
        blur=GLASS_BLUR,
        border_radius=28,
        margin=ft.Margin(20, 0, 20, 20),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.3, ACCENT_CYAN)),
    )

    # Navigation
    current_index = {"v": 0}
    nav_buttons = []
    nav_labels = ["TIMELINE", "MATRIX LAB", "BLOG", "GITHUB"]
    nav_icons = [ft.Icons.TIMELINE, ft.Icons.SCIENCE, ft.Icons.ARTICLE, ft.Icons.CODE]

    def rebuild_nav():
        for i, btn in enumerate(nav_buttons):
            active = (i == current_index["v"])
            row = btn.content
            icon = row.controls[0]
            text = row.controls[1]
            if active:
                icon.color = ACCENT_CYAN
                text.color = ACCENT_CYAN
                btn.bgcolor = ft.Colors.with_opacity(0.3, ACCENT_CYAN)
                btn.border = ft.Border.all(1, ACCENT_CYAN)
            else:
                icon.color = TEXT_SECONDARY
                text.color = TEXT_SECONDARY
                btn.bgcolor = ft.Colors.with_opacity(0.15, ft.Colors.WHITE)
                btn.border = ft.Border.all(1, ft.Colors.with_opacity(0.3, ft.Colors.WHITE))
            btn.update()

    def switch_page(idx):
        if idx == current_index["v"]:
            return
        content_container.opacity = 0
        page.update()
        time.sleep(0.2)
        current_index["v"] = idx
        rebuild_nav()
        if idx == 0:
            content_container.content = timeline_page.build()
        elif idx == 1:
            content_container.content = matlab_page.build(page)
        elif idx == 2:
            content_container.content = blog_page.build(page)
        elif idx == 3:
            content_container.content = github_page.build()
        content_container.opacity = 1
        page.update()

    for i, (label, icon) in enumerate(zip(nav_labels, nav_icons)):
        btn = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icon, size=18, color=TEXT_SECONDARY),
                    ft.Text(label, size=12, weight=ft.FontWeight.W_600, color=TEXT_SECONDARY),
                ],
                spacing=8,
            ),
            padding=ft.Padding(18, 12, 18, 12),
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.3, ft.Colors.WHITE)),
            on_click=lambda e, idx=i: switch_page(idx),
            ink=True,
        )
        nav_buttons.append(btn)

    navbar = ft.Container(
        content=ft.Row(nav_buttons, spacing=12, alignment=ft.MainAxisAlignment.CENTER),
        bgcolor=ft.Colors.with_opacity(0.5, "#050a15"),
        border_radius=60,
        padding=ft.Padding(8, 8, 8, 8),
        margin=ft.Margin(20, 16, 20, 16),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.5, ACCENT_CYAN)),
        blur=ft.Blur(6, 6),
    )

    # User Info (Top-Right Corner)
    user_info = ft.Container(
        content=ft.Column([
            ft.Text("FULAYI MATHEWS WAQAS", size=16, weight=ft.FontWeight.W_700, color=ACCENT_CYAN, text_align=ft.TextAlign.RIGHT),
            ft.Text("STUDENT NO: 224122754", size=12, color=TEXT_SECONDARY, text_align=ft.TextAlign.RIGHT),
        ], spacing=2, horizontal_alignment=ft.CrossAxisAlignment.END),
        bgcolor=GLASS_BG,
        padding=ft.Padding(15, 8, 15, 8),
        border_radius=20,
        border=ft.Border.all(1, ft.Colors.with_opacity(0.5, ACCENT_CYAN)),
        margin=ft.Margin(0, 20, 30, 0),
    )
    
    # Hero header with user info on the right
    centered_content = ft.Column(
        controls=[
            ft.Row([
                ft.Text("⚡ NEO·CODEX ⚡", size=12, weight=ft.FontWeight.W_700, color=ACCENT_CYAN),
                ft.Container(
                    content=ft.Text("Project Manager · Documentation Lead", size=9, color=SUCCESS_GLOW), 
                    bgcolor="#250008FF",
                    padding=ft.Padding(8, 4, 8, 4),
                    border_radius=12,
                ),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=12),
            ft.Text("PORTFOLIO 2026", size=56, weight=ft.FontWeight.W_900, color=TEXT_PRIMARY),
            ft.Text("individual contribution system · civil engineering · fix‑flow", size=14, color=TEXT_SECONDARY),
            ft.Container(width=80, height=2, bgcolor=ACCENT_CYAN, margin=ft.Margin(0, 12, 0, 0)),
        ],
        spacing=6,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
    header_content = ft.Row(
        controls=[
            centered_content,
            user_info,
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    header = ft.Container(
        content=header_content,
        padding=ft.Padding(30, 48, 30, 24),
    )

    page.add(
        ft.Stack(
            controls=[
                bg_container,
                ft.Column(
                    controls=[header, navbar, content_container],
                    spacing=0,
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            expand=True,
        )
    )
    page.update()

# This is the critical line for Fly.io - must bind to 0.0.0.0
if __name__ == "__main__":
    ft.app(target=main, host="0.0.0.0", port=8000)