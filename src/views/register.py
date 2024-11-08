import flet as ft
    
def register(page: ft.Page, logar):
    AZ = '#041955'
    # Layout da tela de registro
    register = ft.Column(
        controls=[
               ft.Text(
                value='PMGAS',
                weight='bold',
                size=30,
                color=ft.colors.WHITE,
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                width=400,
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
                            border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                            hint_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                            ),
                            text_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                            )
                        ),
                        ft.TextField(
                            hint_text='Nome',
                            prefix_icon=ft.icons.PERSON,
                            text_vertical_align=-0.30,
                            border=ft.InputBorder.UNDERLINE,
                            border_width=2,
                            border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                            hint_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                            ),
                            text_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                            )
                        ),
                        ft.TextField(
                            hint_text='Senha',
                            prefix_icon=ft.icons.LOCK,
                            text_vertical_align=-0.30,
                            border=ft.InputBorder.UNDERLINE,
                            border_width=2,
                            border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                            hint_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                            ),
                            text_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                            ),
                            password=True,
                            can_reveal_password=True
                        ),
                        ft.TextField(
                            hint_text='CPF (apenas números)',
                            max_length=11,
                            prefix_icon=ft.icons.CONTACT_PAGE,
                            text_vertical_align=-0.30,
                            border=ft.InputBorder.UNDERLINE,
                            border_width=2,
                            border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                            hint_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                            ),
                            text_style=ft.TextStyle(
                                size=14,
                                weight='bold',
                                color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                            )
                        ),
                        # Campos adicionais podem ser adicionados aqui...
                        ft.ElevatedButton(
                            text='Registrar',
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE_GREY_800,
                            width=400,
                            height=40
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton(
                                    style=ft.ButtonStyle(color=ft.colors.BLUE_GREY_800),
                                    text='Já tenho uma conta',
                                    on_click=logar  # Ação para ir para a tela de login
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
