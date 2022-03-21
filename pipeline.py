from asyncore import read
from email import header
from tkinter.font import names
from tracemalloc import start
import wget
import os
import zipfile
import pandas as pd
import sqlite3

#Links para download
link_cnpj = [
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
        'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/arquivos/novolayoutdosdadosabertosdocnpj-dez2021.pdf'
    )
]

#Nome das colunas do arquivo empresa.csv
columns_empresa = [
    'CNPJ BÁSICO', 'RAZÃO SOCIAL/NOME EMPRESARIAL', 'NATUREZA JURÍDICA', 'QUALIFICAÇÃO DO RESPONSÁVEL', 'CAPITAL SOCIAL DA EMPRESA', 'PORTE DA EMPRESA', 'ENTE FEDERATIVO RESPONSÁVEL' 
]

#Nome das colunas do arquivo estabelecimento.csv
columns_estabelecimento = [
    'CNPJ BÁSICO', 'CNPJ ORDEM', 'CNPJ DV', 'IDENTIFICADOR MATRIZ/FILIAL', 'NOME FANTASIA', 'SITUAÇÃO CADASTRAL', 'DATA SITUAÇÃO CADASTRAL', 'MOTIVO SITUAÇÃO CADASTRAL', 'NOME DA CIDADE NO EXTERIOR', 'PAIS', 'DATA DE INÍCIO ATIVIDADE', 'CNAE FISCAL PRINCIPAL', 'CNAE FISCAL SECUNDÁRIA', 'TIPO DE LOGRADOURO', 'LOGRADOURO', 'NÚMERO', 'COMPLEMENTO', 'BAIRRO', 'CEP', 'UF', 'MUNICÍPIO', 'DDD 1', 'TELEFONE 1', 'DDD 2', 'TELEFONE 2', 'DDD DO FAX', 'FAX', 'CORREIO ELETRÔNICO', 'SITUAÇÃO ESPECIAL', 'DATA DA SITUAÇÃO ESPECIAL'
]

#Nome das colunas do arquivo socio.csv
columns_socio = [
    'CNPJ BÁSICO', 'IDENTIFICADOR DE SÓCIO', 'NOME DO SÓCIO (NO CASO PF) OU RAZÃO SOCIAL (NO CASO PJ)', 'CNPJ/CPF DO SÓCIO', 'QUALIFICAÇÃO DO SÓCIO', 'DATA DE ENTRADA SOCIEDADE', 'PAIS', 'REPRESENTANTE LEGAL', 'NOME DO REPRESENTANTE', 'QUALIFICAÇÃO DO REPRESENTANTE LEGAL', 'FAIXA ETÁRIA'
]

#Nomes para os zip
zip_name = [
    "1-empresa.zip", "2-estabelecimento.zip", "3-socio.zip", "4-colunas.pdf"]

#Nomes para os arquivos
file_name = [
    "1-empresa.csv", "2-estabelecimento.csv", "3-socio.csv", "4-colunas.csv"]

#Confirma se os dados estão baixados no repostitório
file_downloaded_confirm = os.path.exists(zip_name[0]) and os.path.exists(zip_name[1]) and os.path.exists(zip_name[2]) and os.path.exists(zip_name[3])

#Confirma se os dados estão descompactados
file_unziped_confirm = os.path.exists(file_name[0]) and os.path.exists(file_name[1]) and os.path.exists(file_name[2])

#Nome da database
database_name = 'cnpj.db'

#Download dos arquivos
def download_files():
    #loop para fazer o download de todos os arquivos
    count = 0
    for url in link_cnpj:
        print('Downloading...')
        file = wget.download(url)
        file_path = os.path.basename(file)
        os.rename(file_path, zip_name[count])
        count +=1
        print('{} downloaded file'.format(count))