import pandas as pd
import matplotlib.pyplot as plt

def grs_ano():
        # Carregar os dados
        dados = pd.read_excel("4cn_uf_residuos.xlsx", sheet_name="CH4")

        # Mostrar as primeiras 5 linhas para entender a estrutura
        print("Primeiras 5 linhas do DataFrame 'dados':")
        print(dados.head())

        # Acessando a linha da Bahia (presumindo que 'Bahia' está em uma coluna como 'Estado' ou similar)
        # Ajuste o nome da coluna conforme necessário, no caso abaixo, considerando que 'Estado' seria o nome da coluna
        bahia_dados = dados[dados['Ministério da Ciência, Tecnologia e Inovações'] == 'Bahia']

        # Exibindo os dados da Bahia para cada ano (presumindo que os anos estão nas colunas 'Unnamed: 1' até 'Unnamed: 27')
        anos = ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6',
                'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12',
                'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
                'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24',
                'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27']

        # Pegando apenas as colunas de ano para a Bahia
        bahia_anos = bahia_dados[anos]

        # Convertendo os dados para numéricos, pois podem ser lidos como texto
        bahia_anos = bahia_anos.apply(pd.to_numeric, errors='coerce')

        # Exibindo os dados da Bahia por ano (sem agregação)
        print("\nDados da Bahia por ano (sem agregação):")
        print(bahia_anos)


        novos_nomes = {'Unnamed: 1':'1990', 'Unnamed: 2':'1991', 'Unnamed: 3':'1992', 'Unnamed: 4':'1993', 'Unnamed: 5':'1994', 'Unnamed: 6':'1995',
                'Unnamed: 7':'1996', 'Unnamed: 8':'1997', 'Unnamed: 9':'1998', 'Unnamed: 10':'1999', 'Unnamed: 11':'2000', 'Unnamed: 12':'2001',
                'Unnamed: 13':'2002', 'Unnamed: 14':'2003', 'Unnamed: 15':'2004', 'Unnamed: 16':'2005', 'Unnamed: 17':'2006', 'Unnamed: 18':'2007',
                'Unnamed: 19':'2008', 'Unnamed: 20':'2009', 'Unnamed: 21':'2010', 'Unnamed: 22':'2011', 'Unnamed: 23':'2012', 'Unnamed: 24':'2013',
                'Unnamed: 25':'2014', 'Unnamed: 26':'2015', 'Unnamed: 27':'2016'}  # Supondo 27 anos

        # Aplicando a renomeação
        bahia_anos.rename(columns=novos_nomes, inplace=True)


        # Transpondo os dados para ter os anos no eixo X e os valores no eixo Y
        bahia_anos = bahia_anos.transpose()

        cor = ["#021415",
        "#032021",
        "#04282D",
        "#0A3B42",
        "#104F58",
        "#1A6772",
        "#298A95",
        "#3FA8B1",
        "#6EC9CE",
        "#79D0D7",
        "#83D7DF",
        "#8DE0E8",
        "#97E8F0",
        "#A0F1F9",
        "#A9F7FF",
        "#B2FEFF",
        '#BBF7FE',
        "#C4F1FD",
        "#CCECFC",
        "#D5E6FB",
        "#DEE0FA",
        "#E7DAF9",
        "#F0D5F8",
        "#F9D0F7",
        "#FAD1F6",
        "#FAD3F5",
        "#FAD5F4"]
        # Plotando o gráfico de barras para os dados da Bahia
        plt.figure(figsize=(10, 6))
        plt.bar(bahia_anos.index, bahia_anos.values.flatten(), color=cor)
        plt.xlabel('Ano')
        plt.ylabel('Valores de CH₄ (Gg)')
        plt.title('Valores de CH₄ para a Bahia por Ano')

        # Mostrar o gráfico
        plt.xticks(rotation=45)  # Melhor visualização dos anos
        plt.tight_layout()

        # Opcionalmente, salvar o gráfico como uma imagem
        plt.savefig('grafico_bahia.png')  # Salvar o gráfico como imagem

        # Mostrar o gráfico
        plt.show()

grs_ano()

