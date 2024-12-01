import flet as ft
import sys
from pathlib import Path
import pandas as pd

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas
sys.path.append(str(root))

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"
caminho = "Contas - PMGAS - ADM.xlsx"
# Função de configuração
def edit_perfil_adm(page: ft.Page):
    page.title = "PMGAS - Editar Perfil"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página
        
    error_message = ft.Text(value="", color=ft.colors.RED)

    def update_error_message(msg, color):
        error_message.value = msg
        error_message.color = color
        page.update()

    def carregar_perfil():
        df = pd.read_excel(caminho)
        email_logado = page.session.get("user_email")
        perfil = df[df['Email'] == email_logado]
        if not perfil.empty:
            return perfil.iloc[0]
        else:
            return None

    def salvar_edicoes(nome, email, senha, caminho):
        df = pd.read_excel(caminho)
        usuario_index = df[df['Email'] == email].index
        if not usuario_index.empty:
            df.at[usuario_index[0], 'Nome'] = nome
            df.at[usuario_index[0], 'Email'] = email
            df.at[usuario_index[0], 'Senha'] = senha
            df.to_excel(caminho, index=False)
            return True
        else:
            return False

    # Função principal para montar a página de edição de perfil
    def perf():
        from configuracoes_ADM import configuracoes_adm
        
        perfil = carregar_perfil()
        if perfil is None:
            return ft.Text("Perfil não encontrado", color="red")
        
        nome_input = ft.TextField(value=perfil["Nome"], hint_text="Nome", color=a2, border=ft.InputBorder.NONE)
        email_input = ft.TextField(value=perfil["Email"], hint_text="E-mail",  color=a2,border=ft.InputBorder.NONE)
        senha_input = ft.TextField(value=perfil["Senha"], hint_text="Senha", password=True, can_reveal_password=True, color=a2, border=ft.InputBorder.NONE)

        def on_salvar_click(e):
            nome = nome_input.value
            email = email_input.value
            senha = senha_input.value

            # Validação básica
            if not nome or not email or not senha:
                update_error_message("Todos os campos são obrigatórios!", ft.colors.RED)
                return

            # Verificar se o email já está cadastrado
            df = pd.read_excel(caminho)
            if len(df[df['Email'] == email]) > 1:  # Duplicação de e-mail
                update_error_message("Este e-mail já está registrado.", ft.colors.RED)
                return

            if salvar_edicoes(nome, email, senha, caminho):
                update_error_message("Perfil atualizado com sucesso!", ft.colors.GREEN)
            else:
                update_error_message("Erro ao salvar perfil.", ft.colors.RED)
                
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo principal verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza o conteúdo horizontalmente
            controls=[
                ft.Container(height=20),
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    width=1000,
                    height=700,  # Ajuste da altura do container principal
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
                                height=510,  # Altura do container maior
                                padding=ft.padding.all(20),  # Espaçamento interno
                                border_radius=20,  # Bordas arredondadas
                                content=ft.Column(
                                     alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                    # Espaçamento superior
                                    ft.Container(height=20),
                                    
                                    ft.Row(
                                                    
                                                    controls=[  
                                                        ft.Container(width=15),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="Nome",
                                                                weight="bold",
                                                                size=15,
                                                                color=b,
                                                            ),
                                                        ),
                                                    ]
                                    ),
                                    ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        
                                                        ft.Container(
                                                            bgcolor=b,
                                                            width=560,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=0),
                                                            border_radius=15,
                                                            content=ft.Column(
                                                                controls=[nome_input]),
                                                        ),
                                                    ],
                                                ),
                                    
                                    ft.Divider(
                            height=1,
                            color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                            thickness=1
                        ),
                                                
                                                                                    ft.Row(
                                                    
                                                    controls=[  
                                                        ft.Container(width=15),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="Email",
                                                                weight="bold",
                                                                size=15,
                                                                color=b,
                                                            ),
                                                        ),
                                                    ]
                                    ),
                                                                                    
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            bgcolor=b,
                                                            width=560,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=0),
                                                            border_radius=15,
                                                            content=ft.Column(controls=[email_input]),
                                                        ),
                                                    ],
                                                ),
                                                ft.Divider(
                            height=1,
                            color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                            thickness=1
                        ),
                                              
                                                                                    ft.Row(
                                                    
                                                    controls=[  
                                                        ft.Container(width=15),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="Senha",
                                                                weight="bold",
                                                                size=15,
                                                                color=b,
                                                            ),
                                                        ),
                                                    ]
                                    ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            bgcolor=b,
                                                            width=560,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=0),
                                                            border_radius=15,
                                                            content=ft.Column(controls=[senha_input]),
                                                        ),
                                                    ],
                                                ),
                                                ft.Divider(
                            height=1,
                            color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                            thickness=1
                        ),
                                                ft.Container(height=20),
                                                error_message,
                                                ft.ElevatedButton(
                                                    text="Salvar",
                                                    bgcolor=b,
                                                    color=a2,
                                                    width=400,
                                                    height=40,
                                                    on_click=on_salvar_click,
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
