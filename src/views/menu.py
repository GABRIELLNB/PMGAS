import flet as ft
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root =  file.parent.parent  # Importações relativas


sys.path.append(str(root))

from configuracoes import configuracoes

def menu(page: ft.Page):
    # Define o título da página
    page.title = "PMGAS"
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(navigation_bar)  # Re-adiciona a barra de navegação
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    
    # Cria a barra de navegação personalizada
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio" ),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="Gráficos"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações"),
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
            
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o container na linha
                controls=[
                    ft.Container(
                        alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                        bgcolor=ft.colors.WHITE,
                        border_radius=10,
                        padding=ft.padding.all(10),
                        width=1000,  # Largura do container
                        height=500,  # Altura do container
                        content=ft.Column(  # Coloca o conteúdo dentro do container
                            controls=[
                                ft.Text(
                                    value='HELLO',
                                    weight='bold',
                                    size=20,
                                    color=ft.colors.BLACK
                                ),
                            ]
                        ),
                    ),
                ]
            ),
            # Row com Containers centralizados
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
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
