import flet as ft
from login import login
from register import register
from menu import menu
from cadastros import cadastros
from configuracoes import configuracoes
from graficos import graficos
from perfil import perfil
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root =  file.parent.parent  # Importações relativas


sys.path.append(str(root))



def main(page: ft.Page):
    AZ = '#04282D'
    page.title = 'PMGAS'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = False
    page.window.maximized = True
    page.padding = ft.padding.all(0)
    page.bgcolor = AZ

# Função para alternar para a tela de cadastros
    def abrir_perfil(e: ft.ControlEvent):
        page.controls.clear()
        page.add(perfil(page))
        
# Função para alternar para a tela de graficos
    def abrir_graficos(e: ft.ControlEvent):
        page.controls.clear()
        page.add(graficos(page))
        
# Função para alternar para a tela de configurações
    def abrir_configuracoes(e: ft.ControlEvent):
        page.controls.clear()
        page.add(configuracoes(page))
        
# Função para alternar para a tela de cadastros
    def abrir_cadastros(e: ft.ControlEvent):
        page.controls.clear()
        page.add(cadastros(page))
        
    # Função para alternar para a tela de menu
    def abrir_menu(e: ft.ControlEvent):
        page.controls.clear()
        page.add(menu(page))
        
    # Função para alternar para a tela de login
    def logar(e: ft.ControlEvent):
        page.controls.clear()
        page.add(login(page, registar))

    # Função para alternar para a tela de registro
    def registar(e: ft.ControlEvent):
        page.controls.clear()
        page.add(register(page, logar))

    # Começa com a tela de login
    page.add(login(page, registar))

# Executa o app
if __name__ == '__main__':
    ft.app(target=main)
