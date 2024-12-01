import sys
from pathlib import Path
import pandas as pd

file = Path(__file__).resolve()
parent = file.parent
root =  file.parent.parent  # Importações relativas

#BAIXAR pip install openpyxl e pip install pandas

sys.path.append(str(root))

# Caminho do arquivo .xlsx
caminho_arquivo = "Contas - PMGAS.xlsx"


def importar_credenciais(caminho_arquivo):
    # Carregar o arquivo Excel
    df = pd.read_excel(caminho_arquivo)

    # Converter para dicionário onde o 'usuario' é a chave e 'senha' é o valor
    user_credentials = dict(zip(df['Email'], df['Senha']))
    
    # Converter o DataFrame para dicionário de nome
    user_names = dict(zip(df['Email'], df['Nome']))
    
    return user_credentials, user_names

USER_CREDENTIALS, USER_NAMES = importar_credenciais(caminho_arquivo)

def check_email(email):  # Verifica se o email existe
    return email in USER_CREDENTIALS

def check_senha(email, senha):  # Verifica se a senha corresponde ao email informado
    if email in USER_CREDENTIALS:
        if USER_CREDENTIALS[email] == senha:
            return USER_NAMES[email]  # Retorna o nome associado ao emails
    return None
