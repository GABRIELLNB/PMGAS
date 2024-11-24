import flet as ft
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

a1 = "#7BD8D9",
a2 = "#04282D",
b = "#FFFFFF"

# Cria a barra de navegação personalizada
def navigation_bar(update_content, configuracoes_content, cadastros_content, perfil_content):
    return ft.NavigationBar(
        bgcolor=b,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfis"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações"),
        ],
        on_change=lambda e: escolher_opcao(e, update_content, configuracoes_content, cadastros_content, perfil_content)
    )

def escolher_opcao(e, update_content, configuracoes_content, cadastros_content, perfil_content):
    opcao = e.control.selected_index
    

    if opcao == 0:
        update_content(cadastros_content())
    elif opcao == 1:
        update_content(perfil_content())
    elif opcao == 2:
        update_content(configuracoes_content())

def menu_adm(page: ft.Page):
    # Define o título da página
    page.title = "PMGAS - Menu"
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    def configuracoes_content():
        from configuracoes_ADM import configuracoes_adm
        return configuracoes_adm(page)

    def cadastros_content():
        from menu_ADM import menu_adm
        return menu_adm(page)

    def perfil_content():
        from perfis_ADM import perfil_adm
        return perfil_adm(page)

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
                navigation_bar(update_content, configuracoes_content, cadastros_content, perfil_content),
                ft.Container(height=20),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[  
                        ft.Container(
                            alignment=ft.alignment.top_center,
                            bgcolor=ft.colors.WHITE,
                            border_radius=10,
                            padding=ft.padding.all(10),
                            width=800,
                            height=350,
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
                            content=ft.Text("Gráficos"),
                            padding=ft.padding.all(10),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.WHITE,
                            width=400,
                            height=200,
                            border_radius=10,
                            ink=True,
                        ),
                        ft.Container(
                            content=ft.Text("Aterros Ronald"),
                            padding=ft.padding.all(10),
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.WHITE,
                            width=400,
                            height=200,
                            border_radius=10,
                            ink=True,
                        )
                    ]
                )
            ]
        )

    # Adiciona o conteúdo inicial à página
    page.scroll = True
    return inicio()  # Inicia com o conteúdo da página inicial
