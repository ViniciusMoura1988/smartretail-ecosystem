# SmartCheckout

Sistema de validação de leituras para checkout, desenvolvido como projeto de backend com Python, FastAPI, SQLite e SQLAlchemy.

## 🚀 Demonstrações online

### Clique aqui para ver as demonstrações

[![Documentação da API](https://img.shields.io/badge/VER%20DOCUMENTAÇÃO%20DA%20API-Swagger-85EA2D?style=for-the-badge\&logo=swagger\&logoColor=black)](https://smartcheckout-hqiv.onrender.com/docs)

[![Interface do SmartCheckout](https://img.shields.io/badge/ABRIR%20INTERFACE%20DO%20SMARTCHECKOUT-Interface-000000?style=for-the-badge\&logo=html5\&logoColor=white)](https://smartcheckout-hqiv.onrender.com/interface/)

A demonstração online permite visualizar o funcionamento do projeto sem necessidade de executar o sistema localmente.

* **Documentação da API:** acesso ao Swagger para visualizar e testar os endpoints.
* **Interface do SmartCheckout:** tela visual para realizar testes de leitura e visualizar os resultados.

> **Observação:** a aplicação está hospedada gratuitamente no Render. A instância pode entrar em modo de inatividade após um período sem acesso, fazendo com que o primeiro carregamento possa levar alguns segundos.

## Objetivo

O SmartCheckout foi desenvolvido para analisar uma leitura recebida no checkout e decidir se ela deve ser permitida, ignorada ou identificada como produto não cadastrado.

A proposta é criar uma camada de validação que possa atuar antes da entrada de dados no fluxo normal de compra.

## Tecnologias

* Python 3.13
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* SQLite
* HTML, CSS e JavaScript
* Requests

## Como funciona

O sistema trabalha com três tipos de leitura:

* `codigo_barras`
* `qrcode`
* `desconhecido`

### Código de barras

Um código de barras é validado como GTIN.

Se o GTIN for válido e estiver cadastrado no banco de dados, a leitura é permitida.

Se o GTIN for válido, mas não estiver cadastrado, o sistema informa que o produto não está cadastrado.

Se o código for numérico, mas possuir um GTIN inválido, a leitura é ignorada.

### QR Code

Leituras identificadas como QR Code são bloqueadas pelo backend.

Isso impede que uma URL ou outro conteúdo de QR Code seja tratado como produto.

### Tipo desconhecido

Quando não é possível identificar corretamente o tipo da leitura, o backend também impede que ela seja tratada como um produto válido.

## Arquitetura

O projeto mantém uma separação entre backend e interface.

### Backend

Responsável por:

* regras de negócio
* validação dos códigos
* API
* acesso ao banco de dados
* consulta dos produtos
* decisão sobre a leitura

### Frontend

Responsável por:

* interface visual
* entrada da leitura
* comunicação com a API
* apresentação do resultado

Essa separação permite que a camada de backend permaneça independente do equipamento utilizado no checkout.

## Banco de dados

O projeto utiliza SQLite através do SQLAlchemy.

A tabela de produtos contém:

* ID
* nome
* código GTIN
* preço

O banco utilizado no projeto é `banco.db`.

## API

A API possui endpoints para:

* verificar uma leitura do SmartCheckout
* listar produtos
* consultar produto por ID
* cadastrar produto
* atualizar produto
* excluir produto

### Documentação online

A documentação interativa da API está disponível através do Swagger:

https://smartcheckout-hqiv.onrender.com/docs

### Documentação local

Quando o projeto estiver sendo executado no computador:

`http://127.0.0.1:8000/docs`

## Interface online

A interface visual do SmartCheckout está disponível em:

https://smartcheckout-hqiv.onrender.com/interface/

### Interface local

Quando o projeto estiver sendo executado no computador:

`http://127.0.0.1:8000/interface/`

## Como executar

Abra o terminal na pasta do projeto:

`C:\Users\moura\dia-a-dia-api`

Inicie a API:

`uvicorn app:app --reload`

Depois acesse:

`http://127.0.0.1:8000/docs`

Para utilizar a interface visual:

`http://127.0.0.1:8000/interface/`

## Simulador

O projeto também possui o arquivo `leitor_teste.py`, utilizado para simular leituras que posteriormente poderiam ser recebidas por uma camada de captura ou equipamento de checkout.

Para executar:

`python leitor_teste.py`

O simulador identifica automaticamente leituras numéricas, URLs e conteúdos desconhecidos antes de enviá-las para a API.

## Exemplos

### Produto cadastrado

`7894900011517`

Resultado:

`permitir`

### Produto não cadastrado

`7894900011524`

Resultado:

`nao_cadastrado`

### QR Code / URL

`https://exemplo.com`

Resultado:

`qrcode_bloqueado`

### GTIN inválido

`7894900011518`

Resultado:

`gtin_invalido`

## Estrutura do projeto

```text
smartretail-ecosystem/
│
├── app.py
├── banco.db
├── banco_demo.sql
├── leitor_teste.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── frontend/
│   └── index.html
│
└── Ecossistema SmartRetail - Atacadão Dia a Dia.pdf
```

## Status

Projeto em desenvolvimento.

A versão atual concentra-se na construção e validação do backend, banco de dados, API, simulador e interface de demonstração.

A versão online está disponível para demonstração através do Render.

## Autor

Vinicius Moura
