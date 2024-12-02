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
	"Davi": 1.50,
	"Barbosa": 4.00,
	"Junior": 4.50,
	"Capota": 2.25,
	"Sergio": 4.25,
	"Assis": 2.08,
	"Mateus Felipe": 1.08,
	"Matheus Felipe": 3.33,
	"Matheus Araujo": 4.25,
	"Rodrigo Saldanha": 4.08,
	"Rodrigo Almeida": 1.50,
	"Pedro Olimpio": 2.08,
	"Pedro Livyo": 2.54,
	"Manoel": 4.67,
	"Pedro Henrique": 1.9,
	"Marcelo": 4.25,
	"Felipe Rodrigues": 2.18,
	"Gelderson": 2.73,
	"Roberto Olavo": 1.40,
	"Yago": 1.08,
	"Jean": 1.27,
	"Icaro": 3.33,
	"Yuri": 2.27,
	"Jhony": 4.00,
	"Julio": 4.67,
	"Jaco": 1.75,
	"Perygo": 3.00,
	"Cadu": 1.67,
	"Decio": 1.50,
	"Gabriel": 2.17,
	"Lucas Santiago": 3.67,
	"Lucca": 2.33,
	"Morvan": 3.08,
	"Pedro Victor": 5.00,
	"Roberto Julio": 3.58,
	"Cabral": 4.5,
	"Henrique": 3.08,
	"Israel": 3.92,
	"Pablu": 3.42,
	"Kaynnan": 3.00,
	"Lorhan": 3.33,
	"Marcos Vinicius": 2.43,
	"Nicacio": 4.42,
	"Paulo Hemesson": 4.00,
	"Romulo": 2.30,
	"Luan": 3.80,
	"John": 3.78,
	"Falcao": 4.60,
	"Avelino": 4.80,
	"Gustavo": 3.80,
	"Uesley": 4.30,
	"Natan Oliveira": 3.60,
	"Magno": 1.50,
	"Lucas Benicio": 2.20
}

lista_ = []

for i in lista_:
    if i not in nota:
        print(i, "nao tem nota.")
        exit()

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


