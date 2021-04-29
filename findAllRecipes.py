from selenium import webdriver

# Abre o navegador
chrome = webdriver.Chrome()
chrome.get("https://www.tudogostoso.com.br/receitas?page=1")

# Pega o valor da página atual
paginaAtual = "https://www.tudogostoso.com.br/receitas?page=1".split('=')
paginaAtual = paginaAtual[1]
paginaAtual = int(paginaAtual)

# Lista os links da página atual
listaReceitas = chrome.find_elements_by_class_name('link')
linksReceitas = []

# Define o quão longe a pesquisa irá
NUMERO_DE_ITENS_POR_PAGINA = len(listaReceitas)
QUANTIDADE_DE_PAGINAS_RENDERIZADAS = 2

quantidadeDeReceitas = NUMERO_DE_ITENS_POR_PAGINA * QUANTIDADE_DE_PAGINAS_RENDERIZADAS

# Insere os links na lista
for link in listaReceitas:
    linksReceitas.append(link.get_attribute('href'))

contadorDeLinks = 0

for contadorGeral in range(quantidadeDeReceitas):

    print("CONTADOR DE LINKS: " + str(contadorDeLinks))

    # Verifica se já acabou de percorrer todos os links daquela página
    if((contadorDeLinks) == (quantidadeDeReceitas / QUANTIDADE_DE_PAGINAS_RENDERIZADAS)):
        print("MUDANDO DE PÁGINA")
        paginaAtual += 1
        chrome.get("https://www.tudogostoso.com.br/receitas?page=" + str(paginaAtual))

        listaReceitas = chrome.find_elements_by_class_name('link')

        linksReceitas = []

        for link in listaReceitas:
            linksReceitas.append(link.get_attribute('href'))


    # Pega todas as informações da receita
    for contador in range(len(listaReceitas)):

        # Entra no link da receita
        chrome.get(linksReceitas[contador])

        contadorDeLinks += 1

        # Captura o nome da receita
        nomeReceita = chrome.find_element_by_class_name('recipe-title').text
        print("NOME DA RECEITA: " + nomeReceita)

        # Captura todos os igredientes da receita
        igredientes = chrome.find_elements_by_class_name('p-ingredient')
        for contadorIgrediente in range(len(igredientes)):
            print(igredientes[contadorIgrediente].text)

        