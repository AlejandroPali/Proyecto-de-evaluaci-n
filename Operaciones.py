import math
menus = ['suma','Resta','Multiplicacion', 'División','Raiz','Exponentes', 'Seno','Coseno', 'Tangente','Apagar','']
def menu():
    print('**********CALCULADORA*********')
    for oper in menus:
        print(oper)

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

def exponentes(val1,val2):
    exponentes = int(val1)**int(val2)
    print('Resultado: '+ str(exponentes))
    return 

def seno(val1):
    seno = math.sin(float(val1))
    print('Resultado: '+ str(seno))
    return 

def coseno(val1):
    coseno = math.cos(float(val1))
    print('Resultado: '+ str(coseno))
    return

def tangente(val1):
    tangente = math.tan(float(val1))
    print('Resultado: '+ str(tangente))
    return

def datos (operacion):
    if operacion != 5 and operacion !=6 and operacion != 7 and operacion != 8 and operacion != 9:
        val1 = input('Ingresa el primer Valor: ')
        val2 = input('Ingresa el segundo Valor: ')
    elif operacion == 5 or operacion == 7 or operacion ==8 or operacion ==9:
        val1 = input('Ingresa el Valor a calcular: ')
    elif operacion == 6:
        val1 = input('Ingresa el primer Valor: ')
        val2 = input('A qué potencia: ')
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
    elif operacion == 6:
        exponentes(val1,val2)
    elif operacion == 7:
        seno(val1)
    elif operacion == 8:
        coseno(val1)
    elif operacion == 9:
        tangente(val1)
    