import flet as ft
import sys
from pathlib import Path
import pandas as pd

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas
sys.path.append(str(root))

from edit_perfil import edit_perfil
from edit_area import edit_area
from areas_cadastradas import areas_cadastradas

caminho = "Contas - PMGAS.xlsx"

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"


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
        update_content(cadastros_content())  
    elif opcao == 2:
        update_content(graficos_content())  
    elif opcao == 3:
        update_content(perfil_content())  
    elif opcao == 4:
        update_content(configuracoes_content())  

# Função de configuração
def perfil(page: ft.Page):
    page.title = "PMGAS - Perfil"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Funções de conteúdo para cada seção
    def configuracoes_content():
        from configuracoes import configuracoes
        return configuracoes(page)  # Página de configurações

    def cadastros_content():
        from cadastros import cadastros
        return cadastros(page)  # Página de cadastros

    def graficos_content():
        from graficos import graficos
        return graficos(page)  # Página de gráficos

    def menu_content():
        from menu import menu
        return menu(page)

    # Função para exibir o conteúdo do perfil
    def perfil_content(nome, email, cpf, senha):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value=f"Nome: {nome}", weight="bold", size=20, color=a2),
                    ft.Text(value=f"Email: {email}", size=16, color=a2),
                    ft.Text(value=f"CPF: {cpf}", size=16, color=a2),
                    ft.Text(value=f"Senha: {'*' * len(senha)}", size=16, color=a2),
                ],
            ),
        )

    # Função principal para montar a página de perfil
    def perf():
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,  
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(height=5),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER, 
                    controls=[
                        ft.Image(
                            src="image.png", 
                            width=250,
                            height=50,
                            fit=ft.ImageFit.CONTAIN,  
                        )
                    ]
                ),
                navigation_bar(update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, menu_content),
                ft.Container(
                    alignment=ft.alignment.top_center,  
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    padding=ft.padding.all(10),
                    width=950, 
                    height=600,
                    content=ft.Column(
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,  
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,  
                                controls=[
                                    ft.Text(
                                        value='PERFIL',
                                        weight='bold',
                                        size=20,
                                        color=a2
                                    ),
                                ],
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=180,
                                controls=[
                                    ft.Container(
                                        bgcolor=a1,
                                        border_radius=50,  
                                        width=150,  
                                        height=150, 
                                        content=ft.Icon(
                                            ft.icons.PERSON_OUTLINED,  
                                            size=40,  
                                            color=b  
                                        ),
                                    ),
                                ]
                            ),
                            carregar_perfil(),  # Carrega o perfil
    
                            ft.ElevatedButton(
                                bgcolor=a2,
                                content=ft.Container(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                    on_click=lambda e: update_content(edit_perfil(page)),
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.EDIT_SQUARE, color=ft.colors.WHITE),
                                            ft.Text("Editar Perfil", color=ft.colors.WHITE, weight="bold"),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=10,
                                    ),
                                ),
                                width=1000,
                                height=40,
                            ),
                            ft.ElevatedButton(
                                bgcolor=a2,
                                content=ft.Container(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                    on_click=lambda e: update_content(areas_cadastradas(page)),
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.AREA_CHART, color=ft.colors.WHITE),
                                            ft.Text("Áreas Cadastradas", color=ft.colors.WHITE, weight="bold"),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=10,
                                    ),
                                ),
                                width=1000,
                                height=40,
                            ),
                            ft.Container(height=70),
                        ],
                    ),
                ),
            ],
        )

    # Função para carregar o perfil
    def carregar_perfil():
        from models.Bregister import buscar_perfil
        df = pd.read_excel(caminho)
        cpf_usuario = df['CPF'].iloc[0]  # Pega o primeiro CPF (ajustar conforme sua lógica)
        perfil = buscar_perfil(cpf_usuario)
    
        if perfil:
            return perfil_content(perfil["Nome"], perfil["Email"], perfil["CPF"], perfil["Senha"])
        else:
            return ft.Text("Perfil não encontrado!", size=20, color="red")

    # Atualiza o conteúdo com o perfil carregado
    update_content(carregar_perfil())
    return perf()
