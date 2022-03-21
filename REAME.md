
# Data Engineer Challenge <h1>


### Problema: <h3>

O problema proposto é o desenvolvimento de um pipeline de dados que realiza o
processamento dos dados de empresa, estabelecimento e sócio da base pública de
CNPJs da Receita Federal e disponibiliza em um banco de dados estruturados para
consumo.

### Pontos a cumprir: <h3>

1. Montar um pipeline de dados para processamento da base pública de CNPJs da
Receita Federal e disponibilizar em um banco de dados escolhido pelo
desenvolvedor;

2. Realizar o download automático dos dados diretamente do site da receita;

3. Implementar scheduler para execução periódica. (crontab, windows task
scheduler);

4. O fluxo do projeto deve acompanhar as camadas do datalake. Implementar esse
fluxo na própria máquina. (entender os conceitos do datalake)
Raw -> Standardized -> Conformed -> Aplicação

a. Raw -> Salva os dados baixados no seu formato original;
b. Standardized -> Transforma os arquivos em um formato mais fácil para
leitura;
c. Conformed -> Dado processado para disponibilização na aplicação.
(Padronização do tipo do dado, nome de coluna, melhoria do conteúdo);
d. Aplicação -> Disponibilização no banco de dados.

5. Hospedar o código em um repositório do github utilizando conceitos de Gitflow e
Commit Semântico

### Resolução do Problema: <h3>

O problema foi resolvido por meio de um fluxo em três partes com um laço while:

    1. Identificando a existencia dos arquivos zip no diretório e logo após isso realizando o download dos mesmos por meio de um wget e renomeando o arquivo para deixar em formato padrão.

    2. Realizando a identificação da existencia dos arquivos .zip para realizar o fluxo de descompactar cada um dos arquivos

    3. Finalizando com o tratamento dos dados, inserindo as informações das colunas de cada um dos arquivos e gerando um banco de dados para consulta.


### Tecnologias utilizadas: <h3>

    * Python
    * Pandas


### Autor: <h3>

Cayo Emanuel Dias