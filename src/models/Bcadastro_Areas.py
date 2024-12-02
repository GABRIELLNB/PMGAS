import pandas as pd
import flet as ft
import re  # Importa o módulo de expressões regulares
from validate_docbr import CNPJ

#BAIXAR pip install validate_docbr
caminho = 'Areas Cadastradas - PMGAS.xlsx'

def buscar_Area(cnpj):
    df = pd.read_excel(caminho)
    
    # Busca a área pelo CNPJ fornecido
    area = df[df['CNPJ'] == cnpj]
    
    if not area.empty:
        # Retorna a primeira linha da área encontrada como um dicionário
        return area.iloc[0].to_dict()
    else:
        # Retorna None caso não encontre a área
        return None


def validar_cnpj(cnpj): #pip install cnpj-cpf-validator biblioteca de validação
    validaor = CNPJ()
    return validaor.validate(cnpj)
    
def validar_cep(cep):
    cep = ''.join(filter(str.isdigit, cep))
    if len(cep) != 8:
        return False

    padrao = re.compile(r"^\d{8}$")  # Corrigir o padrão
    return bool(padrao.match(cep))

    
def salvar_dados_Areas(Nome_Proprietario, cnpj, cep, nome_empr, nature, porte, update_error_message_Areas):
    # Verifica se o arquivo já existe
    try:
        dados = pd.read_excel(caminho)
    except FileNotFoundError:
        dados = pd.DataFrame(columns=["Nome Proprietario", "CNPJ", "CEP", "Nome da empresa", "Natureza Juridica", "Porte"])# Cria um novo DataFrame se o arquivo não existir
    
    # Verifica se os campos estão vazios
    if not Nome_Proprietario or not cnpj or not cep or not nome_empr or not nature or not porte:
        update_error_message_Areas("Por favor, preencha todos os campos!")
        return
    
    if cnpj in dados["CNPJ"].values:
       update_error_message_Areas("CNPJ já registrados!")
       return
    
    if cep in dados["CEP"].values:
        update_error_message_Areas("CEP já registrados!")
    
    if nome_empr in dados["Nome da empresa"].values:
       update_error_message_Areas("Nome da empresa já registrados!")
        
    if not validar_cnpj(cnpj):
        update_error_message_Areas("O CNPJ está incorreto.")
        return 
    
    if not validar_cep(cep):     
        update_error_message_Areas("O CEP está incorreto.")
        return
    
    # Criação de novo registro
    novos_dados_Area = {
        "Nome Proprietario" : Nome_Proprietario,
        "CNPJ" : cnpj,
        "CEP" : cep,
        "Nome da empresa" :  nome_empr,
        "Natureza Juridica" : nature,
        "Porte" : porte
    }
    
    novos_dados_Area_df = pd.DataFrame([novos_dados_Area])
    dados = pd.concat([dados, novos_dados_Area_df], ignore_index = True)
    
    dados.to_excel(caminho, index=False)
    
    update_error_message_Areas("Cadastro de Area realizado com sucesso!", ft.colors.GREEN)