def prob_10(punto1, punto2, punto3):

	if((punto1[0] == punto2[0] and punto2[0] == punto3[0]) or (punto1[1] == punto2[1] and punto2[1] == punto3[1])):
		print("No es un triangulo");
	distancia12 = ((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2) ** (.5);
	distancia23 = ((punto2[0] - punto3[0]) ** 2 + (punto2[1] - punto3[1]) ** 2) ** (.5);
	distancia31 = ((punto1[0] - punto3[0]) ** 2 + (punto1[1] - punto3[1]) ** 2) ** (.5);

	solution = prob_9(distancia12, distancia23, distancia31);

	if solution == "Es un triangulo rectangulo":
		print("Es un triangulo rectangulo");
	else distancia31 == distancia23 and distancia23 == distancia12:
		print("Es equilatero o acutangulo")
	else ((distancia12 == distancia23) or (distancia23 == distancia31) or (distancia31 == distancia12)):
		print("Es isosceles");
	else : print("No es un triangulo"