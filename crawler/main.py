from scrapy_product import busca
import database as db
import sqlite3
import requests
from bs4 import BeautifulSoup

def main():
    conexao = sqlite3.connect('clients.db')
    
    db.inicializa(conexao)

    busca_paginada("https://www.tokstok.com.br/moveis?")
    
    db.read_all(conexao)
    
    conexao.close()

def busca_paginada(url):
    lista_urls_pag = []
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    #data = soup.find(type="vtex-search-result-3-x-totalProducts--layout pv5 ph9 bn-ns bt-s b--muted-5 tc-s tl t-action--small")
    #print(data)
    for i in range(1,3):
        url_paginada = url + "page=" + str(i)
        for item in busca(url_paginada):
            db.process(conexao, item)

main()
