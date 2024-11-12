import flet as ft

def cadastros(page: ft.Page):
    cad = ft.Column(
        controls=[
            ft.Container(
                alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                padding=ft.padding.all(10),
                width=1000,  # Largura do container
                height=500,
            )
        ]
    )
    return cad