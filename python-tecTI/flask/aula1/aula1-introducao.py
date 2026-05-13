from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def Fala():
    return 'O que é um decorator?' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/decorator') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def explicar():
    return 'é um padrão de projeto estrutural e um recurso de programação (comum em Python, TypeScript/JavaScript) que permite modificar, estender ou envolver o comportamento de funções, métodos ou classes existentes de forma dinâmica, sem alterar seu código-fonte original.\n* Um decorator (ou decorador) serve para modificar, estender ou envolver o comportamento de funções, métodos ou classes em tempo de execução, sem alterar o código original # Isso é o que será retornado quando a rota /hello for acessada \n *No Flask, um decorator é uma função que envolve (ou "decora") uma função de visualização (view function) para adicionar funcionalidades extras, como definir rotas, autenticar usuários ou gerenciar sessões, usando a sintaxe'



if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
