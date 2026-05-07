import flet as ft

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

    def input_field(label, password=False):
        return ft.TextField(
            label=label,
            password=password,
            border="none",
            filled=True,
            bgcolor="#EDE6D6",
            border_radius=20,
            text_size=15,
            width=260,
            height=45,
            content_padding=12,
        )
    
    def main_button(text, color=ACCENT, on_click=None):
        return ft.Button(
            text,
            bgcolor=color,
            color="white",
            width=200,
            height=45,
            on_click=on_click,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
        )
    
    def form_container(content):
        return ft.Container(
            content=content,
            bgcolor="#C7D9C1",
            border_radius=20,
            padding=25,
        )

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
        )





            
    def go_register(e):
        page.controls.clear()

        page.add(
            ft.Text("CADASTRO"),
            ft.Button("VOLTAR", on_click=home)
        )

    def go_dashboard(e):
        page.controls.clear()

        page.add(
            ft.Text("DASHBOARD"),
            ft.Button("SAIR", on_click=home)
        )

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
                main_button("Entrar", color=ACCENT, on_click=go_login),
                main_button("Cadastrar", color=ACCENT, on_click=go_register),
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