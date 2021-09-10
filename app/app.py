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

if __name__ == '__main__':
    app.run(debug=True, port=5000)