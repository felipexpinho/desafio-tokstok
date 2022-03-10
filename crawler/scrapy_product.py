import requests
from bs4 import BeautifulSoup
from product import Product
import json
import lxml

def busca(url):
    try:
        html = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }).content
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find("script", type="application/ld+json")
        content = data.get_text()
        json_object = json.loads(content)

        nome = json_object["name"]
        preco = json_object["offers"]["offers"][0]["price"]
        disponivel = json_object["offers"]["offers"][0]["availability"] == 'http://schema.org/InStock'

        return Product(nome, preco, disponivel)
    except:
        print("Falha na busca da url:" + url)
        return None
