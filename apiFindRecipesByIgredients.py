from flask import Flask
from selenium import webdriver
import json

app = Flask(__name__)

@app.route("/")
def hello():
    # Abre o navegador
    chrome = webdriver.Chrome()
    chrome.get("https://www.tudogostoso.com.br/receitas?page=1")

    # Lista os links da página atual
    listaReceitas = chrome.find_elements_by_class_name('link')
    linksReceitas = []

    # Insere os links na lista
    for link in listaReceitas:
        linksReceitas.append(link.get_attribute('href'))

    # Entra no link da receita
    PRIMEIRA_RECEITA = 0
    chrome.get(linksReceitas[PRIMEIRA_RECEITA])

    # Captura o nome da receita
    nomeReceita = chrome.find_element_by_class_name('recipe-title').text
    print("NOME DA RECEITA: " + nomeReceita)

    # Instancia os igredientes
    textJsonIgrediente = ""

    # Captura todos os igredientes da receita
    igredientes = chrome.find_elements_by_class_name('p-ingredient')
    for contadorIgrediente in range(len(igredientes)):
        igrediente = igredientes[contadorIgrediente].text
        
        if len(igredientes) == igredientes.index(igredientes[contadorIgrediente]) + 1:
            textJsonIgrediente += igrediente
        else:
            textJsonIgrediente += igrediente + ", "
    

    textJsonIgrediente = textJsonIgrediente.split(",")


    jsonReceita = {
        "receita": nomeReceita,
        "igredientes": []
    }

    for index in textJsonIgrediente:
        jsonReceita['igredientes'] += [index]

        
    return json.dumps(jsonReceita, indent = 2)


if __name__ == "__main__":
    app.run()