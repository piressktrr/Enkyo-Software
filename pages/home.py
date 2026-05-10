import flet as ft
import componentes.componentesarquivo as comp

PRIMARY = "#3E8E41"
ACCENT = "#E74C6E"
BG = "#F5EBDD"


class HomeView(ft.View):

    def __init__(self, page: ft.Page):

        botoes = ft.Column(
            controls=[
                comp.main_button(
                    "Entrar",
                    color=ACCENT,
                    on_click=self.go_login
                ),

                comp.main_button(
                    "Cadastrar",
                    color=ACCENT,
                    on_click=self.go_register
                ),

                comp.main_button(
                    "Sair",
                    color=ACCENT,
                    on_click=page.window.close
                ),
            ],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        super().__init__(
            route="/",
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                "ENKYO",
                                size=45,
                                weight=ft.FontWeight.BOLD,
                                color=PRIMARY,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            margin=ft.margin.only(bottom=4),
                        ),

                        ft.Text(
                            "Centro de convivência ao idoso!",
                            color=PRIMARY,
                            size=15,
                            text_align=ft.TextAlign.CENTER,
                        ),

                        botoes
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            bgcolor=BG,
        )

    async def go_login(self, e):
        await self.page.push_route("/login")

    async def go_register(self, e):
        await self.page.push_route("/register")