def menu():
    print('**********CALCULADORA*********')
    print('Suma')
    print('resta')
    print('multiplicación')
    print('División')
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

def datos (operacion):
    val1 = input('Ingresa el primer Valor: ')
    val2 = input('Ingresa el segundo Valor: ')
    if operacion == 1:
        suma(val1,val2)
    elif operacion == 2:
        resta(val1,val2)
    elif operacion == 3:
        multiplicacion(val1,val2)
    else:
        division(val1,val2)