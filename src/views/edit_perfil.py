import flet as ft
import pandas as pd
from pathlib import Path

# Caminho do arquivo onde os dados do usuário são armazenados
caminho = "Contas - PMGAS.xlsx"

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"


# Função de configuração
def edit_perfil(page: ft.Page):
    page.title = "PMGAS - Editar Perfil"
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Função para carregar os dados do perfil
    def carregar_perfil():
        # Função para buscar o perfil no Excel, considerando que você já tem os dados do usuário carregados
        from models.Bregister import buscar_perfil
        df = pd.read_excel(caminho)
        cpf_usuario = df['CPF'].iloc[0]  # Supondo que você já tenha o CPF do usuário logado
        perfil = buscar_perfil(cpf_usuario)
    
        if perfil:
            return perfil
        else:
            return None  # Retorna None se o perfil não for encontrado
    
    # Função para salvar as edições
    def salvar_edicoes(nome, email, senha, cpf):
        df = pd.read_excel(caminho)
        
        # Encontre o índice do usuário a ser editado
        usuario_index = df[df['CPF'] == cpf].index
        
        if not usuario_index.empty:
            # Atualize os dados do usuário
            df.at[usuario_index[0], 'Nome'] = nome
            df.at[usuario_index[0], 'Email'] = email
            df.at[usuario_index[0], 'Senha'] = senha
            df.to_excel(caminho, index=False)  # Salva as alterações no arquivo Excel
            return True
        else:
            return False  # Retorna False se o usuário não for encontrado
    
    # Função principal para montar a página de edição de perfil
    def perf():
        perfil = carregar_perfil()  # Carrega os dados do perfil atual
        if perfil is None:
            return ft.Text("Perfil não encontrado", color="red")
        
        # Campos de entrada para editar os dados do perfil
        nome_input = ft.TextField(value=perfil["Nome"], hint_text="Nome", width=600, height=45)
        email_input = ft.TextField(value=perfil["Email"], hint_text="E-mail", width=600, height=45)
        senha_input = ft.TextField(value=perfil["Senha"], hint_text="Senha", password=True, can_reveal_password=True, width=600, height=45)
        cpf_input = ft.TextField(value=perfil["CPF"], hint_text="CPF", width=600, height=45, read_only=True)

        # Função de "Salvar" alterações
        def on_salvar_click(e):
            nome = nome_input.value
            email = email_input.value
            senha = senha_input.value
            cpf = cpf_input.value  # O CPF não será alterado

            # Salva as edições
            if salvar_edicoes(nome, email, senha, cpf):
                update_content(ft.Text("Perfil atualizado com sucesso!", color="green"))
            else:
                update_content(ft.Text("Erro ao salvar perfil.", color="red"))
        
        # Layout para a página de edição de perfil
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(height=20),
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    width=1300,
                    height=830,
                    padding=ft.padding.all(10),
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.ARROW_BACK_IOS, size=24, color=a2),
                                    ft.Text("Editar Perfil", weight="bold", size=20, color=a2),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10,
                            ),
                            ft.Divider(height=1, color=ft.colors.with_opacity(0.25, ft.colors.GREY)),
                            ft.Container(height=70),
                            ft.Row(
                                controls=[
                                    ft.Container(width=310),
                                    ft.Container(
                                        bgcolor=a2,
                                        width=650,
                                        height=450,
                                        padding=ft.padding.all(20),
                                        border_radius=20,
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[nome_input],
                                                ),
                                                ft.Container(height=10),
                                                ft.Row(
                                                    controls=[email_input],
                                                ),
                                                ft.Container(height=10),
                                                ft.Row(
                                                    controls=[senha_input],
                                                ),
                                                ft.Container(height=10),
                                                ft.Row(
                                                    controls=[cpf_input],
                                                ),
                                                ft.Container(height=40),
                                                ft.ElevatedButton(
                                                    text="Salvar",
                                                    bgcolor=b,
                                                    color=a2,
                                                    width=400,
                                                    height=40,
                                                    on_click=on_salvar_click,
                                                ),
                                            ]
                                        ),
                                    ),
                                ]
                            ),
                        ]
                    )
                ),
            ]
        )

    page.scroll = False
    return perf()

