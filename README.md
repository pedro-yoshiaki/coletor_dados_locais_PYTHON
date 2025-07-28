# Análise de Concorrência Local com Python e Google Maps API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Ferramenta de automação para coletar dados de estabelecimentos concorrentes em uma área geográfica específica, utilizando a API do Google Places. Os dados são extraídos e salvos em um arquivo `.csv` para fácil análise.

## 📝 Contexto

Todo negócio local, como restaurantes e lojas, precisa entender o cenário competitivo ao seu redor. Realizar essa pesquisa manualmente é um processo lento, repetitivo e sujeito a erros. Este projeto nasceu para automatizar essa tarefa, fornecendo uma base de dados estruturada para análises estratégicas de forma rápida e eficiente.

## ✨ Funcionalidades

* Coleta dados de estabelecimentos com base em uma palavra-chave (ex: "pizzaria", "farmácia").
* Busca em um raio definido a partir de um ponto central (latitude/longitude).
* Extrai informações relevantes como nome, endereço, avaliação média, total de avaliações e tipos de estabelecimento.
* Salva os dados de forma organizada em um arquivo `.csv`, usando `;` como separador para compatibilidade com o Excel em português.
* Gerencia chaves de API de forma segura através de variáveis de ambiente.

## 🛠️ Tecnologias Utilizadas

* **Python 3.9+**
* **Requests:** para realizar as chamadas HTTP para a API do Google.
* **Pandas:** para manipulação e exportação dos dados para o formato `.csv`.
* **Google Cloud Platform:** para acesso e gerenciamento da chave da **Places API**.

## 🚀 Como Usar

Siga as instruções abaixo para configurar e executar o projeto em sua máquina local.

### 1. Pré-requisitos

* Python 3.9 ou superior instalado.
* Uma chave de API do Google Cloud com a **Places API** ativada. [Aprenda a criar uma aqui](https://developers.google.com/maps/documentation/places/web-service/get-api-key).

### 2. Instalação

**a. Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```

**b. Crie e ative um ambiente virtual:**
```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**c. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**d. Configure a Chave de API (Método Seguro):**

Para não expor sua chave no código, vamos usar variáveis de ambiente.

* **No Windows (Terminal atual):**
    ```bash
    set GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
    ```
* **No macOS/Linux (Terminal atual):**
    ```bash
    export GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
    ```
    
    *Para que a variável de ambiente se torne permanente, você deve adicioná-la ao perfil do seu sistema (ex: `.bash_profile`, `.zshrc` ou via "Variáveis de Ambiente do Sistema" no Windows).*
    
    O script foi preparado para ler esta variável.

### 3. Execução

**a. Altere os parâmetros de busca:**

Abra o arquivo `dataCollector.py` e ajuste as seguintes variáveis no início do script:
```python
# --- CONFIGURAÇÕES ---
# Exemplo: Av. Paulista, São Paulo
CENTRO_LAT_LNG = "-23.561399,-46.656536" 
RAIO_EM_METROS = 5000  # 5 km
TIPO_DE_NEGOCIO = "restaurante" # Outros exemplos: "pizzaria", "hamburgueria", "sushi"
NOME_ARQUIVO_SAIDA = "analise_concorrentes.csv"
```

**b. Rode o script:**
```bash
python dataCollector.py
```

Ao final da execução, o arquivo `analise_concorrentes.csv` será criado no mesmo diretório, pronto para ser aberto no Excel ou Google Sheets.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Criado por **Pedro Yoshiaki** - [LinkedIn](https://www.linkedin.com/in/pedro-yoshiaki/)
