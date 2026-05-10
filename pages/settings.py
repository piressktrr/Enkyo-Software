import flet as ft
import componentes.componentesarquivo as comp

PRIMARY = "#3E8E41"
ACCENT = "#E74C6E"
BG = "#F5EBDD"


class SettingsView(ft.View):

    def __init__(self, page: ft.Page):

        card = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "CONFIGURAÇÕES",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY,
                        text_align=ft.TextAlign.CENTER,
                    ),

                    ft.Container(height=20),

                    comp.main_button(
                        "Trocar Senha",
                        on_click=self.go_senha
                    ),

                    comp.main_button(
                        "Deletar Conta",
                        color="#B00020",
                        on_click=None
                    ),

                    ft.Container(height=10),

                    comp.main_button(
                        "VOLTAR",
                        on_click=self.go_dashboard
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            ),
            bgcolor="#c4dbc1",
            border_radius=20,
            padding=30,
            width=360,
        )

        super().__init__(
            route="/settings",
            bgcolor=BG,
            controls=[
                ft.Row(
                    controls=[card],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )

    async def go_senha(self, e):
        await self.page.push_route("/senha")

    async def go_dashboard(self, e):
        await self.page.push_route("/dashboard")