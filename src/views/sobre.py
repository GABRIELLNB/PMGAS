import flet as ft
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

a1 = "#7BD8D9",
a2 = "#04282D",
b = "#FFFFFF"

def sobre(page: ft.Page):
 
    def sbr(e):
        sobre_dialog = ft.AlertDialog(
        title=ft.Text("Sobre", size=20, weight="bold"),
        content=ft.Container(  
            width=1000,
            height=500,
            content=ft.Column(
                controls=[
                    ft.Text("Este projeto visa monitorar aterros sanitários em tempo real, "
                            "facilitando a gestão ambiental e a prevenção de riscos ecológicos. "
                            "Desenvolvido por estudantes de Engenharia de Computação."),
                    ft.ElevatedButton("Fechar", on_click=lambda e: sobre_dialog.close())
                ]
            )
        )
    )
    
        page.dialog = sobre_dialog  # Correctly set the dialog to the page object
        sobre_dialog.open = True  # Open the dialog
        page.update()  # Update the page to show the dialog