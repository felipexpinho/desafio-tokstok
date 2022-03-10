import sqlite3
from product import Product

def insert(conexao, produto):
    cursor = conexao.cursor()

    print("Novo produto encontrado:\nNome:",produto.nome,"\nPreco: R$ {:.2f}".format(produto.preco))
    if(produto.disponivel):
        print("Produto disponivel")
    else:
        print("Produto indisponivel")

    cursor.execute("""
    INSERT INTO produtos (nome, valor, disponibilidade)
    VALUES (?, ?, ?)
    """, (produto.nome, produto.preco, produto.disponivel))
    conexao.commit()

def process(conexao, produto):
    print(produto)
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM produtos WHERE nome=?;
    """, (produto.nome,))

    verify = cursor.fetchall()

    if(not verify):
        insert(conexao, produto)
    else:
        if(not compare(verify[0], produto)):
            if(verify[0][1] > produto.preco):
                print("O preco do produto",verify[0][0],"diminuiu de R$ {:.2f} para R$ {:.2f}".format(verify[0][1], produto.preco))
            elif(verify[0][1] < produto.preco):
                    print("O preco do produto",verify[0][0],"aumentou de R$ {:.2f} para R$ {:.2f}".format(verify[0][1], produto.preco))
            if((verify[0][2] != produto.disponivel) and (not verify[0][2])):
                print("O produto",verify[0][0],"ficou disponivel.")
            elif((verify[0][2] != produto.disponivel) and (verify[0][2])):
                print("O produto",verify[0][0],"ficou indisponivel.")
            update(conexao, produto)

def update(conexao, produto):
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET valor = ?, disponibilidade = ?
    WHERE nome = ?
    """, (produto.preco, produto.disponivel, produto.nome))
    conexao.commit()
    print("Produto foi atualizado.")

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

def run_db_test():
    conexao = sqlite3.connect('clients2.db')

    inicializa(conexao)
    prod = Product("Mesa", 25, False)
    process(conexao, prod)
    read_all(conexao)

    conexao.close()
