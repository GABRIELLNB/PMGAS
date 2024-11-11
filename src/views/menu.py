import flet as ft

def menu(page: ft.Page):
    # Define o título da página
    page.title = "Exemplo de NavigationBar"
    
    # Cria a barra de navegação personalizada
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Comutar"),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Favoritos",
            ),
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
                width=1000,  # Largura do container
                height=500,  # Altura do container
            ),
            # Row com Containers centralizados
            ft.Row(
                controls = [
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        border_radius=10,
                        padding=ft.padding.all(10),
                        width=400,  # Largura do container
                        height=100,  # Altura do container
                    ),
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        border_radius=10,
                        padding=ft.padding.all(10),
                        width=400,  # Largura do container
                        height=100,  # Altura do container
                    ),
                ]
            )
        ]
    )

    page.scroll = True
    return inicio
