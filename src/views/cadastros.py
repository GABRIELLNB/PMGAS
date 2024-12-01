import flet as ft
import sys
from pathlib import Path

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

from models.Bcadastro_Areas import salvar_dados_Areas
# Definição de cores
a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

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
def cadastros(page: ft.Page):
    
    page.title = "PMGAS - Cadastros"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página
        
    Nome_Proprietario_input = None
    cnpj_input = None 
    cep_input = None 
    nome_empr_input = None
    nature_input = None
    porte_input = None
    
    def on_Nome_Proprietario_change(e):
        nonlocal Nome_Proprietario_input
        Nome_Proprietario_input = e.control.value
        
    def on_cnpj_change(e):
        nonlocal cnpj_input
        cnpj_input = e.control.value
    
    def on_cep_change(e):
        nonlocal  cep_input
        cep_input = e.control.value
        
    def on_nome_empr_change(e):
        nonlocal nome_empr_input
        nome_empr_input = e.control.value
        
    def on_nature_change(e):
        nonlocal nature_input
        nature_input = e.control.value
        
    def on_porte_change(e):
        nonlocal porte_input
        porte_input = e.control.value
        
    error_message = ft.Text(value="", color=ft.colors.RED)
    
    def update_error_message_Areas(msg):
        error_message.value = msg
        error_message.color = ft.colors.RED
        page.update()
        
        
    

    # Função para retornar a página de perfil
    def perfil_content():
        from perfil import perfil_us
        return perfil_us(page)

    # Funções de conteúdo para cada seção
    def configuracoes_content():
        from configuracoes import configuracoes
        return configuracoes(page)  # Página de configurações

    def cadastros_content():
        return cadastros(page)  # Página de cadastros

    def graficos_content():
        from graficos import graficos
        return graficos(page)  # Página de gráficos

    def menu_content():
        from menu import menu
        return menu(page)

    # Função principal para montar a página de cadastros
    def cad():
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
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    width=1000,
                    height=625,  # Aumentei a altura para acomodar mais campos
                    padding=ft.padding.all(10),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,  # Alinha o título no centro
                                content=ft.Row(
                                controls=[
                                ft.Icon(ft.icons.EDIT_DOCUMENT, size=24, color=ft.colors.BLACK),  # Adiciona o ícone
                                ft.Text(
                                    value='Cadastro de Área',
                                    weight='bold',
                                    size=20,
                                    color=ft.colors.BLACK
                                ),
                            ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Alinha o conteúdo da Row
                        spacing=10,  # Espaço entre o ícone e o texto
                        ),
                    ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                                thickness=1
                            ),
                            # Campos de entrada para o Cadastro
                            ft.Container(
                                bgcolor=a2,
                                padding=ft.padding.all(6),
                                border_radius=10,
                                width=1000,
                                height=200,
                                content=ft.Column(
                                    controls=[
                                        nome_input := ft.TextField(
                                            hint_text='Nome do Proprietário',
                                            prefix_icon=ft.icons.PERSON,
                                            text_vertical_align=-0.15,
                                            border=ft.InputBorder.UNDERLINE,
                                            border_width=2,
                                            border_color=b,
                                            hint_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.4, b)
                                            ),
                                            text_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.9, b)
                                            ),
                                            on_change=on_Nome_Proprietario_change
                                        ),
                                        CNPJ_input := ft.TextField(
                                            hint_text='CNPJ',
                                            prefix_icon=ft.icons.CONTACT_PAGE,
                                            text_vertical_align=-0.15,
                                            border=ft.InputBorder.UNDERLINE,
                                            border_width=2,
                                            border_color=b,
                                            hint_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.4, b)
                                            ),
                                            text_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.9, b)
                                            ),
                                            on_change=on_cnpj_change
                                        ),
                                        CEP_input := ft.TextField(
                                            hint_text='CEP',
                                            prefix_icon=ft.icons.LOCATION_CITY,
                                            text_vertical_align=-0.15,
                                            border=ft.InputBorder.UNDERLINE,
                                            border_width=1,
                                            border_color=b,
                                            hint_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.4, b)
                                            ),
                                            text_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.9, b)
                                            ),
                                            on_change=on_cep_change
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(height=10),
                            # Dados da empresa
                            ft.Container(
                                alignment=ft.alignment.top_left,  # Alinha o texto no canto superior esquerdo
                                content=ft.Text(value='DADOS DA EMPRESA', weight='bold', size=20, color=a2)
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.35, ft.colors.GREY),
                                thickness=1
                            ),
                            ft.Container(
                                bgcolor=a2,
                                padding=ft.padding.all(6),
                                border_radius=10,
                                width=1000,
                                height=200,
                                content=ft.Column(
                                    controls=[
                                        nome_empresa_input := ft.TextField(
                                            hint_text='Nome da Empresa',
                                            prefix_icon=ft.icons.BUSINESS,
                                            text_vertical_align=-0.15,
                                            border=ft.InputBorder.UNDERLINE,
                                            border_width=2,
                                            border_color=b,
                                            hint_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.4, b)
                                            ),
                                            text_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.9, b)
                                            ),
                                            on_change=on_nome_empr_change
                                        ),
                                        Natureza_juridico_input := ft.TextField(
                                            hint_text='Natureza Jurídico',
                                            prefix_icon=ft.icons.BUSINESS,
                                            text_vertical_align=-0.15,
                                            border=ft.InputBorder.UNDERLINE,
                                            border_width=2,
                                            border_color=b,
                                            hint_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.4, b)
                                            ),
                                            text_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.9, b)
                                            ),
                                            on_change=on_nature_change
                                        ),
                                        porte_empresa_input := ft.TextField(
                                            hint_text='Porte da Empresa',
                                            prefix_icon=ft.icons.BUSINESS,
                                            text_vertical_align=-0.15,
                                            border=ft.InputBorder.UNDERLINE,
                                            border_width=2,
                                            border_color=b,
                                            hint_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.4, b)
                                            ),
                                            text_style=ft.TextStyle(
                                                size=14,
                                                weight='bold',
                                                color=ft.colors.with_opacity(0.9, b)
                                            ),
                                            on_change=on_porte_change
                                        ),
                                        
                                    ]
                                ),
                            ),
                            error_message,
                            # Botão de Cadastro
                            cad_button := ft.ElevatedButton(
                                text='Cadastrar',
                                color=ft.colors.WHITE,
                                bgcolor=a2,
                                width=1000,
                                height=35,
                                on_click=lambda e: salvar_dados_Areas(
                                    Nome_Proprietario_input, cnpj_input, cep_input, nome_empr_input, nature_input, porte_input, update_error_message_Areas
                                )
                            ),
                        ],
                    ),
                ),
            ],
        )
        
    return cad()
