import flet as ft
import sys
from pathlib import Path

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas
sys.path.append(str(root))

from edit_perfil import edit_perfil
from edit_area import edit_area
from models.ADM_perfis import ler_perfis_excel

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

# Função para a barra de navegação
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

# Função de configuração
def perfil_adm(page: ft.Page):
    
    page.title = "PMGAS - Perfis"
    
    caminho_arquivo = "Contas - PMGAS.xlsx"
    perfis = ler_perfis_excel(caminho_arquivo)

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Função para retornar a página de perfil
    def perfil_content():
        return perfil_adm(page)

    # Funções de conteúdo para cada seção
    def configuracoes_content():
        from configuracoes_ADM import configuracoes_adm
        return configuracoes_adm(page)  # Página de configurações

    def cadastros_content():
        from menu_ADM import menu_adm
        return menu_adm(page)  # Página de cadastros
    
    def perfis_content(email, nome, cpf, senha, cadastros):
        return ft.Container(
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        width=1000,
        height=280,
        padding=ft.padding.all(10),
        content=ft.Column(
            controls=[
                ft.Container(
                    bgcolor=b,
                    padding=ft.padding.all(10),
                    border_radius=10,
                    width=1300,
                    height=252,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.PERSON, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Email: {email}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.BUSINESS, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Nome: {nome}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.BUSINESS, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"CPF: {cpf}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.CONTACT_PAGE, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Senha: {senha}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.LOCATION_CITY, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Cadastros: {cadastros}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Container(
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=10,
                                    controls=[
                                        ft.Container(
                                            content=ft.Icon(
                                                ft.icons.DELETE,
                                                size=24,
                                                color=a2,
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
                ft.Container(height=10),
            ],
        ),
    )
        
    search_term = ""
    # Função principal para montar a página de perfil
    def perf():
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
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
                navigation_bar(update_content, configuracoes_content, cadastros_content, perfil_content),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,  # Alinha os itens à direita
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha verticalmente ao centro
                    controls=[
                        # SearchBar
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            padding=ft.padding.symmetric(horizontal=10, vertical=5),
                            border_radius=15,
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(ft.icons.SEARCH, color=ft.colors.GREY),
                                    ft.TextField(
                                        hint_text="Buscar...",
                                        border=ft.InputBorder.NONE,
                                        cursor_color=ft.colors.BLACK,
                                        text_style=ft.TextStyle(
                                            size=16, color=ft.colors.BLACK
                                        ),
                                        expand=True,
                                    ),
                                    ft.Icon(ft.icons.CLOSE, color=ft.colors.GREY),
                                ],
                            ),
                            width=1000,  # Ajusta a largura do SearchBar
                        ),

            
                    ],
                ),
                ft.Divider(
                    height=1,
                    color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                    thickness=1,
                ),
                ft.Container(height=10),
                *[perfis_content(p["Email"], p["Nome"], p["CPF"], p["Senha"], p["Cadastros"]) for p in perfis],  # Exibe todos os perfis
            ],
        )
    

    return perf()