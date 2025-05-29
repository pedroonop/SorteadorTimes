from flask import Flask, render_template, request, redirect, url_for
import json
from resources.sorteador import Sorteador
from resources.notas_perebas import notas
from resources.parser import converte

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
	return render_template('home.html')

@app.route('/perebas/')
def perebas():
	sorteador = Sorteador(notas)
	return render_template('lista.html', dados = sorteador.notas)


@app.route('/arquivo/', methods=["POST"])
def sorteado_arquivo():
	jogadores = json.loads(request.files["jogadores.json"].read())
	sorteador = Sorteador(jogadores)
	n = int(request.form.get('n'))
	k = int(request.form.get('k'))
	medias, times = sorteador.sortear(jogadores.keys(), n, k)
	return render_template('resultado-sorteio.html', times=times, medias=medias)

@app.route('/manual/', methods=["POST"])
def sorteado_manual():
	n = int(request.form.get('n'))
	k = int(request.form.get('k'))

	dic = {}
	jogadores=[]
	for i in range(n * k):
		jogador = request.form.get('jogador_' + str(i))
		nota = float(request.form.get('nota_' + str(i)))
		jogadores.append(jogador)
		dic[jogador] = nota

	sorteador = Sorteador(dic)
	medias, times = sorteador.sortear(jogadores, n, k)
	return render_template('resultado-sorteio.html', times=times, medias=medias)


@app.route('/perebas/manual/', methods=["POST"])
def sorteado_perebas():
	n = int(request.form.get('n'))
	k = int(request.form.get('k'))

	jogadores=[]
	for i in range(n * k):
		jogador = request.form.get('jogador_' + str(i))
		jogadores.append(jogador)

	sorteador = Sorteador(notas)
	medias, times = sorteador.sortear(jogadores, n, k)
	return render_template('resultado-sorteio.html', times=times, medias=medias)

@app.route('/perebas/arquivo/', methods=["POST"])
def sorteado_lista_perebas():
	n = int(request.form.get('n'))
	k = int(request.form.get('k'))
	lista = request.form.get('lista')

	jogadores = converte(notas.keys(), lista)
	sorteador = Sorteador(notas)
	medias, times = sorteador.sortear(jogadores, n, k)
	return render_template('resultado-sorteio.html', times=times, medias=medias)

if __name__ == '__main__':
	app.run(debug=True)





