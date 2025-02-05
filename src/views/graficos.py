import flet as ft
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas
sys.path.append(str(root))

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

from models.BgraficoGas import grs_ano
# Função para a barra de navegação
def navigation_bar(update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, menu_content):
    
    return ft.NavigationBar(
        bgcolor=b,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio", bgcolor=a2),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros", bgcolor=a2),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="Gráficos", bgcolor=a2),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil", bgcolor=a2),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações", bgcolor=a2),
        ],
        on_change=lambda e: escolher_opcao(e, update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, menu_content)
    )

# Função para decidir qual conteúdo exibir
def escolher_opcao(e, update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, menu_content):
    opcao = e.control.selected_index
    
    if opcao == 0:
        update_content(menu_content())
    elif opcao == 1:
        update_content(cadastros_content())  # Exibe a página de cadastros
    elif opcao == 2:
        update_content(graficos_content())  # Exibe a página de gráficos
    elif opcao == 3:
        update_content(perfil_content())  # Exibe a página de perfil
    elif opcao == 4:
        update_content(configuracoes_content())  # Exibe a página de configurações


# Função de configuração
def graficos(page: ft.Page):
    
    page.title = "PMGAS - Gráficos"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Função para retornar a página de perfil
    def perfil_content():
        from perfil import perfil_us
        return perfil_us(page)

    # Funções de conteúdo para cada seção
    def configuracoes_content():
        from configuracoes import configuracoes
        return configuracoes(page)  # Página de configurações

    def cadastros_content():
        from cadastros import cadastros
        return cadastros(page)  # Página de cadastros

    def graficos_content():
        return graficos(page)  # Página de gráficos

    def menu_content():
        from menu import menu
        return menu(page)

    # Função principal para montar a página de perfil
    def graf():
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo principal verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(height=5),
                ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a imagem horizontalmente
                controls=[
                    ft.Image(
                        src="image.png",  # Caminho local ou URL da imagem
                        width=250,
                        height=50,
                        fit=ft.ImageFit.CONTAIN,  # Mantém proporção
                    )
                ]
            ),
                navigation_bar(update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, menu_content),
                ft.Container(
                    alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    padding=ft.padding.all(10),
                    width=1000,  # Largura do container
                    height=1000,
                    content=ft.Column(
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo da coluna
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                            alignment=ft.alignment.top_left,  # Alinha o texto no canto superior esquerdo
                            content=ft.Text(value='Gráficos - Gás Metano (CH₄)', weight='bold', size=18, color=a2)
                        ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1
                            ),
                           
                            ft.Image(
                                src="grafico_bahia.png",  # Caminho local ou URL da imagem
                                width=700,  # Largura da imagem
                                height=400,  # Altura da imagem
                                fit=ft.ImageFit.CONTAIN,  # Ajuste da imagem
                            ),
                            ft.Container(
                            alignment=ft.alignment.top_left,  # Alinha o texto no canto superior esquerdo
                            content=ft.Text(value='Gráficos - Temperatura por profundidade', weight='bold', size=18, color=a2)
                        ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1
                            ),
                           
                            ft.Image(
                                src="grafico_temp2.png",  # Caminho local ou URL da imagem
                                width=700,  # Largura da imagem
                                height=400,  # Altura da imagem
                                fit=ft.ImageFit.CONTAIN,  # Ajuste da imagem
                            ),
                            
                        ],
                    ),
                ),
            ],
        )
    page.scroll = True
    return graf()