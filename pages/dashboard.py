import flet as ft
import componentes.componentesarquivo as comp

PRIMARY = "#3E8E41"
ACCENT = "#E74C6E"
BG = "#F5EBDD"


class DashboardView(ft.View):

    def __init__(self, page: ft.Page):

        self.atividades = [
            {
                "nome": "Conversação Japonês",
                "horario": "08h30 - 09h30",
                "imagem": "assets/japa.jpg",
            },
            {
                "nome": "Conversação Mandarim",
                "horario": "10h00 - 11h00",
                "imagem": "assets/japa.jpg",
            },
            {
                "nome": "Kenko Taíso",
                "horario": "11h30 - 12h30",
                "imagem": "assets/japa.jpg",
            },
            {
                "nome": "Smartphone",
                "horario": "14h00 - 15h00",
                "imagem": "assets/japa.jpg",
            },
            {
                "nome": "Dança de Salão",
                "horario": "16h00 - 17h00",
                "imagem": "assets/japa.jpg",
            },
        ]

        self.indice = 0

        self.atividade_nome = ft.Text(
            self.atividades[self.indice]["nome"],
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ACCENT,
            text_align=ft.TextAlign.CENTER,
            width=220,
            max_lines=2,
        )

        self.atividade_imagem = ft.Image(
            src=self.atividades[self.indice]["imagem"],
            width=280,
            height=220,
            fit="contain",
            border_radius=20,
        )

        self.atividade_horario = ft.Text(
            self.atividades[self.indice]["horario"],
            size=22,
            weight=ft.FontWeight.BOLD,
            color=PRIMARY,
            text_align=ft.TextAlign.CENTER,
        )

        header = ft.Row(
            controls=[
                ft.Text(
                    "ENKYO",
                    color=PRIMARY,
                    size=22,
                    weight=ft.FontWeight.BOLD,
                ),

                comp.main_button(
                    "SAIR",
                    on_click=self.go_home,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        settings_button = ft.Container(
            content=ft.IconButton(
                icon=ft.Icons.SETTINGS,
                icon_color=PRIMARY,
                icon_size=28,
                on_click=self.go_settings,
            ),
            alignment=ft.Alignment.TOP_RIGHT,
            padding=ft.padding.only(right=10, top=10),
        )

        ola = ft.Text(
            "OLÁ, (NOME)!",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ACCENT,
            text_align=ft.TextAlign.CENTER,
        )

        trofeu = ft.Image(
            src="assets/trofeu.jpg",
            width=140,
            height=140,
            fit="contain",
        )

        pontos = ft.Text(
            "Sua pontuação mensal é de\nXX pontos!",
            size=20,
            color=PRIMARY,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
        )

        agenda_titulo = ft.Text(
            "AGENDA DO DIA",
            weight=ft.FontWeight.BOLD,
            color=PRIMARY,
            size=22,
            text_align=ft.TextAlign.CENTER,
        )

        navegacao = ft.Row(
            controls=[
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.Icons.ARROW_BACK_IOS,
                        icon_color=PRIMARY,
                        icon_size=30,
                        on_click=self.voltar,
                    ),
                    width=50,
                    alignment=ft.Alignment.CENTER,
                ),

                ft.Container(
                    content=ft.Column(
                        controls=[
                            self.atividade_nome,
                            self.atividade_imagem,
                            self.atividade_horario,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=18,
                    ),
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                ),

                ft.Container(
                    content=ft.IconButton(
                        icon=ft.Icons.ARROW_FORWARD_IOS,
                        icon_color=PRIMARY,
                        icon_size=30,
                        on_click=self.proximo,
                    ),
                    width=50,
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        card = ft.Container(
            content=ft.Column(
                controls=[
                    header,
                    ola,
                    pontos,
                    trofeu,
                    agenda_titulo,
                    navegacao,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            bgcolor="#c4dbc1",
            border_radius=20,
            padding=20,
            width=420,
        )

        super().__init__(
            route="/dashboard",
            bgcolor=BG,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Column(
                    controls=[
                        settings_button,

                        ft.Row(
                            controls=[card],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ]
                )
            ]
        )

    def atualizar(self):
        self.atividade_nome.value = self.atividades[self.indice]["nome"]
        self.atividade_imagem.src = self.atividades[self.indice]["imagem"]
        self.atividade_horario.value = self.atividades[self.indice]["horario"]
        self.page.update()

    def proximo(self, e):
        if self.indice < len(self.atividades) - 1:
            self.indice += 1
            self.atualizar()

    def voltar(self, e):
        if self.indice > 0:
            self.indice -= 1
            self.atualizar()

    async def go_home(self, e):
        await self.page.push_route("/")

    async def go_settings(self, e):
        await self.page.push_route("/settings")