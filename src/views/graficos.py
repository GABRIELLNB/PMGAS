import flet as ft

def graficos(page: ft.Page):
    graf = ft.Column(
        controls=[
            ft.Container(
                alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                bgcolor=ft.colors.PINK,
                border_radius=10,
                padding=ft.padding.all(10),
                width=1000,  # Largura do container
                height=500,
            )
        ]
    )
    return graf