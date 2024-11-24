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



    # Função principal para montar a página de perfil
    def perf():
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo principal verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                navigation_bar(update_content, configuracoes_content, cadastros_content, perfil_content),
                ft.Container(height=20),
                ft.Container(
                    alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    padding=ft.padding.all(10),
                    width=1000,  # Largura do container
                    height=630,
                    content=ft.Column(
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo da coluna
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.END,
                                spacing=180,
                                controls=[
                                    ft.Container(
                                        alignment=ft.alignment.top_right,
                                        bgcolor=b,
                                        border_radius=50,  # Borda arredondada para formar o círculo
                                        width=40,  # Largura do círculo
                                        height=40,  # Altura do círculo
                                        on_click=lambda e: update_content(edit_perfil(page)),
                                        content=ft.Icon(
                                            ft.icons.EDIT_SQUARE,  # Ícone de notificação
                                                size=40,  # Tamanho do ícone ajustado para maior visibilidade
                                                color=a1  # Cor do ícone
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
                                        width=150,  # Largura do círculo
                                        height=150,  # Altura do círculo
                                        on_click=lambda e: print("Círculo com ícone de nuvem clicado!"),
                                        content=ft.Icon(
                                            ft.icons.PERSON_OUTLINED,  # Ícone de notificação
                                                size=40,  # Tamanho do ícone ajustado para maior visibilidade
                                                color=b  # Cor do ícone
                                        ),  
                                    ),
                                ]
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                
                                controls=[
                                    ft.Text(value='Usuario', weight='bold', size=20, color=a2),
                                ]
                            ),
                            ft.Container(height=20),
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
                                            ft.icons.NOTIFICATIONS_OUTLINED,  # Ícone de notificação
                                                size=40,  # Tamanho do ícone ajustado para maior visibilidade
                                                color=b  # Cor do ícone
                                        ),  
                                    ),
                                    ft.Container(
                                        bgcolor=a1,
                                        border_radius=50,  # Borda arredondada para formar o círculo
                                        width=100,  # Largura do círculo
                                        height=100,  # Altura do círculo
                                        on_click=lambda e: update_content(edit_area(page)),
                                        content=ft.Icon(
                                            ft.icons.EDIT_DOCUMENT,  # Ícone de notificação
                                                size=40,  # Tamanho do ícone ajustado para maior visibilidade
                                                color=b  # Cor do ícone
                                        ),  
                                    ),
                                ]
                            ),
                            ft.Container(height=20),
                            ft.ElevatedButton(
                                bgcolor=a2,
                                content=ft.Container(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.AREA_CHART, color=ft.colors.WHITE),
                                        ft.Text("Áreas Cadastradas", color=ft.colors.WHITE, weight="bold"),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                ),
                                bgcolor=a2,
                                width=1000,
                                height=40,
                                ),
                            ),
                            ft.Container(height=70),
                        ],
                    ),
                ),
            ],
        )
    return perf()