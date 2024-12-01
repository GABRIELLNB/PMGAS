import flet as ft
import flet.map as map

def mapa(page: ft.Page):
    # Camada de Marcadores
    marker_layer_ref = ft.Ref[map.MarkerLayer]()

    # Função para lidar com cliques no mapa
    def handle_tap(e: map.MapTapEvent):
        if e.name == "tap":
            marker_layer_ref.current.markers.append(
                map.Marker(
                    content=ft.Icon(
                        ft.Icons.LOCATION_ON, color=ft.cupertino_colors.DESTRUCTIVE_RED
                    ),
                    coordinates=e.coordinates,
                )
            )
        page.update()

    # Adicionar o mapa e outros componentes à página
    page.add(
        ft.Text("Clique no mapa para adicionar marcadores."),
        map.Map(
            expand=True,
            initial_center=map.MapLatitudeLongitude(15, 10),  # Centro inicial do mapa
            initial_zoom=4.2,  # Zoom inicial
            interaction_configuration=map.MapInteractionConfiguration(
                flags=map.MapInteractiveFlag.ALL  # Habilita todas as interações
            ),
            on_tap=handle_tap,  # Registra o evento de clique
            layers=[  # Camadas do mapa
                map.TileLayer(
                    url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",  # Usando OpenStreetMap
                ),
                map.MarkerLayer(
                    ref=marker_layer_ref,  # Camada para os marcadores
                    markers=[],  # Inicialmente, não há marcadores
                ),
            ],
        ),
    )
