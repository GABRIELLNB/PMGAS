import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root =  file.parent.parent  # Importações relativas


sys.path.append(str(root))


USER_CREDENTIALS = {"usuario": "senha123"}


def check_email(email): #Verifica se o email existe
    return email in USER_CREDENTIALS

def check_senha(email, senha): #Verifica se a senha corresponde ao email informado
    return USER_CREDENTIALS.get(email) == senha