import flet as ft   
import componentes.componentesarquivo as comp 

#aqui são as cores bases, pra nn ter que ficar reescrevento

PRIMARY = "#3E8E41"
ACCENT = "#E74C6E"
BG = "#F5EBDD"

def main(page: ft.Page):

    page.title = "ENKYO"
    page.bgcolor = BG
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"  


    #componentes reutilizaveis (talvez, acho que vai ser util, vou ver ainda se vai ficar grande o codigo)

    
    comp.input_field(page.title, password=False, color=BG)
    comp.main_button("Entrar", color=ACCENT, on_click=None)
    comp.form_container(comp.input_field("Cadastrar"))



    #aqui são as pages 
    #
    #
    #
    #
    #
    #
    #
    




    def go_login(e):
        page.controls.clear()

        titulo = ft.Text(
            "ENKYO",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=PRIMARY,
        )

        subtitulo = ft.Text(
            "CENTRO DE CONVIVÊNCIA\nDO IDOSO",
            size=24,
            text_align=ft.TextAlign.CENTER,
            color=PRIMARY,
            weight=ft.FontWeight.W_600,
        )

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
                        text_align=ft.TextAlign.LEFT,
                        color="#4e310a",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        ),
                    telefone,

                    ft.Text(
                        "Senha",
                        text_align=ft.TextAlign.LEFT,
                        color="#4e310a",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        ),
                    senha,

                    ft.Container(height=12),

                    comp.main_button("CONFIRMAR", on_click=go_dashboard),
                    comp.main_button("VOLTAR", on_click=home),
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
                titulo,
                subtitulo,
                ft.Container(height=10),
                form,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        page.add(layout)
        page.update()
            

    def atualizar_senha(e):
        page.controls.clear()

        titulo = ft.Container(
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

        subtitulo = ft.Text(
            "CAMPO DEDICADO APENAS PARA ALTERAR SUA SENHA, TENHA CERTEZA DO QUE ESTÁ FAZENDO!",
            color="#000000",
            size=16,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,

        )

        senha_atual = comp.input_field("Senha atual")
        senha_nova = comp.input_field("Nova senha")
        confirmar_senha = comp.input_field("Confirmar nova senha")

        form = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[titulo],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.Container(height=10),
                    subtitulo,

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

                    comp.main_button("CONFIRMAR", on_click=None), ## fazer aqui pra ele confirmar que realmente quer trocar a senha
                    comp.main_button("VOLTAR", on_click=home),
                ],
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#c4dbc1",
            border_radius=20,
            padding=20,
            width=360,
        )

        page.add(
            ft.Row(
                controls=[form],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        page.update()





    def go_register(e):
        page.controls.clear()

        titulo = ft.Container(
            content=ft.Text(
                "CADASTRO",
                size=26,
                weight=ft.FontWeight.BOLD,
                color="white",
                text_align=ft.TextAlign.CENTER,
            ),
            bgcolor=PRIMARY,
            padding=15,
            border_radius=12,
        )

        nome = comp.input_field("Nome completo")
        telefone = comp.input_field("Telefone")
        senha = comp.input_field("Senha", password=True)
        confirmar = comp.input_field("Confirmar senha", password=True)

        form = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[titulo],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.Container(height=10),

                    ft.Text(
                        "Nome completo",
                        color="#4e310a",
                        size=20,
                        weight=ft.FontWeight.W_500,
                    ),
                    nome,

                    ft.Text(
                        "Telefone",
                        color="#4e310a",
                        size=20,
                        weight=ft.FontWeight.W_500,
                    ),
                    telefone,

                    ft.Text(
                        "Senha",
                        color="#4e310a",
                        size=20,
                        weight=ft.FontWeight.W_500,
                    ),
                    senha,

                    ft.Text(
                        "Confirmação da Senha",
                        color="#4e310a",
                        size=20,
                        weight=ft.FontWeight.W_500,
                    ),
                    confirmar,

                    ft.Container(height=15),

                    comp.main_button("CONFIRMAR", on_click=go_dashboard),
                    comp.main_button("VOLTAR", on_click=home),
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#c4dbc1",
            border_radius=20,
            padding=20,
            width=360,
        )

        page.add(
            ft.Row(
                controls=[form],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        page.update()





    def go_dashboard(e):
        page.controls.clear()
        page.scroll = ft.ScrollMode.AUTO

        atividades = [
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

        indice = {"valor": 0}

        atividade_nome = ft.Text(
            atividades[indice["valor"]]["nome"],
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ACCENT,
            text_align=ft.TextAlign.CENTER,
            width=220,
            max_lines=2,
        )       

        atividade_imagem = ft.Image(
            src=atividades[indice["valor"]]["imagem"],
            width=280,
            height=220,
            fit="contain",
            border_radius=20,
        )

        atividade_horario = ft.Text(
            atividades[indice["valor"]]["horario"],
            size=22,
            weight=ft.FontWeight.BOLD,
            color=PRIMARY,
            text_align=ft.TextAlign.CENTER,
        )

        def atualizar():
            atividade_nome.value = atividades[indice["valor"]]["nome"]
            atividade_imagem.src = atividades[indice["valor"]]["imagem"]
            atividade_horario.value = atividades[indice["valor"]]["horario"]
            page.update()

        def proximo(e):
            if indice["valor"] < len(atividades) - 1:
                indice["valor"] += 1
                atualizar()

        def voltar(e):
            if indice["valor"] > 0:
                indice["valor"] -= 1
                atualizar()

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
                    on_click=home,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
                        on_click=voltar,
                    ),
                    width=50,
                    alignment=ft.Alignment.CENTER,
                ),

                ft.Container(
                    content=ft.Column(
                        controls=[
                            atividade_nome,
                            atividade_imagem,
                            atividade_horario,
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
                        on_click=proximo,
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

        page.add(
            ft.Row(
                controls=[card],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        page.update()





    def home(e=None):
        page.controls.clear()
        page.bgcolor=BG


        titulo = ft.Container(
            content=ft.Text( 
                "ENKYO",
                size=45,
                weight=ft.FontWeight.BOLD,
                color=PRIMARY,
                text_align=ft.TextAlign.CENTER,
            ),
            margin=ft.margin.only(bottom=4),
        )


        subtitulo = ft.Text(
            "Centro de convivência ao idoso!",
            color=PRIMARY,
            size=15,
            text_align=ft.TextAlign.CENTER,

        )

        botoes = ft.Column( 
            controls=[
                comp.main_button("Entrar", color=ACCENT, on_click=go_login),
                comp.main_button("Cadastrar", color=ACCENT, on_click=go_register),
                comp.main_button("Esqueci minha senha", color=ACCENT, on_click=atualizar_senha),
                comp.main_button("Sair", color=ACCENT, on_click=page.window.close),
            ],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )



        page.add(
            ft.Column(titulo),
            ft.Column(subtitulo),
            ft.Column(botoes),
        )

        page.update()

    home()

ft.app(target=main)
