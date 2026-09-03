from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-super-secreta'

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/painel")
def painel():
    if 'usuario_nome' in session:
        return render_template("painel.html",usuario_nome=session['usuario_nome'],usuario_cpf=session['usuario_cpf'])
    return redirect ('/')

@app.route("/verificar",methods= ['POST'])
def verificar():
    cpf = request.form.get('cpf')
    senha =request.form.get('senha')

    print('Tentando login com:', cpf,'/senha: ', senha)
    
    if cpf =="09876543211" and senha=="1112":
        session['usuario_nome'] = "Ryan"
        session['usuario_cpf'] = cpf
        return redirect('/painel')

    if cpf =="123456789" and senha=="2405":
        session['usuario_nome'] = "Yanni"
        session['usuario_cpf'] = cpf
        return redirect('/painel')


    return redirect('/')

@app.route('/sair')
def sair():
    session.pop('usuario_nome',None)
    session.pop('usuario_cpf',None)
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)