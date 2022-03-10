import requests
from bs4 import BeautifulSoup
import json
import lxml

def busca_urls(url):
    lista_urls = []
    
    content = tentativa(url)
    json_object = json.loads(content)

    lista_elementos = json_object["itemListElement"]
    
    for item in lista_elementos:
        url_item = item["url"]
        url_item = url_item.replace("/https://portal.vtexcommercestable.com.br", "")
        lista_urls.append(url_item)

    #print("Busca\n",lista_urls)
    return lista_urls

def tentativa(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    try:
        data = soup.find_all("script", type="application/ld+json")
        content = data[0].get_text()
        return content
    except:
        #print("Tentando novamente.")
        return tentativa(url)
