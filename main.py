#importar la clase Trigo
from clase_Trigo import Trigo
#importar libreria para limpiar la consola
import os

#def __init__(self, cant_almacenada, cant_plantada, precio, T_cosecha, dinero)
objeto1 = Trigo(1, 0, 0, 0)
fin = 0

#funcion para limpiar la consola
def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#bucle para ejecutar el ejercicio
while (fin != 1):

    ClearConsole()
    objeto1.mostrar()
    print("1.Plantar\n2.cosechar\n3.Vender\n4.Comprar\n5. Salir")
    opcion = input("elija: ")

    if opcion == '1':
        c_p = int(input("Cuantas unidades desea plantar?: "))
        objeto1.plantar(c_p)
        
    elif opcion == '2':
        objeto1.cosechar()
        
    elif opcion == '3':
        c_v = int(input("Cuantas unidades desea vender?: "))
        objeto1.vender(c_v)
        
    elif opcion == '4':
        c_c = int(input("Cuantas unidades desea comprar?: "))
        objeto1.comprar(c_c)
    
    elif opcion == 5:
        print("Gracias por jugar.")
        fin = 1
    
    else:
        print("Esa opcion no es valida.")

