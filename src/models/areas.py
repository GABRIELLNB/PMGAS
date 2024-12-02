import sys
from pathlib import Path
import pandas as pd

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

caminho_arquivo = "Areas Cadastradas - PMGAS.xlsx"

# Função para ler os perfis do arquivo Excel
def ler_perfis_excel(caminho_arquivo):
    try:
        # Carregar o Excel com pandas
        df = pd.read_excel(caminho_arquivo)

        # Verificar se as colunas necessárias estão presentes
        colunas_necessarias = ["Nome Proprietario", "CNPJ", "CEP", "Nome da empresa", "Natureza Juridica", "Porte"]
        if not all(coluna in df.columns for coluna in colunas_necessarias):
            raise ValueError("O arquivo Excel não contém todas as colunas necessárias.")

        # Transformar cada linha em um dicionário
        perfis = []
        for _, row in df.iterrows():
            perfil = {
                "Nome Proprietario": row["Nome Proprietario"],
                "CNPJ": row["CNPJ"],
                "CEP": row["CEP"],
                "Nome da empresa": row["Nome da empresa"],
                "Natureza Juridica": row["Natureza Juridica"],
                "Porte": row["Porte"],
            }
            perfis.append(perfil)
        
        return perfis

    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return []

# Exemplo de uso
perfis = ler_perfis_excel(caminho_arquivo)
for perfil in perfis:
    print(perfil)
