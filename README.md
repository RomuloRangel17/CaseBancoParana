# Automação API - /Automation/tests/case_api_automation_PB.py
Este script Python realiza testes nos verbos HTTP (GET, POST, PUT, DELETE) em uma API utilizando a biblioteca `requests` e `jsonschema` para validar o JSON retornado.
O objetivo deste script é verificar se os endpoints da API retornam os resultados esperados e se o JSON retornado atende ao esquema especificado.

# Automação Web - /Automation/tests/case_web_automation_PB.py
Este script em Python utiliza Selenium para realizar automação na interface web do site "[The Internet](https://the-internet.herokuapp.com/challenging_dom)". O script clica em três botões diferentes na página principal e, para cada botão, realiza ações adicionais, clicando nos botões "Edit" e "Delete" em uma tabela.

# Estudo de caso - Case/Case.pdf
Esse arquivo pdf tem como objetivo demonstrar os cenários de testes desenhados, baseado no caso proposto na atividade 1. Para isso, foram abordados:

- Estratégia de teste
- Abordagens de teste
- Tipos/níveis de teste
- Ferramentas
- Atuação

## Pré-requisitos

- [Python](https://www.python.org/downloads/): Certifique-se de ter o Python instalado.
- [WebDriver para Chrome](https://sites.google.com/chromium.org/driver/): Faça o download do WebDriver do Chrome e adicione-o ao seu PATH.

## Instalação

Clone este repositório e instale as dependências necessárias usando o seguinte comando:
https://github.com/RomuloRangel17/CaseBancoParana.git

- pip install requests jsonschema
- pip install selenium

## Execução
Feito a instalação dos pacotes necessários e o clone do projeto, dentro da pasta do projeto, basta executar os seguintes comandos:

```bash
- python ./case_api_automation_PB.py
- python ./case_web_automation_PB.py
