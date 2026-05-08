import flet as ft
from componentes.componentesarquivo import input_field

def main(page: ft.Page):

    
    campo_nome = input_field("Nome")
    botao = main_button("Enviar")

    page.add(campo_nome)
    page.add(botao)

ft.app(target=main)