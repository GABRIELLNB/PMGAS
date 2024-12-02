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


    
a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

from models.areas import ler_perfis_excel
# Função de configuração
def areas_cadastradas(page: ft.Page):
    from perfil import perfil_us
    page.title = "PMGAS - Perfis"
    
    caminho = "Areas Cadastradas - PMGAS.xlsx"
    area = ler_perfis_excel(caminho)
    
    def update_content(content):
        if isinstance(content, ft.Control):
            page.controls.clear()
            page.controls.append(content)
            page.update()  # Atualiza a página com o novo conteúdo
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
        return ft.Container(
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        width=1000,
        height=350,
        padding=ft.padding.all(10),
        content=ft.Column(
            controls=[
                ft.Container(
                    bgcolor=b,
                    padding=ft.padding.all(10),
                    border_radius=10,
                    width=1300,
                    height=300,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.PERSON, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Nome: {nome}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.BUSINESS, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Natureza Juridica: : {natureza}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.BUSINESS, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Porte da Empresa:: {porte}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.CONTACT_PAGE, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"CNPJ: {cnpj}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.LOCATION_CITY, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"CEP: {cep}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Icon(ft.icons.LOCATION_CITY, color=ft.colors.with_opacity(0.9, a2), size=20),
                                    ft.Text(
                                        value=f"Nome da empresa: {nome_empresa}",
                                        style=ft.TextStyle(size=16, weight="bold", color=ft.colors.with_opacity(0.9, a2)),
                                    ),
                                ],
                            ),
                            ft.Divider(
                                height=1,
                                color=ft.colors.with_opacity(0.25, a2),
                                thickness=1,
                            ),
                            ft.Container(
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=10,
                                    controls=[
                                        ft.Container(
                                            content=ft.Icon(
                                                ft.icons.EDIT_SQUARE,
                                                size=24,
                                                color=a2,
                                            ),
                                            on_click=lambda e: update_content(edit_area(page))
                                            
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
                ft.Container(height=10),
            ],
        ),
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
                    alignment=ft.alignment.center,  # Alinha o título no centro
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        on_click=lambda e: 
                                            update_content(perfil_us(page)),
                                        content=ft.Icon(
                                            ft.icons.ARROW_BACK_IOS,
                                            size=24,
                                            color=b,
                                        ),
                                    ),
                                    ft.Container(width=500),

                                    ft.Text(
                                        value="Áreas Cadastradas",
                                        weight="bold",
                                        size=20,
                                        color=b,
                                    ),
                                    ft.Container(width=550),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,  # Alinha o conteúdo da Row
                                spacing=10,  # Espaço entre os elementos da Row
                            ),
                        ],
                    ),
                ),
                
                ft.Divider(
                    height=1,
                    color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                    thickness=1,
                ),
                ft.Container(height=10),
                *[area_layout(p["Nome Proprietario"], p["CNPJ"], p["CEP"], p["Nome da empresa"], p["Natureza Juridica"], p["Porte"]) for p in area],  # Exibe todos os perfis
            ]
        )

    # Carregar os dados e renderizar a página
    area_dados = carregar_areas_dados()
    update_content(area_page(**area_dados))

    return area_page()