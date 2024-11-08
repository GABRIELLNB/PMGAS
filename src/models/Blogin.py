import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root =  file.parent.parent  # Importações relativas


sys.path.append(str(root))


USER_CREDENTIALS = {"usuario": "senha123"}


def check_credentials(email, senha):
    return USER_CREDENTIALS.get(email) == senha
