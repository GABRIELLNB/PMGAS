import pandas as pd
import flet as ft
import re  # Importa o módulo de expressões regulares
from validate_docbr import CPF

# Caminho para o arquivo Excel
caminho = "Contas - PMGAS.xlsx"

def validar_senha(senha):
    # Expressão regular para verificar se a senha contém pelo menos uma letra e um número
    if not re.search(r'(?=.*[A-Za-z])(?=.*\d)', senha):
        return False
    return True

def validar_cpf(cpf):
    # Valida o CPF usando a biblioteca validate_docbr
    cpf_obj = CPF()
    return cpf_obj.validate(cpf)  # Retorna True se o CPF for válido, False caso contrário

def validar_email(email):
    # Expressão regular para validar o formato do email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))  # Retorna True se o email for válido, False caso contrário

def salvar_dados(email, nome, cpf, senha, update_error_message):
    # Verifica se o arquivo já existe
    try:
        dados = pd.read_excel(caminho)
    except FileNotFoundError:
        dados = pd.DataFrame(columns=["Email", "Nome", "CPF", "Senha"])  # Cria um novo DataFrame se o arquivo não existir

    # Verifica se os campos estão vazios
    if not email or not cpf or not nome or not senha:
        update_error_message("Por favor, preencha todos os campos!")
        return
    
    if cpf in dados["CPF"].values and email in dados["Email"].values:
        update_error_message("Dados já registrados!")
        return
    
    # Verifica se o email ou CPF já estão registrados
    if email in dados["Email"].values:
        update_error_message("Este email já está registrado!")
        return

    if cpf in dados["CPF"].values:
        update_error_message("Este CPF já está registrado!")
        return
    
    # Valida a senha
    if not validar_senha(senha):
        update_error_message("A senha deve conter pelo menos uma letra e um número.")
        return
    
    # Valida o CPF
    if not validar_cpf(cpf):
        update_error_message("O CPF está incorreto.")
        return

    # Valida o email
    if not validar_email(email):
        update_error_message("O email está incorreto.")
        return

    # Criação de novo registro
    novos_dados = {
        "Email": email,
        "Nome": nome,
        "CPF": cpf,
        "Senha": senha
    }

    novos_dados_df = pd.DataFrame([novos_dados])  # Converte o dicionário para DataFrame
    dados = pd.concat([dados, novos_dados_df], ignore_index=True)  # Adiciona ao DataFrame existente

    # Salva no arquivo Excel
    dados.to_excel(caminho, index=False)
    
    # Exibe mensagem de sucesso
    update_error_message("Cadastro realizado com sucesso!\n          Reinicie a aplicação")

