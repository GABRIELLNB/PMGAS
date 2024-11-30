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

# Função de configuração
def edit_perfil_adm(page: ft.Page):
    page.title = "PMGAS - Editar Perfil"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Função principal para montar a página de edição de perfil
    def perf():
        from configuracoes_ADM import configuracoes_adm
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo principal verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza o conteúdo horizontalmente
            controls=[
                ft.Container(height=20),
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    width=1000,
                    height=600,  # Ajuste da altura do container principal
                    padding=ft.padding.all(10),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,  # Alinha o título no centro
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            on_click=lambda e: update_content(configuracoes_adm(page)),
                                            content=ft.Icon(
                                                ft.icons.ARROW_BACK_IOS,
                                                size=24,
                                                color=a2,
                                            ),
                                        ),
                                        ft.Container(width=350),
                                        ft.Icon(ft.icons.EDIT_SQUARE, size=24, color=ft.colors.BLACK),
                                        ft.Text(
                                            value="Editar Perfil",
                                            weight="bold",
                                            size=20,
                                            color=a2,
                                        ),
                                        ft.Container(width=400),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,  # Alinha o conteúdo da Row
                                    spacing=10,  # Espaço entre os elementos da Row
                                ),
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                                thickness=1,
                            ),
                            ft.Container(height=70),
                            ft.Row(
                            controls=[   
                                ft.Container(width=150),                         
                                ft.Container(
                                bgcolor=a2,  # Cor de fundo do container maior
                                width=650,  # Largura do container maior
                                height=300,  # Altura do container maior
                                padding=ft.padding.all(20),  # Espaçamento interno
                                border_radius=20,  # Bordas arredondadas
                                content=ft.Column(
                                    controls=[
                                    # Espaçamento superior
                                    ft.Container(height=20),
                                    
                                    # Campos de entrada (Email, Nome, Senha, CPF)
                                    ft.Row(
                                        controls=[
                                            
                                            ft.Container(
                                                bgcolor=b,
                                                padding=ft.padding.symmetric(horizontal=20, vertical=0),
                                                border_radius=10,
                                                width=600,
                                                height=45,  # Altura ajustada para comportar o campo de texto
                                                alignment=ft.alignment.center,
                                                content=ft.Column(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            hint_text="Email",
                                                            prefix_icon=ft.icons.EMAIL,
                                                            text_vertical_align=-0.30,
                                                            border=ft.InputBorder.UNDERLINE,
                                                            border_width=2,
                                                            border_color=a2,
                                                            hint_style=ft.TextStyle(
                                                                size=14,
                                                                weight="bold",
                                                                color=ft.colors.with_opacity(0.4, a2),
                                                            ),
                                                            text_style=ft.TextStyle(
                                                                size=14,
                                                                weight="bold",
                                                                color=ft.colors.with_opacity(0.9, a2),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    ft.Container(height=10),

                                    # Campo Senha
                                    ft.Row(
                                        controls=[
                                            
                                            ft.Container(
                                                bgcolor=b,
                                                padding=ft.padding.symmetric(horizontal=20, vertical=0),
                                                border_radius=10,
                                                width=600,
                                                height=45,
                                                alignment=ft.alignment.center,
                                                content=ft.Column(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.TextField(
                                                            hint_text="Senha",
                                                            prefix_icon=ft.icons.LOCK,
                                                            text_vertical_align=-0.30,
                                                            border=ft.InputBorder.UNDERLINE,
                                                            border_width=2,
                                                            border_color=b,
                                                            hint_style=ft.TextStyle(
                                                                size=14,
                                                                weight="bold",
                                                                color=ft.colors.with_opacity(0.4, a2),
                                                            ),
                                                            text_style=ft.TextStyle(
                                                                size=14,
                                                                weight="bold",
                                                                color=ft.colors.with_opacity(0.9, a2),
                                                            ),
                                                            password=True,
                                                            can_reveal_password=True,
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    ft.Container(height=40),

                                    # Botão Registrar
                                    ft.Row(
                                        controls=[
                                            ft.Container(width=78),
                                            ft.ElevatedButton(
                                                text='Salvar',
                                                color=a2,
                                                bgcolor=b,
                                                width=400,
                                                height=40,
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            ),
                        ],
                    ),
                            
                        ],
                    ),
                ),
            ],
        )
    page.scroll = False
    return perf()
