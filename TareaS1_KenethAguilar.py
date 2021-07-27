print("Generador de contraseñas")

#Metodo 1

#Importe el SystemRandom
from random import SystemRandom

#Declare variables
rango = 15
ascii = []
q = SystemRandom()
v = 0
l= ""

#Desarrolle funcion para que los valores no se repitan
def notrepeat(v, passw):
    valor=True
    for i in range(len(passw)): 
        if v == passw[i]:
            valor= False
            break
    return valor



#Recorrido de los valores
while rango > 0:
    v = (q.randint(33,125))
    if notrepeat(v,ascii):
        ascii.append(v)
    rango = rango - 1

#Pase de numeros a caracteres
for x in ascii:
    l += chr(x)

#Impresion de pantalla
print("Password: " + l)

#Metodo 2

#Importo el Random
import random

#Declaro variables
ascii = []
v = 0
l= ""

#desarrollo funcion par que no se repitan valores
def notrepeat(v, pw):
    valor=True
    for i in range(len(pw)): 
        if v == pw[i]:
            valor= False
            break
    return valor

#Recorro con un for
for r in range(15):
    v = (random.randint(33,125))
    if notrepeat(v,ascii):
        ascii.append(v)

#Hago el cambio de numeros a caracteres
for x in ascii:
    l += chr(x)

#Imprimo pantalla
print("Password: " + l)
