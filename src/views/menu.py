import flet as ft
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

from graficostempS import graficostempS

a1 = "#7BD8D9",
a2 = "#04282D",
b = "#FFFFFF"

# Cria a barra de navegação personalizada
def navigation_bar(update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, inicio_content):
    return ft.NavigationBar(
        bgcolor=b,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="Gráficos"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações"),
        ],
        on_change=lambda e: escolher_opcao(e, update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, inicio_content)
    )

def escolher_opcao(e, update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, inicio_content):
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
    page.title = "PMGAS - Menu"
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    def menu_content():
        return inicio(page)

    def configuracoes_content():
        from configuracoes import configuracoes
        return configuracoes(page)

    def cadastros_content():
        from cadastros import cadastros
        return cadastros(page)

    def graficos_content():
        from graficos import graficos
        return graficos(page)

    def perfil_content():
        from perfil import perfil
        return perfil(page)

    # Função para abrir a página flutuante de gráficos
    def abrir_graficosTP():
        graficos_dialog = ft.AlertDialog(
            title=ft.Text("Informações sobre Gráficos", size=20, weight="bold"),
            content=ft.Container(  
                width=1000,
                height=500,
                content=ft.Column(
                    controls=[
                        ft.Text("Aqui vão as informações detalhadas sobre os gráficos."),
                        ft.ElevatedButton("Fechar", on_click=lambda e: close_grf_dialog(page))
                    ]
                )
            )
        )
        page.dialog = graficos_dialog  # Definindo o Dialog na página
        graficos_dialog.open = True  # Abrindo o Dialog
        page.update()  # Atualizando a página para mostrar o Dialog

    # Função para abrir a página flutuante de Aterros Ronald
    def abrir_GSgraficos():
        aterros_dialog = ft.AlertDialog(
            title=ft.Text("Informações sobre Aterros Ronald", size=20, weight="bold"),
            content=ft.Container(  
                width=1000,
                height=500,
                content=ft.Column(
                    controls=[
                        ft.Text("Aqui vão as informações detalhadas sobre os Aterros Ronald."),
                        ft.ElevatedButton("Fechar", on_click=lambda e: close_grf_dialog(page))
                    ]
                )
            )
        )
        
        page.dialog = aterros_dialog  # Definindo o Dialog na página
        aterros_dialog.open = True  # Abrindo o Dialog
        page.update()  # Atualizando a página para mostrar o Dialog
    
    def close_grf_dialog(page):
        page.dialog.open = False  # Fecha o diálogo
        page.update()  # Atualiza a página

    # Após fechar, reexibe a página de configurações
        update_content(menu_content())
        
    # Define o conteúdo da página inicial
    def inicio():
        return ft.Column(
            controls=[
                ft.Container(height=5),
                ft.Image(
                    src="image.png",  # Caminho local ou URL da imagem
                    width=250,  # Largura da imagem
                    height=50,  # Altura da imagem
                    fit=ft.ImageFit.CONTAIN,  # Ajuste da imagem
                ),
                navigation_bar(update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, menu_content),
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
                            on_click=lambda e: abrir_graficosTP()  # Abre o Dialog de Gráficos
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
                            on_click=lambda e: abrir_GSgraficos()  # Abre o Dialog de Aterros Ronald
                        )
                    ]
                )
            ],

        )

    # Adiciona o conteúdo inicial à página
    page.scroll = True
    return inicio()  # Inicia com o conteúdo da página inicial
