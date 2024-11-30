import flet as ft
import sys
from pathlib import Path

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas
sys.path.append(str(root))

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

from sair_ADM import sair_da_conta_adm
from edit_perfil_ADM import edit_perfil_adm

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
def configuracoes_adm(page: ft.Page):
    
    page.title = "PMGAS - Configurações"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Funções de conteúdo para cada seção
    def configuracoes_content():
        return configuracoes_adm(page)  # Página de configurações

    def cadastros_content():
        from menu_ADM import menu_adm
        return menu_adm(page)  # Página de cadastros

    def perfil_content():
        from perfis_ADM import perfil_adm
        return perfil_adm(page)  # Página de perfil
    
    def adm(id, email, senha):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                ft.Text(value=f"ID: {id}", weight='bold', size=20, color=a2),
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                ft.Text(value=f"Email: {email}", weight='bold', size=20, color=a2),
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                ft.Text(value=f"Senha: {senha}", weight='bold', size=20, color=a2)
                            )
                        ]
                    ),
                ],
            ),
        )
    
    def confg():
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
                navigation_bar(update_content, configuracoes_content, cadastros_content, perfil_content), 
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
                                alignment=ft.MainAxisAlignment.END,
                                spacing=15,
                                controls=[
                                    ft.Container(
                                        on_click=lambda e: update_content(edit_perfil_adm(page)),
                                        content=ft.Icon(
                                        ft.icons.EDIT_SQUARE,  # Ícone de notificação
                                                size=40,  # Tamanho do ícone ajustado para maior visibilidade
                                                color=a2  # Cor do ícone
                                            ),
                                        
                                    ),
                                ]
                            ),
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
                                        ft.icons.PERSON,  # Ícone de notificação
                                                size=40,  # Tamanho do ícone ajustado para maior visibilidade
                                                color=b  # Cor do ícone
                                            ),
                                        
                                    ),
                                ]
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=142,
                                controls=[
                                    ft.Text(value='ADM', weight='bold', size=20, color=a2),
                                ]
                            ),
                            adm(id="151616", email="fdkfsgjkdfhjk", senha="dsgfhgdh"),
                            # Container com a palavra 'Notificações'
                            ft.Container(height=100),
                        

                            ft.ElevatedButton(
                                bgcolor=a2,
                                content=ft.Container(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.EXIT_TO_APP, color=ft.colors.WHITE),
                                            ft.Text("Sair da Conta", color=ft.colors.WHITE, weight="bold"),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=10,
                                    ),
                                    bgcolor=a2,
                                    width=1300,
                                    height=40,
                                ),
                                on_click=lambda e: update_content(sair_da_conta_adm(page)),
                            ),
                            ft.Container(height=100),
                        ]
                    ),
                ),
            ]
        )
    return confg()
