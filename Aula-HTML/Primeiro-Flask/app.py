from flask import Flask, render_template

# criando aplicação
app = Flask(__name__)


# controller
@app.route('/')
def index():
    return 'Olá, mundo!'


# controller
@app.route('/saudacao')
def saudacao():
    return render_template('saudacao.html')


@app.route('/curso')
def curso():
    return render_template('cursos.html')


# path parameters
@app.route('/curso/<nome_curso>')
def curso_com_nome(nome_curso):
    if nome_curso == 'devweb':
        return render_template('curso_devweb.html')
    elif nome_curso == 'poo':
        return render_template('curso_poo.html')
    else:
        return 'Curso inexistente.'


@app.route('/curso/<nome>/<int:ano>')
def curso_dois_parametros(nome, ano):
    return 'Rota de demonstração que recebe dois valores: nome={0} e ano={1}'.format(nome, ano)


# checando se é o programa principal
if __name__ == '__main__':
    app.run(debug=True)
