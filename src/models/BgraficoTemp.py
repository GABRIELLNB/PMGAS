import pandas as pd
import matplotlib.pyplot as plt

def grs_profundidade():
    # Carregar os dados (ajustando o caminho do arquivo se necessário)
    dados = pd.read_excel("MONITORAMENTO DA TEMPERATURA DO SUBSOLO DE OURO VERDE - SP.xlsx", skiprows=2)

    # Mostrar as primeiras 5 linhas para entender a estrutura
    print("Primeiras 5 linhas do DataFrame 'dados':")
    print(dados.head())

    # Certificar-se de que os nomes das colunas estão corretos
    if 'Profundidade (m)' in dados.columns and 'Temperatura Mínima (°C)' in dados.columns:
        # Selecionar as colunas de profundidade e as temperaturas
        dados_profundidade = dados[['Profundidade (m)', 'Temperatura Mínima (°C)', 'Temperatura Média (°C)', 'Temperatura Máxima (°C)']]

        # Remover qualquer linha onde há NaN em colunas essenciais
        dados_profundidade = dados_profundidade.dropna(subset=['Profundidade (m)', 'Temperatura Mínima (°C)', 'Temperatura Média (°C)', 'Temperatura Máxima (°C)'])

        # Exibindo os dados por profundidade
        print("\nDados de Temperatura por Profundidade:")
        print(dados_profundidade)
        
        cor = [ "#1A6772", "#298A95", "#3FA8B1"]
        # Plotando os dados de temperatura por profundidade
        plt.figure(figsize=(10, 6))
        plt.plot(dados_profundidade['Profundidade (m)'], dados_profundidade['Temperatura Mínima (°C)'], label='Temperatura Mínima (°C)', marker='o', color = cor[0])
        plt.plot(dados_profundidade['Profundidade (m)'], dados_profundidade['Temperatura Média (°C)'], label='Temperatura Média (°C)', marker='o', color = cor[1])
        plt.plot(dados_profundidade['Profundidade (m)'], dados_profundidade['Temperatura Máxima (°C)'], label='Temperatura Máxima (°C)', marker='o', color = cor[2])

        # Adicionando título e rótulos
        plt.xlabel('Profundidade (m)')
        plt.ylabel('Temperatura (°C)')
        plt.title('Temperatura por Profundidade')

        # Adicionando a legenda
        plt.legend()

        # Exibindo o gráfico
        plt.tight_layout()

        # Opcionalmente, salvar o gráfico como imagem
        plt.savefig('grafico_temp.png')

        # Mostrar o gráfico
        plt.show()

# Chamar a função
grs_profundidade()
import pandas as pd
import matplotlib.pyplot as plt

def grs_profundidade():
    # Carregar os dados (ajustando o caminho do arquivo se necessário)
    dados = pd.read_excel("MONITORAMENTO DA TEMPERATURA DO SUBSOLO DE OURO VERDE - SP.xlsx", skiprows=2)

    # Mostrar as primeiras 5 linhas para entender a estrutura
    print("Primeiras 5 linhas do DataFrame 'dados':")
    print(dados.head())

    # Certificar-se de que os nomes das colunas estão corretos
    if 'Profundidade (m)' in dados.columns and 'Temperatura Mínima (°C)' in dados.columns:
        # Selecionar as colunas de profundidade e as temperaturas
        dados_profundidade = dados[['Profundidade (m)', 'Temperatura Mínima (°C)', 'Temperatura Média (°C)', 'Temperatura Máxima (°C)']]

        # Remover qualquer linha onde há NaN em colunas essenciais
        dados_profundidade = dados_profundidade.dropna(subset=['Profundidade (m)', 'Temperatura Mínima (°C)', 'Temperatura Média (°C)', 'Temperatura Máxima (°C)'])

        # Exibindo os dados por profundidade
        print("\nDados de Temperatura por Profundidade:")
        print(dados_profundidade)

        # Definindo a largura das barras
        largura = 0.2

        # Ajustando a posição das barras para cada tipo de temperatura
        pos_menor = dados_profundidade['Profundidade (m)'] - largura
        pos_media = dados_profundidade['Profundidade (m)']
        pos_maior = dados_profundidade['Profundidade (m)'] + largura

        # Plotando o gráfico de barras
        plt.figure(figsize=(10, 6))
        
        cor = ["#104F58", "#1A6772", "#298A95"]

        # Barras para Temperatura Mínima
        plt.bar(pos_menor, dados_profundidade['Temperatura Mínima (°C)'], width=largura, label='Temperatura Mínima (°C)', color =cor[0])

        # Barras para Temperatura Média
        plt.bar(pos_media, dados_profundidade['Temperatura Média (°C)'], width=largura, label='Temperatura Média (°C)', color =cor[1])

        # Barras para Temperatura Máxima
        plt.bar(pos_maior, dados_profundidade['Temperatura Máxima (°C)'], width=largura, label='Temperatura Máxima (°C)', color =cor[2])

        # Adicionando título e rótulos
        plt.xlabel('Profundidade (m)')
        plt.ylabel('Temperatura (°C)')
        plt.title('Temperatura por Profundidade')

        # Adicionando a legenda
        plt.legend()

        # Exibindo o gráfico
        plt.tight_layout()

        # Opcionalmente, salvar o gráfico como imagem
        plt.savefig('grafico_temp2.png')

        # Mostrar o gráfico
        plt.show()

# Chamar a função
grs_profundidade()
