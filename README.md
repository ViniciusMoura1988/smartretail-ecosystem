# SmartCheckout

Sistema de validação de leituras para checkout, desenvolvido como projeto independente de portfólio utilizando Python, FastAPI, SQLite e SQLAlchemy.

O projeto demonstra uma arquitetura de backend capaz de receber uma leitura, validar seu formato, consultar um banco de produtos e retornar uma decisão para o fluxo de checkout.

> **Projeto independente de demonstração e portfólio. Não representa um sistema oficial de nenhuma empresa.**

## Objetivo

O SmartCheckout foi desenvolvido para analisar leituras recebidas durante um processo de checkout e determinar como cada entrada deve ser tratada.

O sistema pode:

* validar códigos GTIN;
* identificar leituras numéricas;
* bloquear leituras identificadas como QR Code ou URL;
* identificar códigos GTIN válidos que não estão cadastrados;
* consultar produtos cadastrados;
* permitir leituras de produtos válidos e cadastrados;
* retornar informações estruturadas para uma interface de checkout.

A proposta é criar uma camada de validação que possa atuar antes da entrada de dados no fluxo normal de compra.

## Como funciona

O fluxo básico é:

1. Uma leitura é recebida.
2. O sistema identifica o tipo de entrada.
3. Códigos de barras numéricos são validados como GTIN.
4. O banco de dados é consultado quando o GTIN é válido.
5. O sistema retorna uma decisão.
6. A interface apresenta o resultado ao operador.

### Possíveis resultados

**Produto cadastrado**

O GTIN é válido e existe no banco de dados.

Resultado:

`permitir`

**Produto não cadastrado**

O GTIN é válido, mas não existe no banco.

Resultado:

`nao_cadastrado`

**QR Code ou URL**

A leitura é identificada como QR Code ou URL e não é tratada como produto.

Resultado:

`qrcode_bloqueado`

**GTIN inválido**

A entrada contém apenas números, mas não possui um dígito verificador válido.

Resultado:

`gtin_invalido`

**Entrada desconhecida**

Quando a entrada não pode ser classificada como um código de produto válido.

Resultado:

`ignorar`

## Arquitetura

O projeto possui uma separação entre backend, banco de dados e interface.

### Backend

Responsável por:

* regras de negócio;
* validação dos códigos;
* API REST;
* consulta ao banco de dados;
* cadastro e gerenciamento de produtos;
* decisão sobre as leituras.

### Banco de dados

Responsável pelo armazenamento dos produtos utilizados na demonstração.

### Frontend

Responsável por:

* receber a leitura;
* enviar os dados para a API;
* apresentar o resultado;
* fornecer uma interface visual para demonstração.

### Simulador

O projeto também possui um simulador de leitor que permite testar diferentes tipos de entrada sem a necessidade de um equipamento físico.

## Tecnologias

* Python 3.13
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* SQLite
* HTML
* CSS
* JavaScript
* Requests

## Banco de dados

O projeto utiliza SQLite através do SQLAlchemy.

A tabela `produtos` possui:

* `id`
* `nome`
* `codigo`
* `preco`

O banco incluído no projeto contém produtos fictícios utilizados exclusivamente para testes e demonstração.

O arquivo `banco_demo.sql` também contém a estrutura e os dados de demonstração necessários para reconstrução do banco.

## API

### Verificar uma leitura

`POST /smartcheckout/ler`

Recebe:

* leitura;
* tipo da leitura.

Exemplo:

`7894900011517`

Tipo:

`codigo_barras`

A API consulta o banco e retorna a decisão correspondente.

### Listar produtos

`GET /produtos`

Retorna os produtos cadastrados no banco.

### Consultar produto

`GET /produtos/{produto_id}`

Consulta um produto específico pelo ID.

### Cadastrar produto

`POST /produtos`

Adiciona um novo produto ao banco.

### Atualizar produto

`PUT /produtos/{produto_id}`

Atualiza um produto existente.

### Excluir produto

`DELETE /produtos/{produto_id}`

Remove um produto do banco.

## Documentação da API

A API utiliza a documentação interativa do FastAPI através do Swagger UI.

Durante a execução local:

`http://127.0.0.1:8000/docs`

A documentação permite visualizar e testar os endpoints diretamente pelo navegador.

## Interface SmartCheckout

O projeto possui uma interface web de demonstração disponível em:

`http://127.0.0.1:8000/interface/`

A interface permite:

* digitar um código;
* simular uma leitura;
* enviar a leitura para a API;
* visualizar o resultado;
* identificar produtos cadastrados;
* identificar produtos não cadastrados;
* visualizar bloqueios e validações.

A interface continuará evoluindo de forma independente da camada principal da API.

## Simulador de leitura

O arquivo `leitor_teste.py` permite simular entradas que poderiam ser recebidas por um leitor ou outra camada de captura.

Para executar:

`python leitor_teste.py`

O simulador identifica automaticamente:

* códigos numéricos;
* URLs;
* entradas desconhecidas.

Depois envia a leitura para a API local.

## Exemplos de teste

### Produto cadastrado

Código:

`7894900011517`

Resultado:

`permitir`

### Produto não cadastrado

Código:

`7894900011524`

Resultado:

`nao_cadastrado`

### QR Code / URL

Entrada:

`https://exemplo.com`

Resultado:

`qrcode_bloqueado`

### GTIN inválido

Código:

`7894900011518`

Resultado:

`gtin_invalido`

### GTIN-8 cadastrado

Código:

`96385074`

Resultado:

`permitir`

### GTIN-12 cadastrado

Código:

`036000291452`

Resultado:

`permitir`

### GTIN-14 cadastrado

Código:

`10614141000415`

Resultado:

`permitir`

## Como executar localmente

### 1. Instalar as dependências

Abra o terminal na pasta do projeto e execute:

`pip install -r requirements.txt`

### 2. Iniciar a API

Execute:

`uvicorn app:app --reload`

### 3. Abrir a documentação

Acesse:

`http://127.0.0.1:8000/docs`

### 4. Abrir a interface

Acesse:

`http://127.0.0.1:8000/interface/`

### 5. Executar o simulador

Com a API em execução, abra outro terminal na pasta do projeto e execute:

`python leitor_teste.py`

## Estrutura do projeto

`app.py`

Backend principal da aplicação e definição dos endpoints.

`banco.db`

Banco SQLite utilizado na demonstração.

`banco_demo.sql`

Script para reconstrução do banco de demonstração.

`frontend/`

Arquivos da interface web do SmartCheckout.

`leitor_teste.py`

Simulador de leituras.

`requirements.txt`

Dependências Python utilizadas pelo projeto.

`.gitignore`

Arquivos e pastas que não devem ser enviados ao controle de versão.

## Status do projeto

Projeto em desenvolvimento.

A versão atual possui:

* backend funcional;
* API REST;
* validação de GTIN;
* banco SQLite;
* CRUD de produtos;
* simulador de leitura;
* interface web de demonstração;
* documentação interativa com Swagger.

As próximas evoluções estão concentradas principalmente na interface do SmartCheckout e em recursos adicionais de demonstração.

## Demonstração online

Uma versão pública de demonstração poderá ser disponibilizada posteriormente através de hospedagem externa.

A intenção é disponibilizar:

* **SmartCheckout API — Swagger UI**
* **SmartCheckout — Demonstração**

sem necessidade de executar o projeto no computador do usuário.

## Autor

Vinicius Moura

Projeto desenvolvido como demonstração prática de desenvolvimento backend, APIs, banco de dados e integração com interface web.
