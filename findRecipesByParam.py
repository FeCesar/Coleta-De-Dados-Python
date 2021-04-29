from selenium import webdriver

# Abre o navegador
chrome = webdriver.Chrome()
chrome.get("https://www.tudogostoso.com.br")

# Seleciona o input de busca
label = chrome.find_element_by_name("q")

# Parametros para a busca
parameters = ["farinha de trigo", "ovo"]
leghtParameters = len(parameters)
find = ""

# Formulação da busca
for parameter in parameters:
    if(leghtParameters == parameters.index(parameter) + 1):
        find += parameter
    else:
        find += parameter + ", "

# Inserindo a busca no input
label.send_keys(find)

# Buscando os parametros
button = chrome.find_element_by_xpath("//*[@id='search']/input[2]")
button.click()

# Listando todos links do resultador
listaReceitas = chrome.find_elements_by_class_name('link')
linksReceitas = []

# Guardando todos os links
for link in listaReceitas:
    linksReceitas.append(link.get_attribute('href'))

# Pegando todas as informações das receitas
for index in range(3):

    # Abrindo os links da linksReceitas
    chrome.get(linksReceitas[index])

    # Coletando o nome da receita
    nomeReceita = chrome.find_element_by_class_name('recipe-title').text
    print("NOME RECEITA: " + str(nomeReceita))

    # Listando os igredientes da receita
    igredientes = chrome.find_elements_by_class_name('p-ingredient')
    for contadorIgrediente in range(len(igredientes)):
            print(igredientes[contadorIgrediente].text)

