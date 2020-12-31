from flask import Flask, render_template

app = Flask(__name__,template_folder='prueba')

@app.route('/')

def holamundo():
    return 'Hola Mundo!'

@app.route('/prueba')

def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
