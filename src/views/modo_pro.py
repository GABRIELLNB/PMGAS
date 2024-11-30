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
def mod_pro(page: ft.Page):
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    # Função principal para montar a página de edição de perfil
    def pro():
        from configuracoes import configuracoes
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo principal verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza o conteúdo horizontalmente
            controls=[
                ft.Container(height=20),
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    width=1300,
                    height=830,  # Ajuste da altura do container principal
                    padding=ft.padding.all(10),
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,  # Alinha o título no centro
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            on_click=lambda e: update_content(configuracoes(page)),
                                            content=ft.Icon(
                                                ft.icons.ARROW_BACK_IOS,
                                                size=24,
                                                color=a2,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                           ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a imagem horizontalmente
                                controls=[
                                    ft.Image(
                                        src="imagem_branco.png",  # Caminho local ou URL da imagem
                                        width=500,
                                        height=200,
                                        fit=ft.ImageFit.CONTAIN,  # Mantém proporção
                                    )
                                ]
                            ),
                           ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a imagem horizontalmente
                                controls=[
                                    ft.Text(
                                        "Todo o minoramento que você quiser. \n"
                                        "Cadastrar áreas sem restrições ",
                                        size=24,
                                        color=a2,
                                        weight="bold",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ]
                           ),
                           ft.Container(height=20),
                           ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a imagem horizontalmente
                                controls=[
                                    ft.Text(
                                        "Com o PMGAS PRO você terá direto a consulta 24h de um profissional especializado, além conseguir cadastrar mais área ",
                                        size=22,
                                        color=a2,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ]
                           ),
                           ft.Container(height=20),
                           ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a imagem horizontalmente
                                controls=[
                                pro_button := ft.ElevatedButton(
                                        text='Assinar',
                                        color=ft.colors.WHITE,
                                        bgcolor=a2,
                                        width=1000,
                                        height=35,
                                    ),
                                ]
                           ),
                        ]
                    )
                )
            ]
        )
    return pro()
