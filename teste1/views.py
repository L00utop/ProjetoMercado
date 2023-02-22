from django.shortcuts import render
from .models import Produto
import requests 

def request_products():
# Os meios de acesso para a api.
    url = 'https://www.sitemercado.com.br/api/b2c/product/department/alimentos-basicos?store_id=4501'
    headers = {
        'sm-token': '{"IdClientAddress":26670691,"IsDelivery":true,"Location":{"Latitude":-23.1553254,"Longitude":-47.747738999999996},"IdLoja":4501,"IdRede":2571,"DateBuild":"2023-02-17T14:33:47.8748149"}'
    }

# Código que faz a requisição da api via GET.
    produtos=requests.get(url, headers=headers)

# Loop while que itera sobre os produtos retornados da api.
    while True:
            if produtos.json() == "Token_APIB2CInvalid":
                pass
            else:
                for produto in produtos.json().get('products'):

                    descricao = produto['excerpt']
                    preco = produto['price_old']
                    indice_oferta = produto['isSale']

# Declaração que verifica se os produtos estão em oferta ou não.

                    for d in produto['prices']:
                        pass
                    if indice_oferta == 'True':
                        preco = d['price']
                    if indice_oferta == 'False':
                        preco = produto['price_old']

# Função que salva os dados no models que podem ser acessados pelo admin.
                    produtos = Produto.objects.get_or_create(
                        descricao_produto=descricao,
                        defaults={
                        'preco_normal': produto['price_old'],
                        'preco_oferta': d['price'],
                        'indicador_oferta': indice_oferta,
                        }
                    )
                
# Um print dos dados apenas para checar se tudo está sendo requisitado da maneira correta.
                    print(f''' 

                    Descrição: {descricao}
                    
                    Preço normal: {produto['price_old']}

                    Preço: {d['price']}

                    Esta em oferta: {indice_oferta}

                    ''')
            break
request_products()

# Função que irá trabalhar com o html e mostrar os dados na interface.
def list_products(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})
                    
                    
                    
                    
# if preco > 0:
#     preco = produto['price_old']
#     preco = ['price']
#     indice_oferta = True
# else:
#     preco = ['price']
#     preco = 0
#     indice_oferta = False