import requests
import pandas as pd
import time

# --- CONFIGURAÇÕES ---
API_KEY = "INSIRA SUA CHAVE API" # SUA CHAVE API
# Exemplo: Av. Paulista
CENTRO_LAT_LNG = "-23.56068855881027, -46.657508961984945" 
RAIO_EM_METROS = 7000  # 7 km
TIPO_DE_NEGOCIO = "churrascaria" # Outros exemplos: "pizzaria", "hamburgueria", "sushi"
NOME_ARQUIVO_SAIDA = "analise_concorrentes.csv"

# --- FUNÇÃO PARA BUSCAR CONCORRENTES ---
def buscar_concorrentes(api_key, location, radius, keyword):
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    todos_os_lugares = []
    parametros = {
        'location': location,
        'radius': radius,
        'keyword': keyword,
        'key': api_key
    }

    while True:
        print("Buscando dados...")
        response = requests.get(endpoint_url, params=parametros)
        results = response.json()

        if results.get('status') != 'OK':
            print(f"Erro ao buscar dados: {results.get('status')}")
            print(f"Mensagem de erro: {results.get('error_message')}")
            break

        todos_os_lugares.extend(results.get('results', []))
        
        next_page_token = results.get('next_page_token')
        if not next_page_token:
            break
        
        # O Google exige uma pequena pausa antes de buscar a próxima página
        time.sleep(2) 
        parametros['pagetoken'] = next_page_token

    return todos_os_lugares

# --- FUNÇÃO PARA ORGANIZAR E SALVAR OS DADOS ---
def organizar_e_salvar_csv(lugares, filename):
    dados_organizados = []
    for lugar in lugares:
        info = {
            'Nome': lugar.get('name'),
            'Endereço': lugar.get('vicinity'),
            'Latitude': lugar['geometry']['location']['lat'],
            'Longitude': lugar['geometry']['location']['lng'],
            'Avaliação_Media': lugar.get('rating', 'N/A'),
            'Total_Avaliações': lugar.get('user_ratings_total', 'N/A'),
            'Faixa_de_Preço': lugar.get('price_level', 'N/A'),
            'Tipos': ", ".join(lugar.get('types', [])),
            'ID_do_Lugar': lugar.get('place_id') # Útil para buscas futuras
        }
        dados_organizados.append(info)
        
    if not dados_organizados:
        print("Nenhum concorrente encontrado com os critérios fornecidos.")
        return

    df = pd.DataFrame(dados_organizados)
    df.to_csv(filename, index=False, encoding='utf-8-sig', sep=';')
    print(f"Análise de concorrentes salva com sucesso em '{filename}'!")

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    if API_KEY == "SUA_CHAVE_DE_API_VEM_AQUI":
        print("ERRO: Por favor, substitua 'SUA_CHAVE_DE_API_VEM_AQUI' pela sua chave da API do Google Cloud.")
    else:
        concorrentes = buscar_concorrentes(API_KEY, CENTRO_LAT_LNG, RAIO_EM_METROS, TIPO_DE_NEGOCIO)
        if concorrentes:
            organizar_e_salvar_csv(concorrentes, NOME_ARQUIVO_SAIDA)