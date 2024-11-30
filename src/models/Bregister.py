import pandas as pd
import flet as ft
import re  # Importa o módulo de expressões regulares
from validate_docbr import CPF, CNPJ

# Caminho para o arquivo Excel
caminho = "Contas - PMGAS.xlsx"

def validar_senha(senha):
    # Expressão regular para verificar se a senha contém pelo menos uma letra e um número
    if not re.search(r'(?=.*[A-Za-z])(?=.*\d)', senha):
        return False
    return True

def validar_cpf(cpf): #pip install validate-docbr biblioteca de validação
    cpf = CPF()
    
#def validar_email(email): 
    

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

    elif cpf in dados["CPF"].values:
        update_error_message("Este CPF já está registrado!")
        return
    
    if not validar_senha(senha):
        update_error_message("A senha deve conter pelo menos uma letra e um número.")
        return
    
    if not validar_cpf(cpf):
        update_error_message("O CPF está incorreto.")
        return

    # Criação de novo registro
    novos_dados = {
        "Email": email,
        "Nome": nome,
        "CPF": cpf.validate,
        "Senha": senha
    }

    novos_dados_df = pd.DataFrame([novos_dados])  # Converte o dicionário para DataFrame
    dados = pd.concat([dados, novos_dados_df], ignore_index=True)  # Adiciona ao DataFrame existente

    # Salva no arquivo Excel
    dados.to_excel(caminho, index=False)
    
    # Exibe mensagem de sucesso
    update_error_message("Cadastro realizado com sucesso!\n          Reinicie a aplicação")
