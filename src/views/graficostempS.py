import flet as ft
def graficostempS(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def Handle_Sgraficos():
        ft.Column._add_event_handler(ft.Text("Gráficos semanais de temperatura"))
        click = ft.BottomSheet(
            on_dismiss=Handle_Sgraficos,
            content=ft.Container(
                padding=50,
                content=ft.Column(
                    tight=True,
                    controls=[
                        ft.Text("This is bottom sheet's content!"),
                        ft.ElevatedButton("Close bottom sheet", on_click=lambda _: ft.Column.close(click)),
                    ],
                ),
            ),
        )
        page.add(ft.ElevatedButton("Gráficos", on_click=lambda _: page.open(click)))