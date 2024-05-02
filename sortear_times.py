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

#lista de jogadores com nota
lista = [
    ("PV", 4.85),
    ("Manoel", 4.52),
    ("Julio Rocha", 4.46),
    ("Marcelo", 4.35),
    ("Rodrigo Saldanha", 4.35),
    ("Negão", 4.30),
    ("Junior", 4.19),
    ("Roberto", 4.02),
    ("Barbosa", 3.81),
    ("Gustavo", 3.63),
    ("Henrique", 3.19),
    ("Ícaro", 3.11),
    ("Morvan", 2.96),
    ("Capota", 2.50),
    ("Pedro Olímpio", 2.48),
    ("Assis", 2.46),
    ("Eduardo", 2.35),
    ("Davi", 1.78),
    ("Décio", 1.71),
    ("Yago", 1.29)
]

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


