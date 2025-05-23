import random


class Sorteador:
	def __init__(self):
		self.notas = {
			'a': 1.0,
			'b': 2.0,
			'c': 3.0,
			'd': 4.0
		}



	def sortear1(self, lista, n, k):
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

	def sortear(self, lista_, n, k):
		lista = [(i, self.notas[i]) for i in lista_]

		t = 10000

		menor_dif = 1000
		melhor_times = []
		for i in range(t):
			dif, times = self.sortear1(lista, n, k)
			if dif < menor_dif:
				melhor_times = times
				menor_dif = dif

		return melhor_times
		