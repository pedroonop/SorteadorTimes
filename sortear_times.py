import random

def sortear(lista, n, k):
	ordem = [i for i in range(len(lista))]
	random.shuffle(ordem)
	id_times = []
	for i in range(n):
		id_times.append(ordem[i * k:(i + 1)*k])

	times = []
	for i in range(n):
		times.append([])
		for j in id_times[i]:
			times[-1].append(lista[j])

	medias = []
	for time in times:
		medias.append(sum(i for _,i in time) / float(k))

	maior = max(medias)
	menor = min(medias)
	return (maior - menor), times

nota = {
	"Assis": 2.44,
	"Cabral": 4.67,
	"Cadu": 1.56,
	"Davi": 1.78,
	"Decio": 1.56,
	"Dersao": 1.11,
	"Dhonatas": 2.78,
	"Eduardo": 2.44,
	"Gabriel": 2.5,
	"Gustavo": 4.0,
	"Henrique": 3.11,
	"Icaro": 3.22,
	"Jaco": 1.78,
	"Jhonny": 4.56,
	"John Barber": 4.33,
	"Julio": 4.89,
	"Junior": 4.67,
	"Lorhan": 3.44,
	"Luan Barber": 4.22,
	"Lucas Barbosa": 4.0,
	"Lucas Benicio": 2.63,
	"Lucas Santiago": 3.33,
	"Lucca": 2.56,
	"Manoel": 4.89,
	"Marcelo": 4.67,
	"Mateus Felipe": 1.22,
	"Matheus Felipe": 3.44,
	"Matheus Maia": 3.22,
	"Morvan": 3.0,
	"Nicassio": 4.78,
	"Pedro Henrique": 1.67,
	"Pedro Lyvio": 2.75,
	"Pedro Olimpio": 2.67,
	"Pedro Victor": 5.0,
	"Pedro Ygor": 3.11,
	"Roberto": 3.67,
	"Rodrigo Almeida": 1.78,
	"Rodrigo Saldanha": 4.78,
	"Sergio": 4.67,
	"Vinicius": 2.22,
	"Yago": 1.22,
	"Yuri": 1.89
}

for i in lista_:
    if i not in nota:
        print(i, "nao tem nota.")
        exit()

lista_ = []

#lista de jogadores com nota
lista = [(i, nota[i]) for i in lista_]

#quantidade de times
n = 4

#quantidade de jogadores por time
k = 5

if n * k > len(lista):
	print("Faltam jogadores.")
	exit()
if n * k < len(lista):
	print("Tem jogador demais.")
	exit()

#quantidade de formacoes sorteadas
t = 10000

menor_dif = 1000
melhor_times = []
for i in range(t):
	dif, times = sortear(lista, n, k)
	if dif < menor_dif:
		melhor_times = times
		menor_dif = dif


print("Diferenca: " + "{:.3f}".format(menor_dif))
for i in range(len(melhor_times)):
	media = sum(i for _,i in melhor_times[i]) / float(k)
	print("Time " + str(i + 1) + " - Media " + "{:.3f}".format(media))
	for jogador, nota in melhor_times[i]:
		print(jogador, nota)
	print()


