def prob_9(lado1, lado2, lado3):

	if(lado1 > lado2 and lado2 > lado3):
		hipotenusa = lado1;
		cateto = lado2;
		cateto2 = lado3;
	elif(lado2 > lado1 and lado2 > lado3):
		hipotenusa = lado2;
		cateto = lado1;
		cateto2 = lado3;
	elif(lado3 > lado1 and lado3 > lado2):
		hipotenusa = lado3;
		cateto = lado1;
		cateto2 = lado2;
	else:
		return("No lo es");

	if(hipotenusa**2 == (cateto**2 + cateto2**2)):
		return("Es un triangulo rectangulo");
	else:
		return("No lo es");
