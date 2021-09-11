from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conocimientos = ['python', 'asp', 'mysql', 'sql server']
    data = {
        'titulo': 'Bienvenido',
        'cuerpo': 'Bienvenido a mi pagina!!', 
        'conocimientos': conocimientos
    }
    return render_template('index.html', data=data)

@app.route('/diccionarios.html')
def diccionarios():
    data = {
        'nombre': 'Claudia', 
        'edad': 25,
        'trabaja': True
    }
    return render_template('diccionarios.html', data=data)

@app.route('/listas.html')
def listas():
    data = ['Daniel','Claudia','Jorge','Patricia']
    return render_template('listas.html', data=data)

@app.route('/contacto/<nombre>')
def contacto(nombre):
    data = nombre
    return render_template('contacto.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)