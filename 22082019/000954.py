

multcinco=[]
multtres=[]
lista= list(range(1,100))

for i in lista:

	if i%3==0:
		multtres.append(i)

	if i%5==0:
		multcinco.append(i)


print "Los multiplos de 5 son:", multcinco
print "Los multiplos de 3 son:", multtres