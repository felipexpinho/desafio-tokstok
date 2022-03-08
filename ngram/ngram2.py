import sys

#---------------------- Heapsort ----------------------

def max_heapify(A, B, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        B[i], B[largest] = B[largest], B[i]
        max_heapify(A, B, heap_size, largest)

def build_heap(A, B):
    heap_size = len(A)
    for i in range (int(heap_size/2),-1,-1):
        max_heapify(A, B, heap_size, i)

def heapsort(A, B):
    heap_size = len(A)
    build_heap(A, B)
    #print A #uncomment this print to see the heap it builds
    for i in range(heap_size-1,0,-1):
        A[0], A[i] = A[i], A[0]
        B[0], B[i] = B[i], B[0]
        heap_size -= 1
        max_heapify(A, B, heap_size, 0)

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

# Ordenação
heapsort(listCount, listName)

# Print (Do maior pro menor)
for i in range(len(listName)-1,-1,-1):
    print(listCount[i],"-",listName[i])
