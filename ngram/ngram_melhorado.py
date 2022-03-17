import sys

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
    file = open(sys.argv[1], "r")
except IOError:
    print("Arquivo inexistente")
    exit(1)

#----------------- Alocação dos NGrams -----------------

# Inicializando Dicionario
ngrams = {}

for line in file:
    lineSplit = line.split()
    for i in range(0,len(lineSplit)-(N-1)):
        try:
            # Caso exista o ngram no dicionário, incrementa o contador
            ngrams[' '.join(lineSplit[i:i+N]).lower()]
            ngrams[' '.join(lineSplit[i:i+N]).lower()] += 1
        except:
            # Caso contrário, cria uma nova palavra no dicionário
            ngrams[' '.join(lineSplit[i:i+N]).lower()] = 1

for word, count in sorted(ngrams.items(), key = lambda p:p[1], reverse = True):
    print(count,"-",word)