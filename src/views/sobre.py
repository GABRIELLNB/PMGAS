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

def sobre(page: ft.Page):
    
    
    from configuracoes import configuracoes
    sobre_dialog = ft.AlertDialog(
        title=ft.Text("Sobre o Projeto", weight="bold", size=20, text_align=ft.TextAlign.CENTER),
        content=ft.Container(
            width=500,
            height=200,
            padding=ft.padding.all(10),
            content=ft.Text(
                "Este projeto visa monitorar aterros sanitários em tempo real, "
                "facilitando a gestão ambiental e a prevenção de riscos ecológicos. "
                "Desenvolvido por estudantes de Engenharia de Computação.",
                size=16,
                color=a2,
                text_align=ft.TextAlign.JUSTIFY,
            ),
        ),
        actions=[
            ft.ElevatedButton(
                "Fechar",
                on_click=lambda e: close_sobre_dialog(page, sobre_dialog),  # Passa o diálogo para fechar
                bgcolor=a1,
                color=b,
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,  # Alinha o botão de ação à direita
    )
    
    page.dialog = sobre_dialog  # Vincula o diálogo à página
    sobre_dialog.open = True  # Abre o diálogo
    page.update()  # Atualiza a página para exibir o diálogo

    def close_sobre_dialog(page, sobre_dialog):
    # Fecha o diálogo
        sobre_dialog.open = False
        page.update()  # Atualiza a página para refletir o fechamento do diálogo

    # Após fechar, reexibe a página de configurações
    from configuracoes import configuracoes
    update_content(page, configuracoes(page))

    def update_content(page, content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página
