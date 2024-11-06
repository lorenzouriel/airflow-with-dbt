# ETL with PostgreSQL, DuckDB and Data Contracts with Airflow and Astro CLI

![architecture](/docs/imgs/architecture.png)

This README provides instructions for configuring and running this solution, which uses [Astro CLI](https://docs.astronomer.io/astro/cli), Docker, and Airflow. It also explains how to configure connectors in Airflow to test the flow and how to deploy to [Astronomer](https://www.astronomer.io/).

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running
- [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) installed
- Account on [Astronomer](https://www.astronomer.io/) to perform the deployment
- Python 3.11.5

### Step 1: Configuring and Running Astro CLI with Docker

1. **Clone the repository** and access the project directory:
```bash
   git clone https://github.com/lorenzouriel/airflow-with-duckdb
   cd airflow-with-duckdb
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Start Astro CLI:** To test the solution locally, use Astro CLI with Docker.
```bash
astro dev start
```

This will launch an Airflow development environment using Docker.

4. **Access Airflow** locally at http://localhost:8080 to view and test the DAGs.

### Step 2: Configuring Connectors in Airflow

For DAG to work correctly, you need to configure two connections in Airflow:
- `my_motherduck_conn`: The motherduck connection.
- `my_postgresdb_conn`: The postgres connection.


Go to the **Admin > Connections > Add (+) > Connection Type (Postgres / Duckdb)** tab in Airflow and fill in the necessary information.

### Step 3: Deploy to Astronomer
When you are ready to deploy to the production environment, follow the steps below.

1. **Authenticate yourself to Astronomer:**
```bash
astro login astronomer.io
```

2. **Prepare for Deploy:**
```bash
astro deploy --dags
```

## Explaining ETL
**1. Extract:** The first step involves extracting data from an external API. This extraction process uses Python to obtain the data and prepare it for transformation.

**2. Transform:** The extracted data undergoes a transformation also carried out in Python. At this stage, data can be cleaned, filtered, validated against data contracts and prepared to be loaded into the next PostgreSQL.

**3. Load:** After transformation, the data is loaded into PostgreSQL, using Astro CLI and Aiflow to orchestrate and monitor this process.

**4. Extract and Load (Batch):** Periodically, there is a batch extraction of PostgreSQL data, which is loaded into the MotherDuck platform for analysis and long-term storage.

**5. Architecture:** We see three fundamental tools for this process:
- Apache Airflow and Astro CLI for ETL orchestration.
- Astronomer as the platform to facilitate the use of Airflow.
- Docker to contain and manage project dependencies, ensuring development and production environments are consistent.

## Main Points of the Solution

### Architecture Based on MVC and Data Contracts
This solution adopts an MVC (Model-View-Controller) approach to Airflow, which facilitates the organization and validation of data through clear and well-defined data contracts. This model allows you to centralize validations, ensuring that data complies with requirements before being processed. Furthermore, the use of Airflow is focused exclusively on orchestrating workflows and executing DAGs, without dependence on specific native operators, making the system more flexible and scalable.

### DuckDB Custom Operator
Another strong point of the solution is the creation of a custom operator in Airflow. This operator was developed to meet specific application needs, providing a deeper understanding of how operators work in Airflow. Customization allows the solution to work autonomously, without depending on external tools, increasing the flexibility to adapt the ETL as new requirements arise.

> **PORTUGUÊS**

# ETL com PostgreSQL, DuckDB e Contratos de Dados com Airflow e Astro CLI

![architecture](/docs/imgs/architecture.png)

Este README fornece as instruções para configurar e executar esta solução, que utiliza o [Astro CLI](https://docs.astronomer.io/astro/cli), Docker, e Airflow. Ele também explica como configurar conectores no Airflow para testar o fluxo e como fazer o deploy para o [Astronomer](https://www.astronomer.io/).

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado e em execução
- [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) instalado
- Conta no [Astronomer](https://www.astronomer.io/) para realizar o deploy
- Python 3.11.5

### Passo 1: Configuração e Rodando o Astro CLI com Docker

1. **Clone o repositório** e acesse o diretório do projeto:
```bash
   git clone https://github.com/lorenzouriel/airflow-with-duckdb
   cd airflow-with-duckdb
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Inicie o Astro CLI:** Para testar a solução localmente, utilize o Astro CLI com Docker.
```bash
astro dev start
```

Isso iniciará um ambiente de desenvolvimento com Airflow usando o Docker.

4. **Acesse o Airflow** localmente em http://localhost:8080 para visualizar e testar as DAGs.

### Passo 2: Configuração dos Conectores no Airflow

Para que a DAG funcione corretamente, você precisa configurar duas conexões no Airflow:
- `my_motherduck_conn`: A conexão do motherduck.
- `my_postgresdb_conn`: A conexão do postgres.


Vá até a aba **Admin > Connections > Add (+) > Connection Type (Postgres / Duckdb)** no Airflow e preencha as informações necessárias.

### Passo 3: Deploy para o Astronomer
Quando estiver pronto para realizar o deploy para o ambiente de produção, siga os passos abaixo.

1. **Autentique-se no Astronomer:**
```bash
astro login astronomer.io
```

2. **Prepare o Deploy:**
```bash
astro deploy --dags
```

## Explicando o ETL
**1. Extract:** A primeira etapa envolve a extração de dados de uma API externa. Esse processo de extração utiliza Python para obter os dados e prepará-los para transformação.

**2. Transform:** Os dados extraídos passam por uma transformação também realizada em Python. Nessa etapa, os dados podem ser limpos, filtrados, validados em contratos de dados e preparados para serem carregados no próximo PostgreSQL.

**3. Load:** Após a transformação, os dados são carregados em um PostgreSQL, utilizando Astro CLI e Aiflow para orquestrar e monitorar esse processo.

**4. Extract e Load (Batch):** Periodicamente, há uma extração em lote dos dados do PostgreSQL, que são carregados na plataforma MotherDuck para análise e armazenamento em longo prazo.

**5. Arquitetura:** Vemos três ferramentas fundamentais para esse processo:
- Apache Airflow e Astro CLI para a orquestração do ETL.
- Astronomer como a plataforma para facilitar o uso do Airflow.
- Docker para conter e gerenciar as dependências do projeto, garantindo que os ambientes de desenvolvimento e produção sejam consistentes.

## Pontos Fortes da Solução

### Arquitetura Baseada em MVC e Contratos de Dados
Essa solução adota uma abordagem MVC (Model-View-Controller) no Airflow, o que facilita a organização e validação dos dados através de contratos de dados claros e bem definidos. Esse modelo permite centralizar as validações, garantindo que os dados estejam em conformidade com os requisitos antes de serem processados. Além disso, o uso do Airflow é focado exclusivamente na orquestração de workflows e execução de DAGs, sem dependência de operadores nativos específicos, tornando o sistema mais flexível e escalável.

### Operador Customizado do DuckDB
Outro ponto forte da solução é a criação de um operador customizado no Airflow. Esse operador foi desenvolvido para atender a necessidades específicas da aplicação, proporcionando uma compreensão mais profunda do funcionamento dos operadores no Airflow. A customização permite que a solução funcione de forma autônoma, sem depender de ferramentas externas, ampliando a flexibilidade para adaptar o ETL conforme novos requisitos surgirem.