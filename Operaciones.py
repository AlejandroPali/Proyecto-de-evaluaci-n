import math

def menu():
    print('**********CALCULADORA*********')
    print('Suma')
    print('resta')
    print('multiplicación')
    print('División')
    print('raiz')
    print('Apagar')

def suma(val1,val2):
     suma = float(val1) + float(val2)
     print('Resultado: '+ str(suma))
     return

def resta(val1,val2):
    resta = float(val1) - float(val2)
    print('Resultado: '+ str(resta))
    return

def multiplicacion(val1,val2):
    multiplicacion = float(val1) * float(val2)
    print('Resultado: '+ str(multiplicacion))
    return

def division(val1,val2):
    division = float(val1) / float(val2)
    print('Resultado: '+ str(division))
    return

def raiz(val1):
    raiz = math.sqrt(int(val1))
    print('Resultado: '+ str(raiz))
    return 

def datos (operacion):
    if operacion != 5:
        val1 = input('Ingresa el primer Valor: ')
        val2 = input('Ingresa el segundo Valor: ')
    else :
        val1 = input('Ingresa el primer Valor: ')

    if operacion == 1:
        suma(val1,val2)
    elif operacion == 2:
        resta(val1,val2)
    elif operacion == 3:
        multiplicacion(val1,val2)
    elif operacion == 4:
        division(val1,val2)
    elif operacion == 5:
        raiz(val1)