from flask import Flask, render_template, request
from model import model
import this

this.modelo = model() 
this.nome =     ""
this.telefone = ""
this.data =     ""
this.dados =    ""

pessoa = Flask(__name__)

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome       = request.form['tNovoNome']
        this.telefone   = request.form['tNovoTelefone']
        this.endereco   = request.form['tNovoEndereco']
        this.data       = request.form['tNovaData'] 
        this.dados      = this.modelo.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo="Banco de Deidos", resultado=this.dados)

@pessoa.route('/consultar.html', methods=['GET','POST'])
def consultarTudo():
    if request.method == 'POST':
        this.codigo = request.form['tNovoDado']
        this.msg = this.modelo.consultar()
    return render_template('consultar.html', titulo="Consultar", dados=this.msg)

if __name__ == "__main__":
    pessoa.run(debug=True, port=5000)
