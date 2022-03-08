import sys
from collections import Counter

#----------- Verificação de erros na entrada -----------

# Verificação da existência dos dois parâmetros (arquivo e N)
try:
    sys.argv[2]
except:
    print("Os parametros nao foram inicializados corretamente")
    exit(1)

# Verificação se o parâmetro digitado é um número inteiro
if(sys.argv[2].isnumeric()):
    if(int(sys.argv[2]) > 0):
        N = int(sys.argv[2])
    else:
        print("Valor de N invalido")
        exit(1)
else:
    print("Valor de N invalido")
    exit(1)

# Verificação se o arquivo a ser lido existe
try:
    f = open(sys.argv[1], "r")
except IOError:
    print("Arquivo inexistente")
    exit(1)

#----------------- Alocação dos NGrams -----------------

# Lê o conteudo do arquivo
text = f.read()
text = text.split()

# Cria a lista com todos os ngrams e suas quantidades
listWord = Counter([' '.join(text[i:i+N]) for i in range(0,len(text)-(N-1))])

for word, count in listWord.most_common(): # Print ordenado
    print(count,"-",word)
