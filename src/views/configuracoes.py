import flet as ft
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

from cadastros import cadastros
from graficos import graficos
from perfil import perfil

# Função para a barra de navegação
def navigation_bar(update_content, configuracoes_content, confg, cadastros_content, graficos_content, perfil_content):
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="Gráficos"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações"),
        ],
        on_change=lambda e: escolher_opcao(e, update_content, configuracoes_content, confg, cadastros_content, graficos_content, perfil_content)
    )

# Função para decidir qual conteúdo exibir
def escolher_opcao(e, update_content, configuracoes_content, confg, cadastros_content, graficos_content, perfil_content):
    opcao = e.control.selected_index
    
    if opcao == 1:
        update_content(cadastros_content())  # Exibe a página de cadastros
    elif opcao == 2:
        update_content(graficos_content())  # Exibe a página de gráficos
    elif opcao == 3:
        update_content(perfil_content())  # Exibe a página de perfil
    elif opcao == 4:
        update_content(configuracoes_content())  # Exibe a página de configurações

# Função de configuração
def configuracoes(page: ft.Page):
    a1 = "#C4F7F8"
    a2 = "#04282D"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Funções de conteúdo para cada seção
    def configuracoes_content():
        return configuracoes(page)  # Página de configurações

    def cadastros_content():
        return cadastros(page)  # Página de cadastros

    def graficos_content():
        return graficos(page)  # Página de gráficos

    def perfil_content():
        return perfil(page)  # Página de perfil

    def confg():
        return ft.Column(
            
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo principal verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                navigation_bar(update_content, configuracoes_content, confg, cadastros_content, graficos_content, perfil_content),  # Barra de navegação
                ft.Container(
                    alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    padding=ft.padding.all(10),
                    width=1000,  # Largura do container
                    height=600,
                    content=ft.Column(
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo da coluna
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=50,
                                controls=[
                                    ft.Container(
                                        bgcolor=a1,
                                        border_radius=50,  # Borda arredondada para formar o círculo
                                        width=100,  # Largura do círculo
                                        height=100,  # Altura do círculo
                                    ),
                                    ft.Container(
                                        alignment=ft.alignment.top_center,
                                        bgcolor=a1,
                                        border_radius=50,  # Borda arredondada para formar o círculo
                                        width=100,  # Largura do círculo
                                        height=100,  # Altura do círculo
                                    ),
                                ]
                            ),
        
                            # Agora a linha com o texto "PMGAS" abaixo dos containers circulares
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=70,
                                controls=[
                                    ft.Text(value='PMGAS', weight='bold', size=20, color=a2),
                                    ft.Text(value='PMGAS', weight='bold', size=20, color=a2),
                                ]
                            ),
                            # Aqui estamos centralizando o Container com a palavra 'HELLO'
                            ft.Container(
                                bgcolor=a1,  # Cor de fundo
                                border_radius=15,  # Define borda arredondada para o container
                                width=1000,  # Largura do container
                                height=40,  # Altura do container
                                padding=ft.padding.all(10),
                                alignment=ft.alignment.top_left,
                                content=ft.Column(
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a coluna dentro do container
                                    controls=[
                                        ft.Text(
                                            value='Notificações',
                                            weight='bold',
                                            size=20,
                                            color=a2
                                        ),
                                    ]
                                ),
                            ),
                            ft.Container(
                                bgcolor=a1,  # Cor de fundo
                                border_radius=15,  # Define borda arredondada para o container
                                width=1000,  # Largura do container
                                height=40,  # Altura do container
                                padding=ft.padding.all(10),
                                alignment=ft.alignment.top_left,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a coluna dentro do container
                                    controls=[
                                        ft.Text(
                                            value='Notificações',
                                            weight='bold',
                                            size=20,
                                            color=a2
                                        ),
                                    ]
                                ),
                            ),
                            
                            ft.Container(
                                bgcolor=a1,  # Cor de fundo
                                border_radius=15,  # Define borda arredondada para o container
                                width=1000,  # Largura do container
                                height=40,  # Altura do container
                                padding=ft.padding.all(10),
                                alignment=ft.alignment.top_left,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a coluna dentro do container
                                    controls=[
                                        ft.Text(
                                            value='Notificações',
                                            weight='bold',
                                            size=20,
                                            color=a2
                                        ),
                                    ]
                                ),
                            ),
                            ft.Container(
                                bgcolor=a1,  # Cor de fundo
                                border_radius=15,  # Define borda arredondada para o container
                                width=1000,  # Largura do container
                                height=40,  # Altura do container
                                padding=ft.padding.all(10),
                                alignment=ft.alignment.top_left,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a coluna dentro do container
                                    controls=[
                                        ft.Text(
                                            value='Notificações',
                                            weight='bold',
                                            size=20,
                                            color=a2
                                        ),
                                    ]
                                ),
                            ),
                            ft.Container(
                                bgcolor=a1,  # Cor de fundo
                                border_radius=15,  # Define borda arredondada para o container
                                width=1000,  # Largura do container
                                height=40,  # Altura do container
                                padding=ft.padding.all(10),
                                alignment=ft.alignment.top_left,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a coluna dentro do container
                                    controls=[
                                        ft.Text(
                                            value='Notificações',
                                            weight='bold',
                                            size=20,
                                            color=a2
                                        ),
                                    ]
                                ),
                            ),
                            ft.Container(
                                bgcolor=a1,  # Cor de fundo
                                border_radius=15,  # Define borda arredondada para o container
                                width=1000,  # Largura do container
                                height=40,  # Altura do container
                                padding=ft.padding.all(10),
                                alignment=ft.alignment.top_left,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a coluna dentro do container
                                    controls=[
                                        ft.Text(
                                            value='Notificações',
                                            weight='bold',
                                            size=20,
                                            color=a2
                                        ),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
            ]
        )
    return confg()
