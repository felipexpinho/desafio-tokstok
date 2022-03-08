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
    f = open(sys.argv[1], "r")
except IOError:
    print("Arquivo inexistente")
    exit(1)

#----------------- Alocação dos NGrams -----------------

# Listas para as strings e suas respectivas quantidades
listName = []
listCount = []

text = f.read()
text = text.split()

for i in range(0,len(text)-(N-1)):
    if ' '.join(text[i:i+N]).lower() not in listName:   # Adiciona uma nova string (Não está presente ainda)
        listName.append(' '.join(text[i:i+N]).lower())
        listCount.append(1)
    else:                                       # Incrementa a quantidade (String já está presente)
        listCount[listName.index(' '.join(text[i:i+N]).lower())] += 1

# Prevenção de lista vazia (arquivo txt sem conteúdo)
if not listName:
    exit(0)

# Achando a maior e menor quantidade de repetições de um NGram na lista
maior = listCount[0]
menor = listCount[0]

for i in range(1,len(listCount)):
    if(listCount[i] > maior):
        maior = listCount[i]
    if(listCount[i] < menor):
        menor = listCount[i]

# Print para o usuário, varrendo primeiro a maior quantidade e a cada varredura procura a segunda maior quantidade, terceira e por ai vai
while(maior != -1):
    maiorTemp = -1
    
    for i in range(0,len(listName)):
        if((listCount[i] > maiorTemp) and (listCount[i] < maior)):
            maiorTemp = listCount[i]
        if(listCount[i] == maior):
            print(listCount[i],"-",listName[i])
    maior = maiorTemp
