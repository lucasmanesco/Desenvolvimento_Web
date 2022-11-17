from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'SENHA-MUITO-SECRETA'


@app.route('/exemplo_get')
def exemplo_get():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    if usuario and senha:
        return 'Os dados recebidos são: usuario={0} e senha={1}'.format(usuario, senha)
    else:
        return render_template('exemplo_get.html')


@app.route('/exemplo_post', methods=["GET", "POST"])
def exemplo_post():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario and senha:
        return 'Os dados recebidos são: usuario={0} e senha={1}'.format(usuario, senha)
    else:
        return render_template('exemplo_post.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    msg_erro = ''
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == 'lucas' and senha == '1234':
            session['usuario'] = 'lucas'
            return redirect('/area_logada')
        elif usuario == 'maria' and senha == '4321':
            session['usuario'] = 'maria'
            return redirect('/area_logada')
        else:
            msg_erro = 'Usuário e/ou senha inválidos.'
    return render_template('login.html', erro=msg_erro)


@app.route('/area_logada')
def area_logada():
    if 'usuario' in session:
        nome_aluno = ''
        media_aluno = 0.0
        if session['usuario'] == 'lucas':
            nome_aluno = 'Lucas Soares Manesco'
            media_aluno = 8.0
        elif session['usuario'] == 'maria':
            nome_aluno = 'Maria dos Santos'
            media_aluno = 9.5
        return render_template('area_logada.html', nome=nome_aluno, media=media_aluno)
    else:
        return redirect('/login')


@app.route('/sair')
def sair():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)