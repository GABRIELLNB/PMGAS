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

from sair import sair_da_conta
from ajuda import ajuda
from sobre import sobre
from modo_pro import mod_pro

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
def configuracoes(page: ft.Page):
    
    page.title = "PMGAS - Configurações"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Funções de conteúdo para cada seção
    def configuracoes_content():
        return configuracoes(page)  # Página de configurações

    def cadastros_content():
        from cadastros import cadastros
        return cadastros(page)  # Página de cadastros

    def graficos_content():
        from graficos import graficos
        return graficos(page)  # Página de gráficos

    def perfil_content():
        from perfil import perfil_us
        return perfil_us(page)  # Página de perfil
    
    def menu_content():
        from menu import menu
        return menu(page)
    
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
                navigation_bar(update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, menu_content), 
                ft.Container(
                    alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    padding=ft.padding.all(10),
                    width=950,  # Largura do container
                    height=400,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a imagem horizontalmente
                                controls=[
                                    ft.Text(
                                            value='CONFIGURAÇÕES',
                                            weight='bold',
                                            size=20,
                                            color=a2

                                        ),
                                    ],
                                ),
                            ft.Container(height=20),
                            ft.ElevatedButton(
                                bgcolor=a2,
                                content=ft.Container(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.PAID, color=ft.colors.WHITE),
                                        ft.Text("Modo Pro", color=ft.colors.WHITE, weight="bold"),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                ),
                                bgcolor=a2,
                                width=1000,
                                height=40,
                                ),
                                on_click=lambda e: update_content(mod_pro(page)),
                            ),
                            ft.Container(height=5),
                            ft.Container(
                                bgcolor=a2,  # Cor de fundo
                                border_radius=18,  # Define borda arredondada para o container
                                width=950,  # Largura do container
                                height=45,  # Altura do container
                                padding=ft.padding.symmetric(horizontal=20, vertical=0),
                                border=ft.border.all(2, a2),
                                alignment=ft.alignment.center,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a coluna dentro do container
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Distribui espaço entre os elementos
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza verticalmente
                                            wrap=True,
                                            controls=[
                                                ft.Icon(
                                                    ft.icons.LOCATION_ON,  # Ícone de notificação
                                                    size=20,  # Tamanho do ícone
                                                    color=b  # Cor do ícone
                                                ),
                                                ft.Text(
                                                    value='Localização',
                                                    weight='bold',
                                                    size=15,
                                                    color=b
                                                ),
                                                ft.Container(width=650),
                                                ft.Switch(  # Coloca o switch para alternar a funcionalidade de notificações
                                                    value=False,  # Estado inicial do switch
                                                    on_change=lambda e: print(f"Localização: {'Ativado' if e.control.value else 'Desativado'}"),
                                                    active_color=a1,  # Cor do switch quando está ligado
                                                    inactive_track_color=b  # Cor do switch quando desligado
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ),
                            ft.Container(height=5),
                           ft.ElevatedButton(
                               bgcolor=a2,
                                content=ft.Container(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.INFO, color=ft.colors.WHITE),
                                        ft.Text("Sobre", color=ft.colors.WHITE, weight="bold"),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                ),
                                bgcolor=a2,
                                width=1000,
                                height=40,
                            ),
                                on_click=lambda e: update_content(sobre(page)),
                           ),
                           ft.Container(height=5),
                            ft.ElevatedButton(
                                bgcolor=a2,
                                content=ft.Container(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.QUESTION_MARK, color=ft.colors.WHITE),
                                        ft.Text("Ajuda", color=ft.colors.WHITE, weight="bold"),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=10,
                                ),
                                bgcolor=a2,
                                width=1000,
                                height=40,
                                ),
                                on_click=lambda e: update_content(ajuda(page)),
                            ),
                            ft.Container(height=5),
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
                                    width=1000,
                                    height=40,
                                ),
                                on_click=lambda e: update_content(sair_da_conta(page)),
                            ),
                        ]
                    ),
                ),
            ]
        )
    page.scroll = True
    return confg()
