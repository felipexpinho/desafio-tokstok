import sqlite3
from product import Product

def insert(conexao, produto):
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO produtos (nome, valor, disponibilidade)
    VALUES (?, ?, ?)
    """, (produto.nome, produto.preco, produto.disponivel))
    conexao.commit()

def process(conexao, produto):
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM produtos WHERE nome=?;
    """, (produto.nome,))

    verify = cursor.fetchall()

    if(not verify):
        insert(conexao, produto)
    else:
        if(not compare(verify[0], produto)):
            print("Produto foi atualizado.")
            update(conexao, produto)

def update(conexao, produto):
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET valor = ?, disponibilidade = ?
    WHERE nome = ?
    """, (produto.preco, produto.disponivel, produto.nome))
    conexao.commit()

def compare(verify, produto):
    return (verify[0] == produto.nome) and (verify[1] == produto.preco) and (verify[2] == produto.disponivel)
                

def read_all(conexao):
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM produtos;
    """)

    for linha in cursor.fetchall():
        print(linha)
    
def inicializa(conexao):
    cursor = conexao.cursor()
    try:
        cursor.execute("""
        CREATE TABLE produtos (
                nome TEXT NOT NULL PRIMARY KEY,
                valor INTEGER,
                disponibilidade BOOLEAN
        );
        """)
    
        print('Tabela criada com sucesso.')
    except:
        print("Tabela já criada.")

def run_db():
    conexao = sqlite3.connect('clients.db')

    inicializa(conexao)
    prod = Product("Felipe", 22, True)
    process(conexao, prod)
    read_all(conexao)

    conexao.close()
