# Descrição
Este script baixa arquivos ZIP da sequencia estabelecimentos do site de dados abertos (gov.br) , descompacta os arquivos e coloca eles em uma pasta chamada "estabelecimentos" dentro de outra pasta chamada "base", registra todos os downloads e descompactação em um arquivo de log com a versão contendo data e hora da execução e finalmente apaga os arquivos zipados.

## Dependências
- Python 3.7+
- requests
- tqdm
- zipfile

## Como usar
1. Certifique-se de ter o Python 3.6 ou superior instalado.
2. Instale as dependências acima.
3. Execute o script em um ambiente Python.

## Log de alterações
- Adicionado a verificação de existência e criação da pasta estabelecimentos dentro da pasta base.
- Adicionado a extração dos arquivos e movimentação para a pasta estabelecimentos dentro da pasta base.
- Adicionado a criação de arquivo de log para registrar os downloads e descompactação.
- Adicionado a exclusão dos arquivos zipados.

## Contribuições
Sinta-se à vontade para contribuir com o código ou enviar relatórios de bugs ou sugestões de melhoria.


## Referência

 - [Dados ZIP de estabelecimento](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica-cnpj)


