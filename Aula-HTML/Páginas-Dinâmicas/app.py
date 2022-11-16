from classes.curso import Curso
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    tit = 'Página Inicial'
    cont = 'Olha só que maneiro.'
    return render_template('index.html', titulo=tit, conteudo=cont)


@app.route('/cursos')
def cursos():
    lista_de_cursos = ['Desenvolvimento Web', 'Programação Orientada a Objetos']
    return render_template('cursos.html', lista=lista_de_cursos)


@app.route('/cursos/<nome>')
def curso_por_nome(nome):
    if nome == 'devweb':
        info = Curso('Desenvolvimento Web', 'Disciplina que lida com as tecnologias da Web')
        habilidades = ['HTML', 'CSS', 'Javascript']
        return render_template('info_curso.html', objeto='info', habilidades=habilidades, dificuldade=2)
    elif nome == 'poo':
        info = Curso('Programação Orientada a Objetos', 'Disciplina que ensina o paradigma orientado a objetos')
        habilidades = ['Dicionários', 'Tratamento de Exceções', 'Classes', 'Herança']
        return render_template('info_curso.html', objeto='info', habilidades=habilidades, dificuldade=1)
    else:
        return 'Curso Inexistente.'


if __name__ == '__main__':
    app.run(debug=True)
