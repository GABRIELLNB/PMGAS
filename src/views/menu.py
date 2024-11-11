import flet as ft

def menu(page: ft.Page):
    # Define o título da página
    page.title = "PMGAS"
    
    # Cria a barra de navegação personalizada
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(
                icon=ft.icons.BAR_CHART,
                selected_icon=ft.icons.BOOKMARK,
                label="Gráficos",
            ),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Config"),
        ]
    )
    
    # Define o conteúdo da página
    inicio = ft.Column(
        controls=[  # Aqui você deve ter apenas um "controls"
        ft.Text(
                value='PMGAS',
                weight='bold',
                size=30,
                color=ft.colors.WHITE,
            ),
        
            navigation_bar,  # Coloca a barra de navegação no topo
            ft.Text("Conteúdo da Página"),  # Adiciona o conteúdo abaixo da barra
            
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                padding=ft.padding.all(10),
                width=800,  # Largura do container
                height=300,  # Altura do container
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value="HELLO"
                        )
                    ]
                )
            ),
            # Row com Containers centralizados
            ft.Row(
                controls = [
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        border_radius=10,
                        padding=ft.padding.all(10),
                        width=400,  # Largura do container
                        height=200,  # Altura do container
                    ),
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        border_radius=10,
                        padding=ft.padding.all(10),
                        width=400,  # Largura do container
                        height=200,  # Altura do container
                    ),
                ]
            )
        ]
    )

    page.scroll = True
    return inicio
