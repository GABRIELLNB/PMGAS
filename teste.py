import flet as ft

def main(page: ft.Page):

    def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"Closing view from {text}")
        anchor.close_view(text)

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print("handle_tap")
        anchor.open_view()

    # Lista de cores para busca
    colors = [f"Color {i}" for i in range(10)]

    # Função para atualizar a lista de sugestões no SearchBar
    def update_suggestions(query):
        anchor.controls.clear()
        for color in colors:
            if query.lower() in color.lower():
                anchor.controls.append(
                    ft.ListTile(
                        title=ft.Text(color),
                        on_click=close_anchor,
                        data=color.split()[-1],
                    )
                )
        page.update()

    # Barra de busca personalizada
    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.WHITE,
        on_change=lambda e: update_suggestions(e.data),
        on_submit=handle_submit,
        on_tap=handle_tap,
    )

    # Adiciona a barra de busca na página
    page.add(
        ft.Column(
            controls=[
                ft.Text("Busca de Cores", size=24, weight="bold"),
                anchor,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
ft.Row(
    alignment=ft.MainAxisAlignment.END,  # Alinha os itens à direita
    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha verticalmente ao centro
    controls=[
        # SearchBar
        ft.Container(
            bgcolor=ft.colors.WHITE,
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            border_radius=15,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.SEARCH, color=ft.colors.GREY),
                    ft.TextField(
                        hint_text="Buscar...",
                        border=ft.InputBorder.NONE,
                        cursor_color=ft.colors.BLACK,
                        text_style=ft.TextStyle(
                            size=16, color=ft.colors.BLACK
                        ),
                        expand=True,
                    ),
                    ft.Icon(ft.icons.CLOSE, color=ft.colors.GREY),
                ],
            ),
            width=800,  # Ajusta a largura do SearchBar
        ),
        ft.Container(width=300),
        # Botão com ícone
        ft.Container(
            alignment=ft.alignment.center,
            bgcolor=a2,
            width=40,  # Largura do círculo
            height=40,  # Altura do círculo
            content=ft.Icon(
                ft.icons.EDIT_SQUARE,  # Ícone de notificação
                size=40,  # Tamanho do ícone ajustado para maior visibilidade
                color=a1  # Cor do ícone
            ),
        ),
        ft.Container(width=100),
    ],
),



def searchbar_visual():
        return ft.Column(
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                padding=ft.padding.symmetric(horizontal=10, vertical=5),
                border_radius=15,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.icons.SEARCH, color=ft.colors.GREY),
                        ft.TextField(
                            hint_text="Buscar...",
                            border=ft.InputBorder.NONE,
                            cursor_color=ft.colors.BLACK,
                            text_style=ft.TextStyle(
                                size=16, color=ft.colors.BLACK
                            ),
                            expand=True,
                        ),
                        ft.Icon(ft.icons.CLOSE, color=ft.colors.GREY),
                    ],
                ),
            ),
            ft.Container(
                height=1,
                bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREY),
                margin=ft.margin.only(top=5),
            ),
        ],
        width=1000,  # Largura do SearchBar
        height=100,
    )