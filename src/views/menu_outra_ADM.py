import flet as ft
import sys
from pathlib import Path

# Configurações de cores
a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"
p = '#000000'
# Configurações de caminho e importações relativas
file = Path(__file__).resolve()
root = file.parent.parent
sys.path.append(str(root))


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
def menu_outra_ADM(page: ft.Page):
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



    # Conteúdo inicial
    def inc():
        from menu_ADM import menu_adm
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value="PMGAS", weight="bold", size=30, color=ft.colors.WHITE),
                navigation_bar(update_content, configuracoes_content, cadastros_content, perfil_content),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,  # Alinha os itens à direita
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha verticalmente ao centro
                ),
                ft.Container(height=10),
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    width=1300,
                    height=600,
                    padding=ft.padding.all(10),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            on_click=lambda e: update_content(menu_adm(page)),
                                            content=ft.Icon(
                                                ft.icons.ARROW_BACK_IOS,
                                                size=24,
                                                color=a2,
                                            ),
                                        ),
                                        ft.Container(width=438),
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            content=ft.Text(value="DADOS DA ÁREA xxxxxxxxxxxxx", weight="bold", size=20, color=a2),
                                        ),
                                        ft.Container(width=500),
                                    ],
                                
                                ),
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                                thickness=1,
                            ),
                            # Formulário de entrada
                            ft.Container(
                                bgcolor=b,
                                padding=ft.padding.all(6),
                                border_radius=10,
                                width=1300,
                                height=240,
                                content=ft.Column(
                                    controls=[
                                        ft.Container(height=10),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Icon(ft.icons.PERSON, color=ft.colors.with_opacity(0.9, a2), size=20),
                                                ft.Text(
                                                    value="Nome do Proprietário: ",
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
                                                    value="Nome Jurídico: Empresa XYZ Ltda.",
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
                                                    value="Porte da Empresa: Grande",
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
                                                    value="CNPJ: 12.345.678/0001-99",
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
                                                    value="CEP: 12345-678",
                                                    style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                                ),
                                            ],
                                        ),
                                        ft.Divider(
                                            height=1,
                                            color=ft.colors.with_opacity(0.25, a2),
                                            thickness=1,
                                        ),
                                    ],
                                ),
                            ),
                            
                            ft.Container(height=10),
                            ft.Container(
                                    content=ft.Text(value="DADOS COLETADOS", weight="bold", size=18, color=a2),
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                                thickness=1,
                            ),
                            ft.Container(
                                bgcolor=a2,
                                padding=ft.padding.all(6),
                                border_radius=10,
                                width=1300,
                                height=100,
                            ),
                            ft.Container(
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=10,
                                    controls=[
                                        ft.Container(
                                            on_click=lambda e: update_content(menu_adm(page)),
                                            content=ft.Icon(
                                                ft.icons.FILE_DOWNLOAD_OUTLINED,
                                                size=24,
                                                color=a2,
                                            ),
                                        ),
                                        ft.Container(
                                            on_click=lambda e: update_content(menu_adm(page)),
                                            content=ft.Icon(
                                                ft.icons.DELETE,
                                                size=24,
                                                color=a2,
                                            ),
                                        ),
                                        ft.Container(width=15),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        )
        
    page.scroll = True
    return inc()
