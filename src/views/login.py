import flet as ft
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

# Definição de cores
a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

from models.Blogin import check_email
from models.Blogin import check_senha
from menu import menu

def login(page: ft.Page, registar):
    error_message = ft.Text(value="", color=ft.colors.RED)

    # Função chamada quando o botão de login é pressionado
    def handle_login(event, email_input, senha_input, page):
        email = email_input.value
        senha = senha_input.value

        if not email or not senha:  # Verificação de campos vazios
            error_message.value = "Por favor, preencha todos os campos!"
            error_message.color = ft.colors.RED
        elif not check_email(email):  # Verificação se o email é válido
            error_message.value = "Email não encontrado!"
            error_message.color = ft.colors.RED
        elif not check_senha(email, senha):  # Verificação se a senha está correta
            error_message.value = "Senha incorreta!"
            error_message.color = ft.colors.RED
        else:
            page.clean()  # Função para limpar a página anterior
            page.add(menu(page))  # Ação para ir para a tela de menu

        # Atualiza a página para refletir as mudanças
        page.update()

    # Layout da tela de login
    login = ft.Column(
        controls=[
            ft.Text(value='PMGAS', weight='bold', size=30, color=ft.colors.WHITE),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                width=500,
                height=400,
                padding=ft.padding.all(10),
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Login',
                            weight='bold',
                            size=20,
                            color=ft.colors.BLACK
                        ),
                        ft.Divider(
                            height=1,
                            color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                            thickness=1
                        ),
                        email_input := ft.TextField(
                            hint_text='Digite seu email',
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
                            )
                        ),
                        senha_input := ft.TextField(
                            hint_text='Digite sua senha',
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
                            can_reveal_password=True
                        ),
                        login_button := ft.ElevatedButton(
                            text='Login',
                            color=ft.colors.WHITE,
                            bgcolor=a2,
                            width=500,
                            height=40,
                            on_click=lambda event: handle_login(event, email_input, senha_input, page)
                        ),
                        error_message,
                        ft.Row(
                            controls=[
                                ft.Checkbox(
                                    label="Manter Conectado",
                                    value=False,
                                    label_style=ft.TextStyle(
                                        size=14,  # Definindo o mesmo tamanho de fonte
                                        weight="bold",  # Definindo o mesmo peso de fonte
                                        color=ft.colors.with_opacity(0.9, a2)
                                    )
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton(
                                    text='Recuperar senha',
                                    style=ft.ButtonStyle(color=a2)
                                ),
                                ft.TextButton(
                                    style=ft.ButtonStyle(color=a2),
                                    text='Criar nova conta',
                                    on_click=registar  # Ação para ir para a tela de registro
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.EMAIL, icon_color=a2),
                                ft.IconButton(icon=ft.icons.TELEGRAM, icon_color=a2),
                                ft.IconButton(icon=ft.icons.FACEBOOK, icon_color=a2)
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

    return login
