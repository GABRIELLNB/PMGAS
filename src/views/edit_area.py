import flet as ft
import sys
from pathlib import Path
import pandas as pd

# Caminho relativo para importar módulos
file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas
sys.path.append(str(root))


caminho = 'Areas Cadastradas - PMGAS.xlsx'

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

# Função de configuração
def edit_area(page: ft.Page):
    from perfil import perfil_us
    
    page.title = "PMGAS - Editar Áreas"

    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página
    
    error_message = ft.Text(value="", color=ft.colors.RED)

    def update_error_message(msg, color):
        error_message.value = msg
        error_message.color = color
        page.update()
    
    def carregar_areas():
        from models.Bcadastro_Areas import buscar_Area
        df = pd.read_excel(caminho)
        cnpj_area = df['CNPJ'].iloc[0]
        area = buscar_Area(cnpj_area)
        
        if area:
            return area
        else:
            return None
    
    def salvar_edicoes(nome,cnpj, cep, nome_empresa, natureza, porte):
        df = pd.read_excel(caminho)
        
        area_index = df[df['CNPJ']== cnpj].index
        
        if not area_index.empty:
            df.at[area_index[0], 'Nome Proprietario'] = nome
            df.at[area_index[0], 'CNPJ'] = cnpj
            df.at[area_index[0], 'CEP'] = cep
            df.at[area_index[0], 'Nome da empresa'] =  nome_empresa
            df.at[area_index[0], 'Natureza Juridica'] = natureza
            df.at[area_index[0], 'Porte'] = porte
            return True # Salva as alterações no arquivo Excel
        else:
            return False # Retorna False se o usuário não for encontrado
            

    # Função principal para montar a página de edição de perfil
    def area():
        from areas_cadastradas import areas_cadastradas
        area = carregar_areas()
        if area is None:
            return ft.Text("Area não encontrada", color="red")
        
        nome_input = ft.TextField(value=area["Nome Proprietario"], hint_text="Nome Proprietario", width=600, height=45, border=ft.InputBorder.NONE)
        cnpj_input = ft.TextField(value=area["CNPJ"], hint_text="CNPJ", width=600, height=45, read_only=True, border=ft.InputBorder.NONE)
        cep_input = ft.TextField(value=area["CEP"], hint_text="CEP", width=600, height=45, read_only=True, border=ft.InputBorder.NONE)
        nome_empresa_input = ft.TextField(value=area["Nome da empresa"], hint_text="Nome da empresa", width=600, height=45, border=ft.InputBorder.NONE)
        natureza_input = ft.TextField(value=area["Natureza Juridica"], hint_text="Natureza Juridica", width=600, height=45, border=ft.InputBorder.NONE)
        porte_input = ft.TextField(value=area["Porte"], hint_text="Porte", width=600, height=45, border=ft.InputBorder.NONE)

        
        def on_salvar_click(e):
            nome = nome_input.value
            cnpj = cnpj_input.value
            cep = cep_input.value
            nome_empresa = nome_empresa_input.value
            natureza = natureza_input.value
            porte = porte_input.value
            
            if salvar_edicoes(nome, cnpj, cep, nome_empresa, natureza, porte):
                update_error_message("Área atualizada com sucesso!", ft.colors.GREEN)
            else:
                update_error_message("Erro ao salvar área.", ft.colors.RED)

        # Botão para salvar as edições
        salvar_button = ft.ElevatedButton(
            text="Salvar",
            bgcolor=b,
            color=a2,
            width=400,
            height=40,
            on_click=on_salvar_click,)
        
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
                                    
                                    ft.Container(
                                            on_click=lambda e: update_content(perfil_us(page)),
                                            content=ft.Icon(
                                                ft.icons.ARROW_BACK_IOS,
                                                size=24,
                                                color=a2,
                                            ),
                                        ),
                                    ft.Container(width=500),
                                    ft.Text("Editar Área", weight="bold", size=20, color=a2),
                                    ft.Container(width=550),
                                ],
                            
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10,
                            ),
                            
                            ft.Divider(height=1, color=ft.colors.with_opacity(0.25, ft.colors.GREY)),
        
                            ft.Row( 
                                controls=[
                                    ft.Container(width=310),
                                    ft.Container(
                                        bgcolor=a2,
                                        width=650,
                                        height=750,
                                        padding=ft.padding.all(20),
                                        border_radius=20,
                                        content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[  
                                                ft.Row(
                                                    controls=[ 
                                                        ft.Container(width=20),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="Nome Proprietário",
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
                                                            height=40,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=-5),
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
                                                        ft.Container(width=20),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="CNPJ",
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
                                                            height=40,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=-5),
                                                            border_radius=15,
                                                            content=ft.Column(controls=[cnpj_input]),
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
                                                        ft.Container(width=20),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="CEP",
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
                                                            height=40,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=-5),
                                                            border_radius=15,
                                                            content=ft.Column(controls=[cep_input]),
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
                                                        ft.Container(width=20),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="Nome da Empresa",
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
                                                            height=40,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=-5),
                                                            border_radius=15,
                                                            content=ft.Column(controls=[nome_empresa_input]),
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
                                                        ft.Container(width=20),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="Natureza Jurídica",
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
                                                            height=40,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=-5),
                                                            border_radius=15,
                                                            content=ft.Column(controls=[natureza_input]),
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
                                                        ft.Container(width=20),
                                                        ft.Container(
                                                            alignment=ft.alignment.top_left,  # Alinha no canto superior esquerdo
                                                            content=ft.Text(
                                                                value="Porte da Empresa",
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
                                                            height=40,
                                                            padding=ft.padding.symmetric(horizontal=20, vertical=-5),
                                                            border_radius=15,
                                                            content=ft.Column(controls=[porte_input]),
                                                        ),
                                                    ],
                                                ),
                                                ft.Divider(
                                                height=1,
                                                color=ft.colors.with_opacity(0.25, ft.colors.GREY),
                                                thickness=1
                                                ),
                                                ft.Container(height=10),
                                                error_message,
                                                salvar_button,
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

    page.scroll = True
    return area()


