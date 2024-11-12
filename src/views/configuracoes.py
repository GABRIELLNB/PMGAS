import flet as ft

def configuracoes(page: ft.Page):
    confg = ft.Column(
        controls=[  # Corrigido para colocar o Container dentro de controls
            ft.Container(
                alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                bgcolor=ft.colors.BLACK,
                border_radius=10,
                padding=ft.padding.all(10),
                width=1000,  # Largura do container
                height=500,
            )
        ]
    )
    return confg
