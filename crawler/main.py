from scrapy_product import busca
from scrapy_urls import busca_urls
import database as db
import sqlite3
import requests
from bs4 import BeautifulSoup
import json

def main():
    conexao = sqlite3.connect('clients.db')
    
    db.inicializa(conexao)

    busca_paginada(conexao, "https://www.tokstok.com.br/moveis?")
    busca_paginada(conexao, "https://www.tokstok.com.br/acessorios?")
    
    db.read_all(conexao)
    
    conexao.close()

def busca_paginada(conexao, url):
    lista_urls_pag = []
    #while(True):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
        #try:
            #data = soup.find_all("span", class_="vtex-search-result-3-x-showingProductsCount b")
            #data = soup.find_all("script")
            #print(data[16])
            #content = data[16].get_text()
            #json_object = json.loads(content)
            #print(json_object["cacheId"])
            #quantidade = data.get_text().split()
            #print(data)
            #nPags = float(quantidade[2])/45
            #print(nPags)
            #break
        #except:
            #print("Tentando novamente.")
    for i in range(1,3): # O range depende de conseguir a busca do número de produtos total daquela categoria.
        url_paginada = url + "page=" + str(i)
        print(url_paginada)
        itens_url = busca_urls(url_paginada)
        if(itens_url):
            for item_url in itens_url:
                produto = busca(item_url)
                db.process(conexao, produto)

main()
