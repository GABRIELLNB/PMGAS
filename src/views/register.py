import flet as ft
import sys
from pathlib import Path

# Configuração de caminho para importações relativas
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Caminho relativo

sys.path.append(str(root))

from models.Bregister import salvar_dados
# Definição de cores
a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

def register(page: ft.Page):
    from login import login
    page.title = "PMGAS - Cadastro"
    


    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página
        
    email_input = ""
    nome_input = ""
    cpf_input = ""
    senha_input = ""
    
    def on_email_change(e):
        nonlocal email_input
        email_input = e.control.value
    
    def on_nome_change(e):
        nonlocal nome_input
        nome_input = e.control.value
    
    def on_senha_change(e):
        nonlocal senha_input
        senha_input = e.control.value
    
    def on_cpf_change(e):
        nonlocal cpf_input
        cpf_input = e.control.value
        
    error_message = ft.Text(value="", color=ft.colors.RED)

    def update_error_message(msg):
        error_message.value = msg
        error_message.color = ft.colors.RED
        page.update()
        
    # Layout da tela de registro
    register = ft.Column(
        controls=[
               ft.Image(
                    src="image.png",  # Caminho local ou URL da imagem
                    width=300,  # Largura da imagem
                    height=100,  # Altura da imagem
                    fit=ft.ImageFit.CONTAIN,  # Ajuste da imagem
                ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                height=480,
                width=500,
                padding=ft.padding.all(10),
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Cadastro',
                            weight='bold',
                            size=20,
                            color=ft.colors.BLACK
                        ),
                        ft.Divider(
                            height=1,
                            color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                            thickness=1
                        ),
                        ft.TextField(
                            hint_text='Email',
                            prefix_icon=ft.icons.EMAIL,
                            text_vertical_align=-0.30,
                            border=ft.InputBorder.UNDERLINE,
                            border_width=2,
                            border_color=ft.colors.with_opacity(0.4, a2),
                            hint_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.4, a2)
                            ),
                            text_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.9, a2)
                            ),
                            on_change=on_email_change
                        ),
                        ft.TextField(
                            hint_text='Nome',
                            prefix_icon=ft.icons.PERSON,
                            text_vertical_align=-0.30,
                            border=ft.InputBorder.UNDERLINE,
                            border_width=2,
                            border_color=ft.colors.with_opacity(0.4, a2),
                            hint_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.4, a2)
                            ),
                            text_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.9, a2)
                            ),
                            on_change=on_nome_change,
                        ),
                        ft.TextField(
                            hint_text='Senha',
                            prefix_icon=ft.icons.LOCK,
                            text_vertical_align=-0.30,
                            border=ft.InputBorder.UNDERLINE,
                            border_width=2,
                            border_color=ft.colors.with_opacity(0.4, a2),
                            hint_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.4, a2)
                            ),
                            text_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.9, a2)
                            ),
                            password=True,
                            can_reveal_password=True,
                            on_change=on_senha_change
                        ),
                        ft.TextField(
                            hint_text='CPF (apenas números)',
                            max_length=11,
                            prefix_icon=(ft.icons.CONTACT_PAGE),
                            text_vertical_align=-0.30,
                            border=ft.InputBorder.UNDERLINE,
                            border_width=2,
                            border_color=ft.colors.with_opacity(0.4, a2),
                            hint_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.4, a2)
                            ),
                            text_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.9, a2)
                            ),
                            on_change=on_cpf_change
                        ),
                        error_message,
                        ft.ElevatedButton(
                            text='Registrar',
                            color=ft.colors.WHITE,
                            bgcolor=a2,
                            width=500,
                            height=40,
                            on_click=lambda e: salvar_dados(
                                email_input, nome_input, cpf_input, senha_input, update_error_message
                            ) 
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton(
                                    style=ft.ButtonStyle(color=a2),
                                    text='Já tenho uma conta',
                                    on_click=lambda e: update_content(login(page))  # Ação para ir para a tela de login
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    return register
