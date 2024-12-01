import flet as ft
import sys
from pathlib import Path
import pandas as pd

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent
sys.path.append(str(root))

from edit_area import edit_area

caminho = "Areas Cadastradas - PMGAS.xlsx"

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"


# Função de configuração
def areas_cadastradas(page: ft.Page):
    from perfil import perfil
    page.title = "PMGAS - Perfis"

    def update_content(content):
        page.controls.clear()
        if isinstance(content, ft.Control):
            page.controls.append(content)
        else:
            page.controls.append(ft.Text("Erro ao carregar conteúdo.", color="red"))
        page.update()

    def carregar_areas_dados():
        """
        Carrega os dados de áreas a partir do arquivo Excel e busca detalhes no banco.
        """
        from models.Bcadastro_Areas import buscar_Area
        try:
            df = pd.read_excel(caminho)
            if 'CNPJ' not in df.columns:
                raise ValueError("CNPJ não encontrado no arquivo.")
            cnpj_area = df['CNPJ'].iloc[0]
            area = buscar_Area(cnpj_area)
            if area:
                return {
                    "nome": area.get("Nome da empresa", "N/A"),
                    "natureza": area.get("Natureza Juridica", "N/A"),
                    "porte": area.get("Porte", "N/A"),
                    "cnpj": area.get("CNPJ", "N/A"),
                    "cep": area.get("CEP", "N/A"),
                    "nome_empresa": area.get("Nome Proprietario", "N/A"),
                }
            else:
                raise ValueError("Área não encontrada!")
        except Exception as e:
            return {
                "nome": "Erro",
                "natureza": "N/A",
                "porte": "N/A",
                "cnpj": "N/A",
                "cep": "N/A",
                "nome_empresa": str(e),
            }

    def area_layout(nome, natureza, porte, cnpj, cep, nome_empresa):
        """
        Retorna o layout da área com as informações fornecidas.
        """
        return ft.Column(
            controls=[
                ft.Text(value=f"Nome: {nome}", size=20),
                ft.Text(value=f"Natureza Jurídica: {natureza}", size=16),
                ft.Text(value=f"Porte da Empresa: {porte}", size=16),
                ft.Text(value=f"CNPJ: {cnpj}", size=16),
                ft.Text(value=f"CEP: {cep}", size=16),
                ft.Text(value=f"Nome do Proprietário: {nome_empresa}", size=16),
            ]
        )

    def area_page(nome, natureza, porte, cnpj, cep, nome_empresa):
        """
        Monta a página principal de áreas cadastradas.
        """
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(height=5),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                on_click=lambda e: update_content(perfil(page)),
                                content=ft.Icon(
                                    ft.icons.ARROW_BACK_IOS,
                                    size=24,
                                    color=b,
                                ),
                            ),
                            ft.Text(
                                value="Áreas Cadastradas",
                                weight="bold",
                                size=20,
                                color=b,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ),
                ft.Divider(height=1, color=ft.colors.with_opacity(0.25, ft.colors.GREY), thickness=1),
                ft.Container(height=10),
                area_layout(nome, natureza, porte, cnpj, cep, nome_empresa),
            ],
        )

    # Carregar os dados e renderizar a página
    area_dados = carregar_areas_dados()
    update_content(area_page(**area_dados))

    return page
