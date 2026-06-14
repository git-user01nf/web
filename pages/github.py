import flet as ft
import webbrowser

# ── GLASS DARK THEME ─────────────────────────────────────────────────────────
GLASS_BG = "#0a0f1a"
GLASS_BLUR = ft.Blur(12, 12)
TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#a0b0d0"
ACCENT_CYAN = "#00e5ff"
ACCENT_CORAL = "#ff6b6b"
ACCENT_GOLD = "#ffcc44"
SUCCESS_GLOW = "#00ffaa"

# ── PROJECT LINKS (using only standard icons that exist in all Flet versions) ──
LINKS = {
    "GitHub Repository": {
        "url": "https://github.com/git-user01nf/UNAM-I3691CP-WaterLeak-Ongwediva",
        "icon": ft.Icons.CODE,
        "color": "#6e44ff"
    },
    "GitHub Actions (Builds)": {
        "url": "https://github.com/git-user01nf/UNAM-I3691CP-WaterLeak-Ongwediva/actions",
        "icon": ft.Icons.BUILD,
        "color": "#00e5ff"
    },
    "Figma Designs": {
        "url": "https://www.figma.com/make/hKeuoG4pWZ4VkaiO3AKRyI/fix-flow-app-designs",
        "icon": ft.Icons.DRAW,
        "color": "#ff44cc"
    },
    "Firebase Console": {
        "url": "https://console.firebase.google.com/project/civi-fix13",
        "icon": ft.Icons.SETTINGS,
        "color": "#ffaa44"
    },
    "Firestore Database": {
        "url": "https://console.firebase.google.com/project/civi-fix13/firestore/data",
        "icon": ft.Icons.LIST,
        "color": "#00ffaa"
    },
    "Cloudinary Console": {
        "url": "https://cloudinary.com/console",
        "icon": ft.Icons.CLOUD,
        "color": "#00e5ff"
    },
}

