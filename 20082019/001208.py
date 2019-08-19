
#BMI calculator
# Se definene las variables 

name1 ="YK"
height_m1=2
weight_kg1=90

name2 ="YK's sister"
height_m2=1.8
weight_kg2=70

name3 ="YK's brother"
height_m3=2.5
weight_kg3=160

#Se define la funcion bmi_calculator, con varaible input name,height_m y weight_kg
# la funcion al ser evaluada calcula una variable "bmi", con las variables de 
# entrada, luego imprime en consola el "bmi:", junto con el valor de la variable
# bmi en otra linea
# se aplican condiciones que imprimen cosas distintas segun se cumplan o no las
# condiciones.


def bmi_calculator(name,height_m, weight_kg):
	bmi=weight_kg / (height_m**2)
	print "bmi:"
	print bmi

	if bmi<25:
		return name + " "+"not overweight"
	else :
		return name + " "+ "is overweight"

# se definide las variables result1, result2, result3 mediantes la funcion
# bmi_calculator evaluada con distintas variables

result1= bmi_calculator(name1, height_m1,weight_kg1)
result2= bmi_calculator(name2, height_m2,weight_kg2)
result3= bmi_calculator(name3, height_m3,weight_kg3)

# se imprime en consola el valor de las variables

print result1
print result2
print result3
