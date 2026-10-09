import platform
import subprocess
import time
from entradas import pedir_entero_rango
from funciones import *
from salidas import *

def limpiar_consola() -> None:
    if platform.system() == "Windows":
        subprocess.run("cls",shell=True)
        subprocess.run("cls",shell=True)
    else:
        subprocess.run("clear",shell=True)
        subprocess.run("clear",shell=True)

def refrescar_menu(tiempo_menu:int = 0,mensaje_menu:str = "Toque enter para continuar...", ) -> None:
    time.sleep(tiempo_menu)
    if tiempo_menu == 0:
        input(mensaje_menu)
    limpiar_consola()

def mostrar_menu_principal():
    print("=== EJERCICIO ARRAYS ===")
    print("1. Cargar cinco notas")
    print("2. Mostrar suma y promedio total")
    print("3. Mostrar promedio de promocionados")
    print("4. Mostrar promedio de aprobados")
    print("5. Mostrar cantidad de aprobados")
    print("6. Mostrar cantidad de desaprobados")
    print("7. Mostrar notas de promocionados")
    print("8. Mostrar notas de aprobados")
    print("9. Salir")

def ejecutar_menu_principal() -> None:
    lista_notas = []
    while True:
        mostrar_menu_principal()
        opcion = pedir_entero_rango(1,9,"Ingrese una opcion: ")
        limpiar_consola()

        if opcion == 1:
            #Si quieren vaciar la lista cada vez que tocan el punto 1 pueden usar el clear()
            lista_notas.clear()#La clase que viene haremos un clear casero
            if cargar_notas(lista_notas,5,"Ingrese la nota del alumno","ERROR, la nota deberia estar entre 1 y 10, reingresela") == True:
                print("ALUMNOS CARGADOS CON EXITO!")
                mostrar_array(lista_notas,"NOTAS ALUMNOS\n","Nota alumno")
            else:
                print("HUBO UN ERROR EN LA CARGA")
        elif opcion == 9:
            print("Saliendo")
            break
        elif len(lista_notas) == 0:
            print("Primero debe cargar a los alumnos")
        elif opcion == 2:
            #2.Tenemos que mostrar la suma y el promedio total 
            suma_notas = sumar_array(lista_notas)
            cantidad_notas = len(lista_notas)
            promedio_total = calcular_promedio(suma_notas,cantidad_notas)
            mostrar_suma_promedio_notas(suma_notas,promedio_total)
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass  
        elif opcion == 8:
            pass  

        refrescar_menu()