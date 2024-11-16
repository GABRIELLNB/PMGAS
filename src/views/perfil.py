import flet as ft
import sys
from pathlib import Path

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas
sys.path.append(str(root))

from cadastros import cadastros
from graficos import graficos

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

# Função para a barra de navegação
def navigation_bar(update_content, cadastros_content, graficos_content, perfil_content):
    return ft.NavigationBar(
        bgcolor=b,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="Gráficos"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações"),
        ],
        on_change=lambda e: escolher_opcao(e, update_content, cadastros_content, graficos_content, perfil_content)
    )

# Função para decidir qual conteúdo exibir
def escolher_opcao(e, update_content, cadastros_content, graficos_content, perfil_content):
    opcao = e.control.selected_index
    
    if opcao == 0:
        update_content(ft.Text("Página Inicial"))  # Exibe conteúdo para a página inicial
    elif opcao == 1:
        update_content(cadastros_content())  # Exibe a página de cadastros
    elif opcao == 2:
        update_content(graficos_content())  # Exibe a página de gráficos
    elif opcao == 3:
        update_content(perfil_content())  # Exibe a página de perfil

# Função para o conteúdo da página de perfil
def perfil(page: ft.Page):
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Funções de conteúdo para cada seção
    def cadastros_content():
        return cadastros(page)  # Página de cadastros

    def graficos_content():
        return graficos(page)  # Página de gráficos
    
    # Função para gerar a página de perfil
    def perfil_content():
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo principal verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
            # Passa todos os parâmetros necessários
            navigation_bar(update_content, perfil_content, cadastros_content, graficos_content),  # Barra de navegação
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
                            spacing=180,
                            controls=[
                                ft.Container(
                                    bgcolor=a1,
                                    border_radius=50,  # Borda arredondada para formar o círculo
                                    width=100,  # Largura do círculo
                                    height=100,  # Altura do círculo
                                    on_click=lambda e: print("Círculo com ícone de nuvem clicado!"),
                                    content=ft.Icon(
                                        ft.icons.CLOUD,  # Ícone de notificação
                                        size=40,  # Tamanho do ícone ajustado para maior visibilidade
                                        color=b  # Cor do ícone
                                    ),
                                ),
                            ]
                        )
                    ],
                ),
            ),
        ]
    )

    # Retorna o conteúdo da página de perfil
    return perfil_content()  # Chama diretamente a função perfil_content()
