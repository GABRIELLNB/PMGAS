import flet as ft
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

from configuracoes import configuracoes
from cadastros import cadastros
from graficos import graficos
from perfil import perfil

# Cria a barra de navegação personalizada
def navigation_bar(update_content, configuracoes_content, inicio, cadastros_content, graficos_content, perfil_content, inicio_content):
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="Gráficos"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações"),
        ],
        on_change=lambda e: escolher_opcao(e, update_content, configuracoes_content, inicio, cadastros_content, graficos_content, perfil_content, inicio_content)
    )

def escolher_opcao(e, update_content, configuracoes_content, inicio, cadastros_content, graficos_content, perfil_content, inicio_content):
    
    opcao = e.control.selected_index
    if opcao == 0:
        update_content(inicio_content())
    elif opcao == 1:
        update_content(cadastros_content())
    elif opcao == 2:
        update_content(graficos_content())
    elif opcao == 3:
        update_content(perfil_content())
    elif opcao == 4:
        update_content(configuracoes_content())

def menu(page: ft.Page):
    # Define o título da página
    page.title = "PMGAS"
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    def inicio_content():
        return inicio()

    def configuracoes_content():
        return configuracoes(page)

    def cadastros_content():
        return cadastros(page)

    def graficos_content():
        return graficos(page)

    def perfil_content():
        return perfil(page)

    # Define o conteúdo da página inicial
    def inicio():
        return ft.Column(
            controls=[
                ft.Text(
                    value='PMGAS',
                    weight='bold',
                    size=30,
                    color=ft.colors.WHITE,
                ),
                navigation_bar(update_content, configuracoes_content, inicio, cadastros_content, graficos_content, perfil_content, inicio_content),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.top_center,
                            bgcolor=ft.colors.WHITE,
                            border_radius=10,
                            padding=ft.padding.all(10),
                            width=1000,
                            height=500,
                            content=ft.Column(
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
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            border_radius=10,
                            padding=ft.padding.all(10),
                            width=400,
                            height=200,
                        ),
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            border_radius=10,
                            padding=ft.padding.all(10),
                            width=400,
                            height=200,
                        ),
                    ]
                )
            ]
        )

    # Adiciona o conteúdo inicial à página
    page.scroll = True
    return inicio()  # Inicia com o conteúdo da página inicial
