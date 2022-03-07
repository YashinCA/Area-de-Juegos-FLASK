from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html", phrase="hello", cantidad=3)


@app.route('/play/<numero>')
def play(numero):
    return render_template("index.html", phrase="hello", cantidad=int(numero))


@app.route('/play/<numero>/<nuevocolor>')
def play_dos(numero, nuevocolor):
    return render_template("index.html", nuevocolor=nuevocolor, cantidad=int(numero))


if __name__ == "__main__":
    app.run(debug=True)
