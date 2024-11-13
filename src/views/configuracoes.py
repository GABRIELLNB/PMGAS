import flet as ft
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

from cadastros import cadastros
from graficos import graficos
from perfil import perfil

# Função para a barra de navegação
def navigation_bar(update_content, configuracoes_content, confg, cadastros_content, graficos_content, perfil_content):
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="Gráficos"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações"),
        ],
        on_change=lambda e: escolher_opcao(e, update_content, configuracoes_content, confg, cadastros_content, graficos_content, perfil_content)
    )

# Função para decidir qual conteúdo exibir
def escolher_opcao(e, update_content, configuracoes_content, confg, cadastros_content, graficos_content, perfil_content):
    opcao = e.control.selected_index
    
    
    
#!!!!!!FALTA COLOCAR A OPÇÃO DE SELECIONAR INICIO/MENU!!!!!!!!!!!!!


    if opcao == 1:
        update_content(cadastros_content())  # Exibe a página de cadastros
    elif opcao == 2:
        update_content(graficos_content())  # Exibe a página de gráficos
    elif opcao == 3:
        update_content(perfil_content())  # Exibe a página de perfil
    elif opcao == 4:
        update_content(configuracoes_content())  # Exibe a página de configurações

# Função de configuração
def configuracoes(page: ft.Page):
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Funções de conteúdo para cada seção
    def configuracoes_content():
        return configuracoes(page)  # Página de configurações

    def cadastros_content():
        return cadastros(page)  # Página de cadastros

    def graficos_content():
        return graficos(page)  # Página de gráficos

    def perfil_content():
        return perfil(page)  # Página de perfil

    def confg():
        # Corrigindo o uso de navigation_bar e a estrutura da coluna
        return ft.Column(
            controls=[  
                navigation_bar(update_content, configuracoes_content, confg, cadastros_content, graficos_content, perfil_content),  # Barra de navegação
                ft.Container(
                    alignment=ft.alignment.top_center,  # Alinha o container ao topo central
                    bgcolor=ft.colors.BLACK,
                    border_radius=10,
                    padding=ft.padding.all(10),
                    width=1000,  # Largura do container
                    height=500,
                )
            ]
        )

    return confg()