def grs_linha():
    # Carregar os dados
    dados = pd.read_excel("4cn_uf_residuos.xlsx", "4cn_uf_residuos.xlsx", sheet_name="CH4")

    # Mostrar as primeiras 5 linhas para entender a estrutura
    print("Primeiras 5 linhas do DataFrame 'dados':")
    print(dados.head())

    # Acessando a linha da Bahia (presumindo que 'Bahia' está em uma coluna como 'Estado' ou similar)
    # Ajuste o nome da coluna conforme necessário, no caso abaixo, considerando que 'Estado' seria o nome da coluna
    bahia_dados = dados[dados['Ministério da Ciência, Tecnologia e Inovações'] == 'Bahia']

    # Exibindo os dados da Bahia para cada ano (presumindo que os anos estão nas colunas 'Unnamed: 1' até 'Unnamed: 27')
    anos = ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6',
            'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12',
            'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
            'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24',
            'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27']

    # Pegando apenas as colunas de ano para a Bahia
    bahia_anos = bahia_dados[anos]

    # Convertendo os dados para numéricos, pois podem ser lidos como texto
    bahia_anos = bahia_anos.apply(pd.to_numeric, errors='coerce')

    # Exibindo os dados da Bahia por ano (sem agregação)
    print("\nDados da Bahia por ano (sem agregação):")
    print(bahia_anos)

    novos_nomes = {'Unnamed: 1':'1990', 'Unnamed: 2':'1991', 'Unnamed: 3':'1992', 'Unnamed: 4':'1993', 'Unnamed: 5':'1994', 'Unnamed: 6':'1995',
                   'Unnamed: 7':'1996', 'Unnamed: 8':'1997', 'Unnamed: 9':'1998', 'Unnamed: 10':'1999', 'Unnamed: 11':'2000', 'Unnamed: 12':'2001',
                   'Unnamed: 13':'2002', 'Unnamed: 14':'2003', 'Unnamed: 15':'2004', 'Unnamed: 16':'2005', 'Unnamed: 17':'2006', 'Unnamed: 18':'2007',
                   'Unnamed: 19':'2008', 'Unnamed: 20':'2009', 'Unnamed: 21':'2010', 'Unnamed: 22':'2011', 'Unnamed: 23':'2012', 'Unnamed: 24':'2013',
                   'Unnamed: 25':'2014', 'Unnamed: 26':'2015', 'Unnamed: 27':'2016'}  # Supondo 27 anos

    # Aplicando a renomeação
    bahia_anos.rename(columns=novos_nomes, inplace=True)

    # Transpondo os dados para ter os anos no eixo X e os valores no eixo Y
    bahia_anos = bahia_anos.transpose()

    cor = ["#021415", "#032021", "#04282D", "#0A3B42", "#104F58", "#1A6772", "#298A95", "#3FA8B1", "#6EC9CE", 
           "#79D0D7", "#83D7DF", "#8DE0E8", "#97E8F0", "#A0F1F9", "#A9F7FF", "#B2FEFF", '#BBF7FE', "#C4F1FD", 
           "#CCECFC", "#D5E6FB", "#DEE0FA", "#E7DAF9", "#F0D5F8", "#F9D0F7", "#FAD1F6", "#FAD3F5", "#FAD5F4"]

    # Plotando o gráfico de linha para os dados da Bahia
    plt.figure(figsize=(10, 6))

    # Utilizando plt.plot() para gerar o gráfico de linha
    plt.plot(bahia_anos.index, bahia_anos.values.flatten(), marker='o', color="#04282D", linestyle='-', linewidth=2, markersize=5)

    # Personalizando o gráfico
    plt.xlabel('Ano')
    plt.ylabel('Valores de CO₂e (Gg)')
    plt.title('Valores de CO₂e (GWP SAR) para a Bahia por Ano')

    # Melhor visualização dos anos no eixo X
    plt.xticks(rotation=45)  # Rotaciona os anos para melhor visualização

    # Ajuste para que o gráfico fique bem ajustado
    plt.tight_layout()

    # Opcionalmente, salvar o gráfico como uma imagem
    plt.savefig('grafico_bahia2.png')  # Salvar o gráfico como imagem

    # Mostrar o gráfico
    plt.show()


