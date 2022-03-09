import requests
from bs4 import BeautifulSoup
from product import Product
import json

def busca(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find("script", type="application/ld+json")
    content = data.get_text()
    json_object = json.loads(content)

    nome = json_object["name"]
    preco = json_object["offers"]["offers"][0]["price"]
    disponivel = json_object["offers"]["offers"][0]["availability"] == 'http://schema.org/InStock'

    return Product(nome, preco, disponivel)
