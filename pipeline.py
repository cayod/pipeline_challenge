from asyncore import read
from email import header
from tkinter.font import names
from tracemalloc import start
import wget
import os
import zipfile
import pandas as pd
import sqlite3

# Links para download
linkCnpj = [
    (
        'http://200.152.38.155/CNPJ/K3241.K03200Y0.D20212.SOCIOCSV.zip'
    ),
    (
        'http://200.152.38.155/CNPJ/K3241.K03200Y0.D20212.ESTABELE.zip'
    ),
    (
        'http://200.152.38.155/CNPJ/K3241.K03200Y0.D20212.EMPRECSV.zip'
    ),
    (
        'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-'
        'tributaria/cadastros/consultas/arquivos/'
        'novolayoutdosdadosabertosdocnpj-dez2021.pdf'
    )
]

# Nome das colunas do arquivo empresa.csv
columnsEmpresa = [
    'CNPJ BÁSICO', 'RAZÃO SOCIAL/NOME EMPRESARIAL', 'NATUREZA JURÍDICA',
    'QUALIFICAÇÃO DO RESPONSÁVEL', 'CAPITAL SOCIAL DA EMPRESA',
    'PORTE DA EMPRESA', 'ENTE FEDERATIVO RESPONSÁVEL'
]

# Nome das colunas do arquivo estabelecimento.csv
columnsEstabelecimento = [
    'CNPJ BÁSICO', 'CNPJ ORDEM', 'CNPJ DV', 'IDENTIFICADOR MATRIZ/FILIAL',
    'NOME FANTASIA', 'SITUAÇÃO CADASTRAL', 'DATA SITUAÇÃO CADASTRAL',
    'MOTIVO SITUAÇÃO CADASTRAL', 'NOME DA CIDADE NO EXTERIOR', 'PAIS',
    'DATA DE INÍCIO ATIVIDADE', 'CNAE FISCAL PRINCIPAL',
    'CNAE FISCAL SECUNDÁRIA', 'TIPO DE LOGRADOURO', 'LOGRADOURO', 'NÚMERO',
    'COMPLEMENTO', 'BAIRRO', 'CEP', 'UF', 'MUNICÍPIO', 'DDD 1', 'TELEFONE 1',
    'DDD 2', 'TELEFONE 2', 'DDD DO FAX', 'FAX', 'CORREIO ELETRÔNICO',
    'SITUAÇÃO ESPECIAL', 'DATA DA SITUAÇÃO ESPECIAL'
]

# Nome das colunas do arquivo socio.csv
columnsSocio = [
    'CNPJ BÁSICO', 'IDENTIFICADOR DE SÓCIO',
    'NOME DO SÓCIO (NO CASO PF) OU RAZÃO SOCIAL (NO CASO PJ)',
    'CNPJ/CPF DO SÓCIO', 'QUALIFICAÇÃO DO SÓCIO', 'DATA DE ENTRADA SOCIEDADE',
    'PAIS', 'REPRESENTANTE LEGAL', 'NOME DO REPRESENTANTE',
    'QUALIFICAÇÃO DO REPRESENTANTE LEGAL', 'FAIXA ETÁRIA'
]

# Nomes para os zip
zipName = [
    "1-empresa.zip", "2-estabelecimento.zip", "3-socio.zip", "4-colunas.pdf"]

# Nomes para os arquivos
fileName = [
    "1-empresa.csv", "2-estabelecimento.csv", "3-socio.csv", "4-colunas.csv"]

# Nome da database
databaseName = 'cnpj.db'

# Confirma se os dados estão baixados no repostitório
fileDownloadedConfirm = os.path.exists(
    zipName[0]) and os.path.exists(
        zipName[1]) and os.path.exists(
            zipName[2]) and os.path.exists(zipName[3])

# Confirma se os dados estão descompactados
fileUnzipedConfirm = os.path.exists(
    fileName[0]) and os.path.exists(
        fileName[1]) and os.path.exists(fileName[2])

# Download dos arquivos


def downloadFiles():
    # loop para fazer o download de todos os arquivos
    count = 0
    for url in linkCnpj:
        print('Downloading...')
        file = wget.download(url)
        filePath = os.path.basename(file)
        os.rename(filePath, zipName[count])
        count += 1
        print('{} downloaded file'.format(count))

# Desconpacta os arquivos zip


def unzip():
    endCount = 3
    startCount = 0
    for startCount in range(endCount):
        with zipfile.ZipFile(zipName[startCount], 'r') as unzip:
            unzip.extractall()
            changeName = unzip.infolist()[0].filename
            os.rename(changeName, fileName[startCount])
            print('{} unziped file'.format(startCount))

# Gera a database e insere as tables


def createDatabase():
    database = sqlite3.connect('databaseName')
    empresaDataframe = pd.read_csv(
        fileName[0], encoding="ISO8859-1", sep=',')
    empresaDataframe.to_sql(name='empresa', con=database)
    estabelecimentoDataframe = pd.read_csv(
        fileName[1], encoding="ISO8859-1", sep=',')
    estabelecimentoDataframe.to_sql(name='estabelecimento', con=database)
    sociosDataframe = pd.read_csv(
        fileName[2], encoding="ISO8859-1", sep=',')
    sociosDataframe.to_sql(name='socios', con=database)

# Pega os dados das colunas para inserir nos csv


def dataframe_set_columns():
    empresaDataframe = pd.read_csv(
        fileName[0], encoding="ISO8859-1", names=columnsEmpresa, sep=';')
    empresaDataframe.to_csv(fileName[0])
    print('Columns set at {}'.format(fileName[0]))
    estabelecimentoDataframe = pd.read_csv(
        fileName[1], encoding="ISO8859-1", names=columnsEstabelecimento,
        sep=';')
    estabelecimentoDataframe.to_csv(fileName[1])
    print('Columns set at {}'.format(fileName[1]))
    sociosDataframe = pd.read_csv(
        fileName[2], encoding="ISO8859-1", names=columnsSocio, sep=';')
    sociosDataframe.to_csv(fileName[2])
    print('Columns set at {}'.format(fileName[2]))
    createDatabase()


# Fluxo de baixar o arquivo, descompactar, tratar e disponibilizar
countFlow = 0
while countFlow == 0:
    if not fileDownloadedConfirm:
        downloadFiles()
    elif not fileUnzipedConfirm:
        unzip()
    else:
        dataframe_set_columns()
        countFlow = 1
