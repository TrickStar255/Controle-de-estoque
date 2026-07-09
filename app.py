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
    if quantidade < 0:
        flash("Quantidade não pode ser negativa!", "danger")
        return  redirect("/")

    estoque[nome] = quantidade

    salvar_estoque(estoque)
    flash("Produto cadastrado com sucesso!", "success")
    
    return redirect("/")

@app.route("/entrada", methods=["POST"])
def entrada():
    estoque = carregar_estoque()

    nome = normalizar_nome (request.form["nome"])
    quantidade = int(request.form["quantidade"])
    if quantidade < 1:
        flash("Quantidade inválida!", "danger")
        return  redirect("/")

    if nome in estoque:
        estoque[nome] += quantidade
        salvar_estoque(estoque)
        flash("Entrada registrada com sucesso!", "success")
    else:
        flash("Produto não encontrado!", "danger")

    return redirect("/")
    
@app.route("/saida", methods=["POST"])
def saida():
    estoque = carregar_estoque()

    nome = normalizar_nome (request.form["nome"])
    quantidade = int(request.form["quantidade"])
    if quantidade < 1:
        flash("Quantidade inválida!", "danger")
        return redirect("/")

    if nome in estoque:
        estoque[nome] -= quantidade
        salvar_estoque(estoque)
        flash("Saída registrada com sucesso!", "success")
    else:
        flash("Produto não encontrado!", "danger")

    return redirect("/")

@app.route("/excluir", methods=["POST"])
def excluir():
    estoque = carregar_estoque()

    nome = normalizar_nome(request.form["nome"])

    if nome in estoque:
        del estoque[nome]
        salvar_estoque(estoque)
        flash("Produto excluído com sucesso!", "success")

    else:
        flash("Produto não encontrado!", "danger")
    return redirect("/")


@app.route("/buscar", methods=["POST"])
def buscar():
    estoque = carregar_estoque()
    pesquisa = normalizar_nome(request.form["pesquisa"])
   
    if pesquisa in estoque:
        resultado = {pesquisa: estoque[pesquisa]}
        return render_template ("index.html", estoque=resultado)
    else:
        flash("Produto não encontrado!", "danger")
    return redirect("/")


if __name__ =="__main__":
    app.run(debug=True)