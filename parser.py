def pre_process(letra):
	l = letra.lower()

	if (l == 'á') | (l == 'â'):
		return 'a'
	if (l == 'é') | (l == 'ê'):
		return 'e'
	if (l == 'í') | (l == 'î'):
		return 'i'
	if (l == 'ó') | (l == 'ô'):
		return 'o'
	if (l == 'ú') | (l == 'û'):
		return 'u'

	return l

def processa_palavra(palavra):
	return ''.join(pre_process(i) for i in palavra)

def distancia_edicao(a, b):
	n, m = len(a), len(b)
	M = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

	for i in range(n + 1):
		M[i][0] = i

	for j in range(m + 1):
		M[0][j] = j

	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if a[i - 1] == b[j - 1]:
				M[i][j] = M[i - 1][j - 1]
			else:
				M[i][j] = 1 + min(M[i - 1][j], M[i][j - 1])

	return M[n][m]

def converte(base, lista_):

	i = lista_.index('1-')
	if 'LISTA DE' in lista_:
		f = lista_.index('LISTA DE')
	else:
		f = len(lista_)

	lista_pre = lista_[i:f].split('-')[1:]

	for i in range(len(lista_pre)):
		lista_pre[i] = processa_palavra(lista_pre[i])

	print(lista_pre)

	result = []
	for nome in lista_pre:
		menor_dif = 10000
		r = ''
		for compara_ in base:
			if compara_ in result:
				continue

			compara = processa_palavra(compara_)
			x = distancia_edicao(compara, nome)
			# if nome == "manoel hudson":
				# print(compara, x)
			if x < menor_dif:
				menor_dif = x
				r = compara_

		result.append(r)

	return result
