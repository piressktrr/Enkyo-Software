import flet as ft
import componentes.componentesarquivo as comp

PRIMARY = "#3E8E41"
ACCENT = "#E74C6E"
BG = "#F5EBDD"

class LoginView(ft.View):

    def __init__(self, page: ft.Page):

        telefone = comp.input_field("Telefone")
        senha = comp.input_field("Senha", password=True)

        form = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    "ENTRAR",
                                    color="white",
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                bgcolor=PRIMARY,
                                padding=10,
                                border_radius=10,
                                height=60,
                                expand=True,
                                alignment=ft.Alignment.CENTER,
                            ),
                        ]
                    ),

                    ft.Text(
                        "Telefone",
                        color="#4e310a",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                    ),

                    telefone,

                    ft.Text(
                        "Senha",
                        color="#4e310a",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                    ),

                    senha,

                    ft.Container(height=12),

                    comp.main_button(
                        "CONFIRMAR",
                        on_click=self.go_dashboard
                    ),

                    comp.main_button(
                        "VOLTAR",
                        on_click=self.go_home
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor="#c4dbc1",
            border_radius=15,
            padding=ft.padding.only(bottom=20),
            margin=40,
            expand=True,
        )

        layout = ft.Column(
            [
                ft.Text(
                    "ENKYO",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=PRIMARY,
                ),

                ft.Text(
                    "CENTRO DE CONVIVÊNCIA\nDO IDOSO",
                    size=24,
                    text_align=ft.TextAlign.CENTER,
                    color=PRIMARY,
                    weight=ft.FontWeight.W_600,
                ),

                ft.Container(height=10),

                form,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        super().__init__(
            route="/login",
            controls=[layout],
            bgcolor=BG
        )

    async def go_dashboard(self, e):
        await self.page.push_route("/dashboard")

    async def go_home(self, e):
        await self.page.push_route("/")