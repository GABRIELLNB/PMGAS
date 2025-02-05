import sys
from pathlib import Path
import pandas as pd
from validate_docbr import CPF

file = Path(__file__).resolve()
parent = file.parent
root =  file.parent.parent  # Importações relativas


sys.path.append(str(root))
def importar_credenciais(caminho_arquivo):
    # Carregar o arquivo Excel
    df = pd.read_excel(caminho_arquivo)

    # Converter para dicionário onde o 'usuario' é a chave e 'senha' é o valor
    user_credentials = dict(zip(df['Email'], df['Senha']))
    
    return user_credentials

# Caminho do arquivo .xlsx
caminho_arquivo = "Contas - PMGAS - ADM.xlsx"
USER_CREDENTIALS = importar_credenciais(caminho_arquivo)


def check_email(email): #Verifica se o email existe
    return email in USER_CREDENTIALS

def check_senha(email, senha): #Verifica se a senha corresponde ao email informado
    return USER_CREDENTIALS.get(email) == senha






def buscar_perfil(email):
    df = pd.read_excel(caminho_arquivo)
    # Filtra o DataFrame para o e-mail fornecido
    perfil = df[df['Email'] == email]
    
    if not perfil.empty:
        # Retorna o perfil como um dicionário
        return perfil.iloc[0].to_dict()  
    else:
        return None