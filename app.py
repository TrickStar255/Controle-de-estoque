from flask import Flask, render_template, request, redirect, flash
import json

app = Flask(__name__)
app.secret_key = "123456"

def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            dados = json.load(arquivo)
        
        estoque_normalizado = {}

        for nome, qtd in dados.items():
            nome_normalizado = nome.strip().lower()
            estoque_normalizado[nome_normalizado] = qtd

        return estoque_normalizado
    
    except:
        return{}

def salvar_estoque(estoque):
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)

@app.route("/")
def index():
    estoque = carregar_estoque()
    return render_template("index.html", estoque=estoque)

def normalizar_nome(nome):
    return nome.strip().lower()

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    estoque = carregar_estoque()

    nome = normalizar_nome(request.form["nome"])
    if nome in estoque:
        flash("Produto já está cadastrado!", "danger")
        return redirect("/")
    
    quantidade = int(request.form["quantidade"])

    estoque[nome] = quantidade

    salvar_estoque(estoque)

    return redirect("/")

@app.route("/entrada", methods=["POST"])
def entrada():
    estoque = carregar_estoque()

    nome = normalizar_nome (request.form["nome"])
    quantidade = int(request.form["quantidade"])
    if quantidade < 1:
        return  redirect("/")

    if nome in estoque:
        estoque[nome] += quantidade
        salvar_estoque(estoque)

    return redirect("/")
    
@app.route("/saida", methods=["POST"])
def saida():
    estoque = carregar_estoque()

    nome = normalizar_nome (request.form["nome"])
    quantidade = int(request.form["quantidade"])
    if quantidade < 1:
        return redirect("/")

    if nome in estoque:
        estoque[nome] -= quantidade
        salvar_estoque(estoque)

    return redirect("/")

@app.route("/excluir", methods=["POST"])
def excluir():
    estoque = carregar_estoque()

    nome = normalizar_nome(request.form["nome"])

    if nome in estoque:
        del estoque[nome]
        salvar_estoque(estoque)
    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True)