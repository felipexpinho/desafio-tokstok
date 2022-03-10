Para rodar o sistema, execute o arquivo main.py.
OBS.: Para rodar na linha de comando, utilize o comando "python3 main.py" (Podendo ser diferente de acordo com o Python instalado em sua máquina)

O arquivo database.py consiste nas funções responsáveis por manipular o banco de dados e apresentar os respectivos eventos a cada varredura.

O arquivo product.py possui o esqueleto da classe na qual serão gerados os produtos.

O arquivo scrapy_product.py possui a função responsável por procurar na página do produto as informações desejadas e retornar um objeto Produto contendo essas informações.

O arquivo scrapy_urls consiste nas funções responsáveis pela busca de todas as urls de cada produto individualmente a partir da página de apresentação de 45 produtos.
OBS.: Por algum motivo que ainda não descobri, a lista de URLs retorna vazia na maior parte dos casos, então foi necessária uma função em loop que continua tentando até conseguir a informação.

O arquivo main.py é responsável por inicializar todo o processo, gerando o banco de dados e procurando pelas urls.
OBS.: Não consegui resgatar a quantidade total de produtos de cada categoria a partir do HTML (As tentativas sempre estão retornando listas nulas, e ainda não descobri qual é exatamente o problema)