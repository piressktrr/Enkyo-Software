import flet as ft    

PRIMARY = "#3E8E41"
ACCENT = "#E74C6E"
BG = "#F5EBDD"

class Componentes:
    def __init__(self):
        
        def input_field(label, password=False, color=BG):
            return ft.TextField(
                label=label,
                password=password,
                color=color,
                border=ft.InputBorder.OUTLINE,
                border_color="transparent",
                border_radius=20,
                filled=True,
                bgcolor="#EDE6D6",
                text_size=15,
                width=260,
                height=45,
                content_padding=12,
                margin=ft.Margin.only(left=20, right=20),
            )
    
        def main_button(text, color=ACCENT, on_click=None):
            return ft.Button(
                text,
                bgcolor=color,
                color="white",
                width=200,
                height=45,
                on_click=on_click,
                margin=ft.Margin.only(left=20, right=20),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
            )
    
        def form_container(content):
            return ft.Container(
                content=content,
                bgcolor="#C7D9C1",
                border_radius=20,
                padding=25,
            )