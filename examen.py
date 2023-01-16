#calculadora

import Operaciones
encendido=True
accion=''

while encendido:
    Operaciones.menu()
    accion = input('¿Qué desea realizar? ')

    if accion.lower().lower() == 'suma':
        Operaciones.datos(1)
    elif accion.lower() == 'resta':
        Operaciones.datos(2)
    elif accion.lower() == 'multiplicacion':
        Operaciones.datos(3)
    elif accion.lower() == 'division':
        Operaciones.datos(4)
    elif accion.lower() == 'raiz':
        Operaciones.datos(5)
    elif accion.lower() == 'apagar':
        encendido = False
    else:
        print('Ingresa una accion correcta (Sin acentos, ni numeros)')