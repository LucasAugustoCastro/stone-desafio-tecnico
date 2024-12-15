# Pedra Pagamentos - Desafio Técnico

## Introdução

O time de controle da companhia Pedra Pagamentos é responsável por efetuar o acompanhamento de todos os KPIs e OPIs, de modo a garantir que as metas estabelecidas serão atingidas. A companhia ainda é uma Startup, e muitos processos precisam ser amadurecidos, pois são manuais e demorados.

Você é responsável por automatizar o processo de cálculo de alguns indicadores da operação. Se for bem sucedido, os analistas poderão investir mais tempo na análise de dados (hoje esse tempo é desperdiçado com extração e tratamento de dados para que sejam posteriormente apurados).

Neste primeiro momento o foco será a automatização dos indicadores da operação de Last Mile. São eles:
- Produtividade por Green Angel
- SLA de cada base logística
- SLA de cada Green Angel

## Estrutura do Projeto
```
├── Dockerfile
├── README.md
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 0e8424471d84_criar_tabela_atendimento.py
│       ├── 4a870803f55b_criar_tabela_usuario.py
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── controllers
│   │   ├── atendimentos.py
│   │   └── usuarios.py
│   ├── models
│   │   ├── atendimentos.py
│   │   └── usuarios.py
│   ├── repository
│   │   └── atendimentos.py
│   ├── routes
│   │   ├── atendimentos.py
│   │   ├── auth.py
│   │   └── usuarios.py
│   ├── schema
│   │   ├── atendimentos.py
│   │   └── usuarios.py
│   └── scripts
│       ├── __init__.py
│       └── load_csv.py
├── docker-compose.yml
├── requirements.txt
├── run.py
└── tests
    ├── __init__.py
    ├── integration
    │   ├── __init__.py
    │   └── atendimento_test.py
    ├── repository
    │   └── atendimentos_fake.py
    └── unit
        ├── __init__.py
        └── atendimento_test.py
```
## Instalação e Execução

### Pré-requisitos

- Docker
- Docker Compose
- Python3

### Passos

1. Clone o repositório:
   ```sh
   git clone https://github.com/LucasAugustoCastro/stone-desafio-tecnico.git
   cd stone-desafio-tecnico
3. Construa e inicie os containers Docker:
    ```
    docker-compose up --build
    ```
4. Acesse a API em http://localhost:5000.

## Carregar Dados do CSV
Para carregar os dados do CSV no banco de dados, execute o seguinte comando:
1. Crie o ambiente virtual:
    ```
    python3 -m venv .venv
    ```
2. Ative o ambiente virtual:
    ```
    source .venv/bin/activate
    ```
3. Instale as dependencias:
    ```
    pip install -r requirements.txt
    ```
4. Execute o comando para carregar a base csv:
    ```
    python app/script/load_csv.py /path/to/your/csvfile.csv
    ```

## Executar Testes
1. Com o ambiente virtual criado e dependencias instaladas, execute o seguinte comando para executar os testes:
    ```
    pytest
    ```

## Endpoints da API
### Autenticação
- ```POST /auth/login```: Autenticação de usuário.
### Usuários
- ```GET /usuarios```: Listar usuários.
- ```POST /usuarios```: Criar um novo usuário.
- ```GET /usuarios/<id>```: Obter detalhes de um usuário.
- ```PATCH /usuarios/<id>```: Atualizar um usuário.
- ```DELETE /usuarios/<id>```: Deletar um usuário.
### Atendimentos
- ```GET /atendimentos```: Listar atendimentos com filtros.
- ```POST /atendimentos```: Criar um novo atendimento.
- ```PATCH /atendimentos/<id>```: Atualizar um atendimento.
### Contribuição
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (```git checkout -b feature/nova-feature```).
3. Commit suas mudanças (```git commit -am 'Adiciona nova feature'```).
4. Faça o push para a branch (```git push origin feature/nova-feature```).
5. Abra um Pull Request.
