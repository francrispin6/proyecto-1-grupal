def prob_7(numero, multiple):
   
    resido = numero % multiple
    if resido == 0:
        return True
    else:
        return False
lista1=[]
lista2=[]
for i in range(1,1001):
    if multiple(i,4):
        lista1.append(i)
 
    if multiple(i,7):
        lista2.append(i)
lista1.append(lista2)
lista1.sort
return ("Los multiples de 4 son:" ,lista1)
return ("Los multiples de 7 son:", lista2)
