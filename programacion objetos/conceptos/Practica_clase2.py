## verificar el mayor de tres numeros ##

a=int(input("ingrese el primer numero:"))
b=int(input("ingrese el segundo numero:"))
c=int(input("ingrese el tercer numero:)"))
while a<=0 or b<=0 or c<=0:
    print("ingrese numeros validos")
    a=int(input("ingrese el primer numero:"))
    b=int(input("ingrese el segundo numero:"))
    c=int(input("ingrese el tercer numero:)"))

if a>b and a>c:
    print("el mayor es ", a)
elif b>a and b>c:
    print("el mayor e", b)
else:
    print("el mayor es ", c)
    
    
## calcular el factorial de un numero ##

numero=int(input("ingrese el numero:"))
while numero<=1:
    print("ingrese un numero valido")
    numero=int(input("ingrese el numero:"))

factorial=1
for i in range(1, numero+1):
    factorial*=i
print("el factorial de", numero, "es", factorial)

## opcion 2 ##
while True:                                                                     #numero=4    factorial=1-1-2-6-24    contador=1-2-3-4-5
  try:
    numero=int(input("Ingrese un numero para calcular el factorial: "))
    if numero>=0:
      break
    else:
      print("Debe ingresar un numero positivo")
  except ValueError:
    print("Debe ingresar un numero")

factorial=1
contador=1
if numero==0:
  print(f"El factorial de {numero} es {factorial}")                             #"El factorial de 0 es 1"
else:
  while contador<=numero:                                                       #contador<=numero     5<=4
    factorial=factorial*contador                                                #factorial=factorial*contador         factorial=6*4
    contador=contador+1                                                         #contador=contador+1                  contador= 4+1
  print(f"El factorial de {numero} es {factorial}")




