import flet as ft
import sys
from pathlib import Path
import flet.map as map  # Adicionando o import necessário para o mapa

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

a1 = "#7BD8D9"
a2 = "#04282D"
b = "#FFFFFF"

# Cria a barra de navegação personalizada
def navigation_bar(update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, inicio_content):
    return ft.NavigationBar(
        bgcolor=b,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.DOCUMENT_SCANNER_SHARP, label="Cadastros"),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="Gráficos"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configurações"),
        ],
        on_change=lambda e: escolher_opcao(e, update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, inicio_content)
    )

def escolher_opcao(e, update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, inicio_content):
    opcao = e.control.selected_index
    
    if opcao == 0:
        update_content(inicio_content())
    elif opcao == 1:
        update_content(cadastros_content())
    elif opcao == 2:
        update_content(graficos_content())
    elif opcao == 3:
        update_content(perfil_content())
    elif opcao == 4:
        update_content(configuracoes_content())

def menu(page: ft.Page):

    # Define o título da página
    page.title = "PMGAS - Menu"
    
    def update_content(content):
        page.controls.clear()  # Limpa o conteúdo da página
        page.controls.append(content)  # Adiciona o novo conteúdo
        page.update()  # Atualiza a página

    def menu_content():
        return inicio(page)

    def configuracoes_content():
        from configuracoes import configuracoes
        return configuracoes(page)

    def cadastros_content():
        from cadastros import cadastros
        return cadastros(page)

    def graficos_content():
        from graficos import graficos
        return graficos(page)

    def perfil_content():
        from perfil import perfil_us
        return perfil_us(page)
    
    # Função para abrir a página flutuante de gráficos
    def abrir_graficosTP():
        graficos_dialog = ft.AlertDialog(
            title=ft.Row(
                controls=[
                    ft.Container(
                        on_click=lambda e: close_grf_dialog(page),  # Função para voltar ao menu
                        content=ft.Icon(
                            ft.icons.ARROW_BACK_IOS,
                            size=24,
                            color=a2,
                        ),
                    ),
                    ft.Text(
                        "Mais informações sobre os níveis de gás",
                        size=20,
                        weight="bold",
                        color=a2,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            content=ft.Container(  
                width=1000,
                height=500,
                content=ft.Column(
                    controls=[
                        ft.Text("Observa-se que as emissões de metano na Bahia aumentaram ao longo do período, com uma significativa elevação entre 2010 e 2016, atingindo 190,9 Gg em 2016. Esse aumento pode estar relacionado a fatores como o crescimento da população, aumento da urbanização e a expansão das atividades industriais e de manejo de resíduos."),
                        ft.Container(height=30),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Image(
                                        src="grafico_bahia2.png",  # Caminho local ou URL da imagem
                                        width=700,  # Largura da imagem
                                        height=400,  # Altura da imagem
                                        fit=ft.ImageFit.CONTAIN,  # Ajuste da imagem
                                    ),
                            ]
                        )
                    ],
                ),
                
            ),
            bgcolor=b,
        )
        page.dialog = graficos_dialog  # Definindo o Dialog na página
        graficos_dialog.open = True  # Abrindo o Dialog
        page.update()  # Atualizando a página para mostrar o Dialog

    # Função para abrir a página flutuante de Aterros Ronald
    def abrir_GSgraficos():
        aterros_dialog = ft.AlertDialog(
            title=ft.Row(
                controls=[
                    ft.Container(
                        on_click=lambda e: close_grf_dialog(page),  # Função para voltar ao menu
                        content=ft.Icon(
                            ft.icons.ARROW_BACK_IOS,
                            size=24,
                            color=a2,
                        ),
                    ),
                    ft.Text(
                        value = "Mais informações sobre as temperaturas",
                        size=20,
                        weight="bold",
                        color=a2,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            content=ft.Container(  
                width=1000,
                height=500,
                content=ft.Column(
                    controls=[

                        ft.Text("Os dados de temperatura do solo em diferentes profundidades indicam que a temperatura média se mantém relativamente estável entre as camadas, com variações menores conforme a profundidade aumenta."),
                        ft.Container(height=30),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Image(
                                        src="grafico_temp.png",  # Caminho local ou URL da imagem
                                        width=700,  # Largura da imagem
                                        height=400,  # Altura da imagem
                                        fit=ft.ImageFit.CONTAIN,  # Ajuste da imagem
                                    ),
                            ]
                        )
                    ]
                )
            ),
            bgcolor=b,
        )
        
        page.dialog = aterros_dialog  # Definindo o Dialog na página
        aterros_dialog.open = True  # Abrindo o Dialog
        page.update()  # Atualizando a página para mostrar o Dialog
    
    def close_grf_dialog(page):
        page.dialog.open = False  # Fecha o diálogo
        page.update()  # Atualiza a página

        # Após fechar, reexibe a página de configurações
        update_content(menu_content())
    
    page.window.always_on_top = True

    def handle_tap(e: map.MapTapEvent):
        print(e)
    
    def create_map():
        # Container para o mapa
        map_container = ft.Container(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=75,
                controls=[
                    ft.Container(
                        height=380,  
                        width=1000,
                        border_radius=15,
                        content=map.Map(
                            configuration=map.MapConfiguration(
                                on_init=lambda e: print("Map Init"),
                                on_tap=handle_tap,
                                on_long_press=handle_tap,
                            ),
                            layers=[
                                map.TileLayer(
                                    url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                                    on_image_error=lambda e: print("Image Error"),
                                ),
                                map.CircleLayer(
                                    circles=[
                                        map.CircleMarker(
                                            radius=20,
                                            coordinates=map.MapLatitudeLongitude(-12.9714, -38.5014),
                                            color=ft.colors.BLUE,
                                            border_color=ft.colors.random_color(),
                                            border_stroke_width=5,
                                        )
                                    ]
                                ),
                                map.MarkerLayer(
                                    markers=[
                                        map.Marker(
                                            content=ft.Icon(
                                                ft.icons.random_icon(),
                                                color=ft.colors.random_color(),
                                                size=30,
                                            ),
                                            coordinates=map.MapLatitudeLongitude(35, 35),
                                        )
                                    ]
                                ),
                                map.RichAttribution(
                                    alignment=ft.alignment.top_center,
                                    attributions=[
                                        map.TextSourceAttribution(
                                            text="Flet",
                                            prepend_copyright=False,
                                            on_click=lambda e: page.launch_url("https://flet.dev"),
                                        )
                                    ],
                                ),
                                map.SimpleAttribution(
                                    text="Simple Attr.", alignment=ft.alignment.top_center
                                ),
                            ],
                        ),
                     )
                ]
            ),
        )

        # Conteúdo do menu com a navegação
        navigation_controls = navigation_bar(
            update_content, configuracoes_content, cadastros_content, graficos_content, perfil_content, menu_content
        )

        # Row com containers para "Gráficos" e "Gás"
        action_buttons = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=75,
        controls=[
            ft.Container(
                padding=ft.padding.all(10),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE,
                width=450,
                height=205,
                border_radius=10,
                ink=True,
                on_click=lambda e: abrir_graficosTP(),  
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        
                        ft.Container(
                            alignment=ft.alignment.center,  # Center the title
                            content=ft.Text(
                                value="20 g/m 5h2min",
                                weight='bold',
                                size=28,
                                color=a2
                                ),  # Text label
                            ),
                        ft.Image(
                            src="gas.png",  # Path to the image
                            width=450,  # Image width
                            height=122,  # Image height
                            fit=ft.ImageFit.CONTAIN,  # Fit the image within the container
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.Text(value="Conteúdo meramente ilustrativo", size=8, text_align=ft.TextAlign.END, color=a2),
                            ]
                        ),
                    ]
                ),
            ),
                    
                    
                ft.Container(
                    
                    padding=ft.padding.all(10),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=450,
                    height=200,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: abrir_GSgraficos(),
                    content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        
                        ft.Container(
                            alignment=ft.alignment.center,  # Center the title
                            content=ft.Text(
                                value="PMGAS Aterros",
                                weight='bold',
                                size=30,
                                color=a2
                                ),  # Text label
                            ),
                        ft.Container(
                            alignment=ft.alignment.center,  # Center the title
                            content=ft.Text(
                                value="26 °C",
                                weight='bold',
                                size=70,
                                color=a2
                                ),
                        ),
                        ft.Container(height=5),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.Text(value="Conteúdo meramente ilustrativo", size=8, text_align=ft.TextAlign.END, color=a2),
                            ]
                            ),
                    ]
                ),
                )
            ]
        )

        # Retorna a estrutura do conteúdo principal
        return ft.Column(
            controls=[
                ft.Container(height=5),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a imagem horizontalmente
                    controls=[
                        ft.Image(
                            src="image.png",  # Caminho local ou URL da imagem
                            width=250,
                            height=50,
                            fit=ft.ImageFit.CONTAIN,  # Mantém proporção
                        )
                    ]
                ),
                
                navigation_controls,
                ft.Container(height=5),
                map_container,
                action_buttons,
            ]
        )

    def inicio():
        return create_map()

    # Adiciona o conteúdo inicial à página
    page.scroll = True
    return inicio()