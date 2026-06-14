import flet as ft

# ── BETTER VISIBILITY ─────────────────────────────────────────────────────────
GLASS_BG = "#E2E7FD"
GLASS_BLUR = ft.Blur(80, 80)
TEXT_PRIMARY = "#4E0D0D"
TEXT_SECONDARY = "#000000"
ACCENT_CYAN = "#273AE9"
SUCCESS_GLOW = "#00009C"
ACTIVE_GLOW = "#b6c02b"

class TimelinePage:
    ENTRIES = [
        {"week": "WEEK 01-02", "date": "02‑13 Mar", "task": "PHASE 0: SETUP", 
         "contribution": "GitHub repo creation, team onboarding, Expo environment check", 
         "hash": "repo-init", "details": "Created public repository, invited 15 members, verified Expo Go on all devices.", 
         "status": "done"},
        {"week": "WEEK 03-04", "date": "16‑27 Mar", "task": "PHASE 1: PITCH", 
         "contribution": "Co‑prepared presentation & registered Fix‑Flow idea", 
         "hash": "pitch-ok", "details": "Presented 3 ideas; Mr. Abisai approved civil engineering infrastructure reporter.", 
         "status": "done"},
        {"week": "WEEK 05-08", "date": "30 Mar‑25 Apr", "task": "PHASE 2: SRS", 
         "contribution": "Authored main SRS sections + Firestore data model", 
         "hash": "srs-final", "details": "Wrote 25‑page SRS, defined collections (users, reports, likes, comments).", 
         "status": "done"},
        {"week": "WEEK 09-12", "date": "27 Apr‑30 May", "task": "PHASE 3: FIGMA", 
         "contribution": "Coordinated UI/UX team & delivered design rationale", 
         "hash": "figma-proto", "details": "Built 8‑screen prototype, ensured mobile‑first layout, submitted design rationale.", 
         "status": "done"},
        {"week": "WEEK 13", "date": "01‑06 Jun", "task": "PHASE 4A: PROGRESS DEMO", 
         "contribution": "Prepared live demo script & documentation", 
         "hash": "demo-live", "details": "Demonstrated authentication, report creation, admin panel to Mr. Abisai.", 
         "status": "done"},
        {"week": "WEEK 14", "date": "08‑13 Jun", "task": "PHASE 4B: FINAL", 
         "contribution": "User manual, final SRS, group declaration, APK build", 
         "hash": "final-submit", "details": "Wrote 12‑page user manual, updated SRS, submitted APK via EAS Build.", 
         "status": "active"},
    ]

    def __init__(self):
        self.expanded_states = {}

    def _toggle_details(self, details_col, expand_btn):
        details_col.visible = not details_col.visible
        expand_btn.content.value = "▲ HIDE DETAILS" if details_col.visible else "▼ VIEW DETAILS"
        expand_btn.update()

    def _build_entry(self, entry, is_last):
        status_color = SUCCESS_GLOW if entry["status"] == "done" else ACTIVE_GLOW
        
        node = ft.Container(
            width=48, height=48,
            bgcolor=GLASS_BG,
            border_radius=24,
            border=ft.Border.all(2, status_color),
            content=ft.Text(entry["week"][-2:], size=14, weight=ft.FontWeight.W_800,
                            color=status_color, text_align=ft.TextAlign.CENTER),
            alignment=ft.Alignment(0.5, 0.5),
            shadow=ft.BoxShadow(blur_radius=8, color=status_color + "66"),
        )
        
        details_col = ft.Column(
            controls=[ft.Text(entry["details"], size=12, color=TEXT_SECONDARY)],
            visible=False,
            spacing=8,
        )
        
        expand_btn = ft.TextButton(
            content=ft.Text("▼ VIEW DETAILS", size=10, color=ACCENT_CYAN),
        )
        expand_btn.on_click = lambda e: self._toggle_details(details_col, expand_btn)
        
        card = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(entry["task"], size=16, weight=ft.FontWeight.W_700, color=TEXT_PRIMARY),
                    ft.Container(
                        content=ft.Text("✓" if entry["status"] == "done" else "◉", 
                                       size=12, color=status_color),
                        bgcolor=status_color + "22",
                        padding=ft.Padding(8, 4, 8, 4),
                        border_radius=12,
                    ),
                ]),
                ft.Text(entry["contribution"], size=13, color=TEXT_SECONDARY),
                ft.Row([
                    ft.Text(entry["date"], size=11, color=TEXT_SECONDARY),
                    ft.Text("🔗", size=10, color=status_color),
                    ft.Text(entry["hash"], size=10, color=status_color),
                ], spacing=6),
                details_col,
                expand_btn,
            ], spacing=8),
            bgcolor=GLASS_BG,
            blur=GLASS_BLUR,
            border_radius=20,
            padding=16,
            expand=True,
            shadow=ft.BoxShadow(blur_radius=4, color=ft.Colors.BLACK26),
        )
        
        connector = ft.Container(
            width=2, height=40,
            bgcolor=status_color if not is_last else "transparent",
            margin=ft.Margin(23, 0, 0, 0)
        )
        
        return ft.Row([
            ft.Column([node] + ([connector] if not is_last else []), width=48, spacing=0),
            ft.Container(card, expand=True, margin=ft.Margin(16, 0, 0, 0)),
        ], vertical_alignment=ft.CrossAxisAlignment.START)

    def build(self):
        entries = [self._build_entry(e, i == len(self.ENTRIES) - 1) for i, e in enumerate(self.ENTRIES)]
        return ft.Column(entries, spacing=20, scroll=ft.ScrollMode.AUTO)