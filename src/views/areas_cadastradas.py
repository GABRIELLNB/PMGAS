import flet as ft
import sys
from pathlib import Path

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas
sys.path.append(str(root))

from edit_area import edit_area

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"


# Função de configuração
def areas_cadastradas(page: ft.Page):
    from perfil import perfil
    page.title = "PMGAS - Perfis"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página
    
    def areas(nome, natureza, porte, cnpj, cep):
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
                                        value=f"Natureza Juridica: : {natureza}",
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
                                        value=f"Porte da Empresa:: {porte}",
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
                                        value=f"CNPJ: {cnpj}",
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
                                        value=f"CEP: {cep}",
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
                                                ft.icons.EDIT_SQUARE,
                                                size=24,
                                                color=a2,
                                            ),
                                            on_click=lambda e: update_content(edit_area(page))
                                            
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

        

    # Função principal para montar a página de perfil
    def area():
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(height=5),
                ft.Container(
                    alignment=ft.alignment.center,  # Alinha o título no centro
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                on_click=lambda e: update_content(perfil(page)),
                                content=ft.Icon(
                                    ft.icons.ARROW_BACK_IOS,
                                    size=24,
                                    color=b,
                                ),
                            ),
                            ft.Container(width=500),
                            ft.Icon(ft.icons.EDIT_SQUARE, size=24, color=b),
                            ft.Text(
                                value="Áreas Cadastradas",
                                weight="bold",
                                size=20,
                                color=b,
                            ),
                            ft.Container(width=550),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,  # Alinha o conteúdo da Row
                                    spacing=10,  # Espaço entre os elementos da Row
                                ),
                            ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,  # Alinha os itens à direita
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha verticalmente ao centro
                    controls=[
                        # SearchBar
                        ft.Container(height=15),
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
                        ft.Container(width=260),
                        
                    ],
                ),
                ft.Divider(
                    height=1,
                    color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                    thickness=1,
                ),
                ft.Container(height=10),
                areas(nome ="ass", natureza="assd",porte="asdffdgf" ,cnpj="dsfds",cep="aasfgdf" ),
                areas(nome ="ass", natureza="assd",porte="asdffdgf" ,cnpj="dsfds",cep="aasfgdf" ),
            ],
        )

    return area()
