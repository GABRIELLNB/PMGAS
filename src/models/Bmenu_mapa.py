import pandas as pd


def Maps(tabela, grafico):
    tabela = pd.read_csv("weather_2000.csv")

    #display(tabela) para exbir a tablea não necessario!

    grafico = px.desity_mapbox(tabela, lon="geolocation_lng",lat="geolocation_lat", z="quantidade", zoom=3, radius=1)
    grafico.update_layout(margin={"r":0, "t": 0, "b": 0, "l":0})
    grafico.show()

