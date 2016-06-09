def prob_13:
	cont=0
	suma=0
	for cont in range(1, numero):
		divisor=numero/cont 
		if divisor.is_integer() == True:
			suma+=cont
	return(suma)