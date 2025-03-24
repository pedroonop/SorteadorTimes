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
	"Barbosa": 4.20,
	"Junior": 4.60,
	"Capota": 2.10,
	"Sergio": 4.40,
	"Assis": 2.20,
	"Mateus Felipe": 1.30,
	"Matheus Felipe": 3.90,
	"Matheus Araujo": 4.40,
	"Rodrigo Saldanha": 3.90,
	"Rodrigo Almeida": 1.50,
	"Pedro Olimpio": 2.10,
	"Pedro Lyvio": 2.54,
	"Manoel": 4.60,
	"Pedro Henrique": 1.50,
	"Marcelo": 4.10,
	"Felipe Rodrigues": 2.00,
	"Gelderson": 2.73,
	"Roberto Olavo": 1.40,
	"Yago": 1.20,
	"Jean": 1.27,
	"Icaro": 3.30,
	"Yuri": 2.27,
	"Jhony": 4.00,
	"Julio": 4.67,
	"Jaco": 1.65,
	"Perygo": 3.10,
	"Cadu": 1.50,
	"Decio": 1.50,
	"Gabriel": 2.17,
	"Lucas Santiago": 3.80,
	"Lucca": 2.2,
	"Morvan": 3.20,
	"Pedro Victor": 5.00,
	"Roberto Julio": 3.65,
	"Cabral": 4.5,
	"Henrique": 3.10,
	"Israel": 4.2,
	"Pablu": 3.60,
	"Lorhan": 3.30,
	"Marcos Vinicius": 2.43,
	"Paulo Hemesson": 4.00,
	"Romulo": 2.60,
	"Luan": 3.80,
	"John": 3.80,
	"Falcao": 4.60,
	"Avelino": 4.80,
	"Gustavo": 3.30,
	"Uesley": 4.30,
	"Natan Oliveira": 3.60,
	"Magno": 1.50,
	"Lucas Benicio": 2.40,
	"Elixandre": 3.5,
	"Marcelo Barbosa": 2.5,
	"Geova": 2.8,
	"Francisco Pedro": 3.0,
	"Danilo": 2.0,
	"Angelo": 1.1,
	"Gabriel Braga": 2.8,
	"Jacim": 4.6,
	"Pedin": 5.0,
	"Thiago Gimenez": 2.8,
	"Caio Jordan": 3.0,
	"Victor Julio": 1.5,
	"Carlos Victor": 3.0,
	"gabigol": 2.8,
	"Gabriel Silva": 1.2,
	"João Victor": 1.7,
	"Joao Vitor": 2.5,
	"Fabiano": 2.0,
	"Jeferson": 3.3,
	"Gabriel Sudario": 3.2,
	"Leodecio Segundo": 3.8,
	"Ryan": 3.0
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


