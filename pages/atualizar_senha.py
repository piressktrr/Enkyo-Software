import flet as ft
import componentes.componentesarquivo as comp

PRIMARY = "#3E8E41"
BG = "#F5EBDD"

class AtualizarSenhaView(ft.View):

    def __init__(self, page: ft.Page):

        senha_atual = comp.input_field("Senha atual")
        senha_nova = comp.input_field("Nova senha")
        confirmar_senha = comp.input_field("Confirmar nova senha")

        form = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    "Atualizar sua Senha!",
                                    size=26,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                bgcolor=PRIMARY,
                                padding=15,
                                border_radius=12,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.Container(height=10),

                    ft.Text(
                        "CAMPO DEDICADO APENAS PARA ALTERAR SUA SENHA, TENHA CERTEZA DO QUE ESTÁ FAZENDO!",
                        color="#000000",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),

                    ft.Text(
                        "Senha atual",
                        color="#000000",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),

                    senha_atual,

                    ft.Text(
                        "Nova senha",
                        color="#000000",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),

                    senha_nova,

                    ft.Text(
                        "Confirmar nova senha",
                        color="#000000",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),

                    confirmar_senha,

                    ft.Container(height=15),

                    comp.main_button(
                        "CONFIRMAR",
                        on_click=None
                    ),

                    comp.main_button(
                        "VOLTAR",
                        on_click=self.go_home
                    ),
                ],
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#c4dbc1",
            border_radius=20,
            padding=20,
            width=360,
        )

        super().__init__(
            route="/senha",
            controls=[
                ft.Row(
                    controls=[form],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            bgcolor=BG
        )

    async def go_home(self, e):
        await self.page.push_route("/")