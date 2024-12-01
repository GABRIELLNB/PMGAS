import sys
from pathlib import Path
import pandas as pd

file = Path(__file__).resolve()
parent = file.parent
root = file.parent.parent  # Importações relativas

sys.path.append(str(root))

caminho_arquivo = "Contas - PMGAS.xlsx"

# Função para ler os perfis do arquivo Excel
def ler_perfis_excel(caminho_arquivo):
    try:
        # Carregar o Excel com pandas
        df = pd.read_excel(caminho_arquivo)

        # Verificar se as colunas necessárias estão presentes
        colunas_necessarias = ["Email", "Nome", "CPF", "Senha", "Cadastros"]
        if not all(coluna in df.columns for coluna in colunas_necessarias):
            raise ValueError("O arquivo Excel não contém todas as colunas necessárias.")

        # Transformar cada linha em um dicionário
        perfis = []
        for _, row in df.iterrows():
            perfil = {
                "Email": row["Email"],
                "Nome": row["Nome"],
                "CPF": row["CPF"],
                "Senha": row["Senha"],
                "Cadastros": row["Cadastros"],
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
