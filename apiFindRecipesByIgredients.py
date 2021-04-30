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
    textJsonIngrediente = ""

    # Captura todos os igredientes da receita
    ingredientes = chrome.find_elements_by_class_name('p-ingredient')
    for contadorIngrediente in range(len(ingredientes)):
        ingrediente = ingredientes[contadorIngrediente].text
        
        if len(ingredientes) == ingredientes.index(ingredientes[contadorIngrediente]) + 1:
            textJsonIngrediente += ingrediente
        else:
            textJsonIngrediente += ingrediente + ", "
    

    textJsonIngrediente = textJsonIngrediente.split(",")


    jsonReceita = {
        "receita": nomeReceita,
        "ingredientes": []
    }

    for index in textJsonIngrediente:
        jsonReceita['ingredientes'] += [index]

        
    return json.dumps(jsonReceita, indent = 2)


if __name__ == "__main__":
    app.run()