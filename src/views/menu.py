import flet as ft 

def menu(page: ft.Page, menu):
    menu = ft.Column(
       controls = [
            ft.Text(
                value='PMGAS',
                weight='bold',
                size=30,
                color=ft.colors.WHITE,
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                width=400,
                padding=ft.padding.all(10),
                
            )
       ]
    )
    return menu