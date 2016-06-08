def prob_11(palabra):
	lista = split(palabra)
	for x in range (0, int(len(palabra)/2)):
		if lista[x] != lista[len(palabra)-x]:
			return("No lo es")
	return("Lo es")