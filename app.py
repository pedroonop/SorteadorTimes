from flask import Flask, render_template, request, redirect, url_for
from Sorteador import Sorteador

app = Flask(__name__)
sorteador = Sorteador()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/perebas')
def perebas():
	n = request.args.get('n')
	k = request.args.get('k')
	if n and k:
		return redirect(url_for('get_perebas', n = n, k = k))
	return render_template('times_tamanho.html')

@app.route('/perebas/<n>/<k>', methods=["GET"])
def get_perebas(n, k):
	return render_template('lista.html', dados=sorteador.notas, times=int(n), quantidade=int(k))

@app.route('/perebas/<n>/<k>', methods=["POST"])
def post_perebas(n, k):
	jogadores = request.form.getlist('jogador')
	times = sorteador.sortear(jogadores, int(n), int(k))
	return render_template('resultado-sorteio.html', times=times)

if __name__ == '__main__':
	app.run(debug=True)





