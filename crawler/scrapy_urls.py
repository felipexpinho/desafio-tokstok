import requests
from bs4 import BeautifulSoup
import json

def busca(url):
    lista_urls = []
    
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all("script", type="application/ld+json", limit=1)
    content = data[0].get_text()
    json_object = json.loads(content)

    lista_elementos = json_object["itemListElement"]
    
    for item in lista_elementos:
        url_item = item["url"]
        url_item = url_item.replace("/https://portal.vtexcommercestable.com.br", "")
        lista_urls.append(url_item)

    print("Busca\n",lista_urls)
    return lista_urls

busca("https://www.tokstok.com.br/moveis?")
