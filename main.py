from fastapi import FastAPI, Query
import requests

app = FastAPI()
@app.get('/api/hello')

def hello():
    '''
    Endpoint padrao!
    '''
    return {'message': 'Hello World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if restaurante is None:
            return {'Dados': data}
        
        dados_restaurante = []
        for item in data:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}