class GithubPage:
    COMMITS = [
        {"hash": "a3f9c12", "msg": "docs: initial SRS structure & team roles", "date": "28 Mar 2126"},
        {"hash": "b72e4d8", "msg": "feat: add Firestore data model (users, reports)", "date": "5 Apr 2126"},
        {"hash": "c1a8f53", "msg": "docs: complete SRS with requirements and use cases", "date": "25 Apr 2126"},
        {"hash": "d90b217", "msg": "design: export Figma screens to /designs", "date": "30 May 2126"},
        {"hash": "e5c3a91", "msg": "docs: write design rationale", "date": "1 Jun 2126"},
        {"hash": "f84d632", "msg": "docs: final user manual & group declaration", "date": "12 Jun 2126"},
    ]

    PULL_REQUESTS = [
        {"num": 8, "title": "Initial SRS submission", "status": "merged", "reviews": 2},
        {"num": 14, "title": "Figma export and design rationale", "status": "merged", "reviews": 1},
        {"num": 22, "title": "User manual & final docs", "status": "merged", "reviews": 2},
    ]

    def _open_link(self, url, page):
        webbrowser.open(url)

    def _build_link_card(self, title, link_data):
        """Build a futuristic glass card for each project link"""
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(link_data["icon"], size=28, color=link_data["color"]),
                    ft.Text(title, size=16, weight=ft.FontWeight.W_700, color=TEXT_PRIMARY, expand=True),
                ], spacing=12),
                ft.Text(link_data["url"], size=11, color=TEXT_SECONDARY, selectable=True),
                ft.Container(
                    content=ft.Text("🔗 OPEN →", size=12, color=link_data["color"], weight=ft.FontWeight.W_600),
                    margin=ft.Margin(0, 8, 0, 0),
                ),
            ], spacing=8),
            bgcolor=GLASS_BG,
            blur=GLASS_BLUR,
            border_radius=20,
            padding=16,
            border=ft.Border.all(1, ft.Colors.with_opacity(0.3, link_data["color"])),
            on_click=lambda e, url=link_data["url"]: self._open_link(url, e.page),
        )

    def build(self):
        # Stats row
        stats = ft.Row([
            ft.Container(
                content=ft.Column([
                    ft.Text("6", size=36, weight=ft.FontWeight.W_800, color=ACCENT_CYAN),
                    ft.Text("COMMITS", size=11, color=TEXT_SECONDARY, weight=ft.FontWeight.W_600),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=GLASS_BG, blur=GLASS_BLUR, border_radius=20, padding=16, expand=True,
                border=ft.Border.all(1, ACCENT_CYAN + "44"),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("3", size=36, weight=ft.FontWeight.W_800, color=ACCENT_CYAN),
                    ft.Text("PRs", size=11, color=TEXT_SECONDARY, weight=ft.FontWeight.W_600),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=GLASS_BG, blur=GLASS_BLUR, border_radius=20, padding=16, expand=True,
                border=ft.Border.all(1, ACCENT_CYAN + "44"),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("5", size=36, weight=ft.FontWeight.W_800, color=ACCENT_CYAN),
                    ft.Text("REVIEWS", size=11, color=TEXT_SECONDARY, weight=ft.FontWeight.W_600),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=GLASS_BG, blur=GLASS_BLUR, border_radius=20, padding=16, expand=True,
                border=ft.Border.all(1, ACCENT_CYAN + "44"),
            ),
        ], spacing=16)

        # Links section header
        links_header = ft.Row([
            ft.Icon(ft.Icons.LINK, size=20, color=ACCENT_GOLD),
            ft.Text("PROJECT RESOURCES", size=16, weight=ft.FontWeight.W_700, color=ACCENT_GOLD),
            ft.Icon(ft.Icons.LINK, size=20, color=ACCENT_GOLD),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=8)

        # Links grid
        links_grid = ft.GridView(expand=True, max_extent=300, child_aspect_ratio=1.3, spacing=16, run_spacing=16)
        for title, link_data in LINKS.items():
            links_grid.controls.append(self._build_link_card(title, link_data))

        links_section = ft.Container(
            content=ft.Column([links_header, links_grid], spacing=16),
            margin=ft.Margin(0, 0, 0, 20),
        )

        # Commit history
        commit_rows = []
        for c in self.COMMITS:
            commit_rows.append(
                ft.Container(
                    content=ft.Row([
                        ft.Icon(ft.Icons.COMMIT, size=14, color=ACCENT_CYAN),
                        ft.Text(c["hash"], size=12, color=TEXT_SECONDARY, width=80, font_family="monospace"),
                        ft.Text(c["msg"], size=13, color=TEXT_PRIMARY, expand=True),
                        ft.Text(c["date"], size=11, color=TEXT_SECONDARY),
                    ], spacing=10),
                    padding=ft.Padding(12, 10, 12, 10),
                    border=ft.Border(bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.15, ft.Colors.WHITE))),
                )
            )
        
        commits_block = ft.Container(
            content=ft.Column([
                ft.Text("▸ COMMIT LOG", size=14, weight=ft.FontWeight.W_700, color=ACCENT_CYAN),
                ft.Column(commit_rows, spacing=0),
            ], spacing=12),
            bgcolor=GLASS_BG, blur=GLASS_BLUR, border_radius=20, padding=16,
            border=ft.Border.all(1, ACCENT_CYAN + "44"),
        )

        # Pull Requests
        pr_cards = []
        for pr in self.PULL_REQUESTS:
            status_color = SUCCESS_GLOW if pr["status"] == "merged" else ACCENT_CYAN
            pr_cards.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(f"PR #{pr['num']}", size=14, weight=ft.FontWeight.W_700, color=status_color),
                            ft.Text(pr["title"], size=13, color=TEXT_PRIMARY, expand=True),
                            ft.Container(
                                content=ft.Text(pr["status"].upper(), size=9, color=status_color, weight=ft.FontWeight.W_600),
                                bgcolor=status_color + "22",
                                padding=ft.Padding(8, 4, 8, 4),
                                border_radius=12,
                            ),
                        ]),
                        ft.Text(f"👥 {pr['reviews']} review(s)", size=11, color=TEXT_SECONDARY),
                    ], spacing=6),
                    bgcolor=GLASS_BG, blur=GLASS_BLUR, border_radius=16, padding=16, margin=ft.Margin(0, 0, 0, 12),
                    border=ft.Border.all(1, ACCENT_CYAN + "44"),
                )
            )
        
        pr_block = ft.Container(
            content=ft.Column([
                ft.Text("▸ PULL REQUESTS", size=14, weight=ft.FontWeight.W_700, color=ACCENT_CYAN),
                ft.Column(pr_cards, spacing=8),
            ], spacing=12),
            bgcolor=GLASS_BG, blur=GLASS_BLUR, border_radius=20, padding=16,
            border=ft.Border.all(1, ACCENT_CYAN + "44"),
        )

        # Impact summary
        impact = ft.Container(
            content=ft.Column([
                ft.Text("▸ IMPACT SUMMARY", size=14, weight=ft.FontWeight.W_700, color=ACCENT_CYAN),
                ft.Text(
                    "As Project Manager and Documentation Lead, I delivered the 25‑page SRS, coordinated the Figma prototype, "
                    "wrote the 12‑page user manual, and ensured all documentation meets UNAM standards. "
                    "My GitHub history shows 6 documentation commits, 3 merged PRs, and 5 code reviews performed.",
                    size=12, color=TEXT_SECONDARY, selectable=True,
                ),
            ], spacing=12),
            bgcolor=GLASS_BG, blur=GLASS_BLUR, border_radius=20, padding=16,
            border=ft.Border.all(1, ACCENT_CYAN + "44"),
        )

        return ft.Column([stats, links_section, commits_block, pr_block, impact], spacing=20, scroll=ft.ScrollMode.AUTO)