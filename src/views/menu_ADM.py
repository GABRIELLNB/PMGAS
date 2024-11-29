import flet as ft
import sys
from pathlib import Path

# Configurações de cores
a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

# Configurações de caminho e importações relativas
file = Path(__file__).resolve()
root = file.parent.parent
sys.path.append(str(root))

from excluir import excluir


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


# Define a troca de opções na barra de navegação
def escolher_opcao(e, update_content, configuracoes_content, cadastros_content, perfil_content):
    opcao = e.control.selected_index
    if opcao == 0:
        update_content(cadastros_content())
    elif opcao == 1:
        update_content(perfil_content())
    elif opcao == 2:
        update_content(configuracoes_content())


# Menu Administrativo
def menu_adm(page: ft.Page):
    from menu_outra_ADM import menu_outra_ADM
    
    # Configuração da página
    page.title = "PMGAS - Menu"
    page.scroll = True

    def update_content(content):
        page.controls.clear()
        page.controls.append(content)
        page.update()

    # Conteúdos do menu
    def configuracoes_content():
        from configuracoes_ADM import configuracoes_adm
        return configuracoes_adm(page)

    def cadastros_content():
        from menu_ADM import menu_adm
        return menu_adm(page)

    def perfil_content():
        from perfis_ADM import perfil_adm
        return perfil_adm(page)
    
    def cad(nome_proprietario, nome_juridico, porte_empresa, cnpj, cep, area):
        return ft.Container(
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    width=1000,
                    height=330,
                    padding=ft.padding.all(10),
                    on_click=lambda e:update_content(menu_outra_ADM(page)),
                    content=ft.Column(
                        controls=[
                            # Dados da área
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Text(value=f"DADOS DA ÁREA {area}", weight="bold", size=20, color=a2),
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                                thickness=1,
                            ),
                            # Formulário de entrada
                            ft.Container(
                                bgcolor=b,
                                padding=ft.padding.all(10),
                                border_radius=10,
                                width=1000,
                                height=270,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.PERSON, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Nome do Proprietário: {nome_proprietario}",
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
                                        value=f"Nome Jurídico: {nome_juridico}",
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
                                        value=f"Porte da Empresa: {porte_empresa}",
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
                                                ft.icons.DELETE,
                                                size=24,
                                                color=a2,
                                            ),
                                            on_click=lambda e: update_content(excluir(page)),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )



    # Conteúdo inicial
    def inicio():
  
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value="PMGAS", weight="bold", size=30, color=ft.colors.WHITE),
                navigation_bar(update_content, configuracoes_content, cadastros_content, perfil_content),
                ft.Container(height=10),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,  # Alinha os itens à direita
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
                        ft.Container(width=125),
                        # Botão com ícone
                        ft.Container(
                            alignment=ft.alignment.center,
                            bgcolor=a2,
                            width=40,  # Largura do círculo
                            height=40,  # Altura do círculo
                            content=ft.Icon(
                                ft.icons.EDIT_DOCUMENT,  # Ícone de notificação
                                size=40,  # Tamanho do ícone ajustado para maior visibilidade
                                color=b  # Cor do ícone
                            ),
                        ),
                        
                        ft.Container(width=75),
                        
                    ],
                ),
                ft.Divider(
                    height=1,
                    color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                    thickness=1,
                ),
                ft.Container(height=10),
                cad(nome_proprietario= "sa", nome_juridico="as", porte_empresa="as", cnpj="as", cep="as",area="xxxxxxxxxxxxxxx"),
            ],
        )

    return inicio()
