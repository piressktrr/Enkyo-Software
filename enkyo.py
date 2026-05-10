import flet as ft

from pages.home import HomeView
from pages.login import LoginView
from pages.register import RegisterView
from pages.atualizar_senha import AtualizarSenhaView
from pages.dashboard import DashboardView
from pages.settings import SettingsView

PRIMARY = "#3E8E41"
ACCENT = "#E74C6E"
BG = "#F5EBDD"


def main(page: ft.Page):

    page.title = "ENKYO"
    page.bgcolor = BG
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def route_change():

        page.views.clear()

        #home
        page.views.append(HomeView(page))

        #login
        if page.route == "/login":
            page.views.append(LoginView(page))

        #register
        if page.route == "/register":
            page.views.append(RegisterView(page))

        #atualizar a senha lá
        if page.route == "/senha":
            page.views.append(AtualizarSenhaView(page))

        #dashboard
        if page.route == "/dashboard":
            page.views.append(DashboardView(page))

        #settings
        if page.route == "/settings":
            page.views.append(SettingsView(page))

        page.update()

    
    async def view_pop(e: ft.ViewPopEvent):

        if e.view is not None:

            page.views.remove(e.view)

            top_view = page.views[-1]

            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


if __name__ == "__main__":
    ft.run(main)