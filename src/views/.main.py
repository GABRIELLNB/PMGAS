import flet as ft
from login import login
from register import register
from menu import menu
from cadastros import cadastros
from configuracoes import configuracoes
from graficos import graficos
from perfil import perfil
from ajuda import ajuda
from sobre import sobre
from sair import sair_da_conta
from edit_perfil import edit_perfil
from edit_area import edit_area
import sys
from pathlib import Path

# Configuração de caminho para importações relativas
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent
sys.path.append(str(root))

# Função principal
def main(page: ft.Page):
    AZ = "#04282D"
    page.title = "PMGAS"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = False
    page.window.maximized = True
    page.padding = ft.padding.all(0)
    page.bgcolor = AZ

    # Função genérica para troca de tela
    def trocar_tela(nova_tela):
        page.controls.clear()
        page.controls.append(nova_tela)
        page.update()
        
        # Funções para alternar entre telas
    def abrir_edit_area(e: ft.ControlEvent):
        trocar_tela(edit_area(page))
    
    # Funções para alternar entre telas
    def abrir_edit_perf(e: ft.ControlEvent):
        trocar_tela(edit_perfil(page))
        
    # Funções para alternar entre telas
    def abrir_sobre(e: ft.ControlEvent):
        trocar_tela(sobre(page))
            
    # Funções para alternar entre telas
    def abrir_ajuda(e: ft.ControlEvent):
        trocar_tela(ajuda(page))
        
    # Funções para alternar entre telas
    def abrir_sair(e: ft.ControlEvent):
        trocar_tela(sair_da_conta(page))
        
    # Funções para alternar entre telas
    def abrir_perfil(e: ft.ControlEvent):
        trocar_tela(perfil(page))

    def abrir_graficos(e: ft.ControlEvent):
        trocar_tela(graficos(page))

    def abrir_configuracoes(e: ft.ControlEvent):
        trocar_tela(configuracoes(page))

    def abrir_cadastros(e: ft.ControlEvent):
        trocar_tela(cadastros(page))

    def abrir_menu(e: ft.ControlEvent):
        trocar_tela(menu(page))

    def logar(e: ft.ControlEvent):
        trocar_tela(login(page, registar))

    def registar(e: ft.ControlEvent):
        trocar_tela(register(page, logar))

    # Exibe a tela inicial de login
    trocar_tela(login(page, registar))

# Executa o app
if __name__ == "__main__":
    ft.app(target=main)
