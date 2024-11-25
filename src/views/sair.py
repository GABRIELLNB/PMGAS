import flet as ft
import sys
from pathlib import Path

# Configuração de caminho para importações relativas
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Caminho relativo
sys.path.append(str(root))


# Definição de cores
a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

def sair_da_conta(page: ft.Page):
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página
        
    from configuracoes import configuracoes
    from login import login
    # Diálogo de confirmação
    sair_dialog = ft.AlertDialog(
        title=ft.Text("DESEJA SAIR DA SUA CONTA?", weight="bold", size=20, text_align=ft.TextAlign.CENTER,),
        content=ft.Container(
            width=500,
            height=200,
            padding=ft.padding.all(10),
            alignment=ft.alignment.center,  # Certifique-se de usar o Alignment correto
            content=ft.Column(
                alignment=ft.alignment.center,
                controls=[
                    ft.Text(
                        "Tem certeza de que deseja se desconectar?",
                        size=16,
                        color=a2,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Divider(
                        height=10,
                        color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                        thickness=1
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            ft.ElevatedButton(
                                "Sim",
                                on_click=lambda e: print,  # Aqui você pode adicionar a lógica para sair da conta
                                bgcolor=a1,
                                color=b,
                            ),
                            ft.ElevatedButton(
                                "Cancelar",
                                on_click=lambda e: close_sair_dialog(page, sair_dialog),  # Fecha o diálogo
                                bgcolor=a1,
                                color=b,
                            ),
                        ]
                    ),
                ]
            ),
        ),
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
       
    page.dialog = sair_dialog  # Vincula o diálogo à página
    sair_dialog.open = True  # Abre o diálogo
    page.update()  # Atualiza a página para exibir o diálogo

    def close_sair_dialog(page, sair_dialog):
        # Fecha o diálogo
        sair_dialog.open = False
        page.update()  # Atualiza a página para refletir o fechamento do diálogo

    # Após fechar, reexibe a página de configurações
    from configuracoes import configuracoes
    update_content(page, configuracoes(page))

    def update_content(page, content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página
