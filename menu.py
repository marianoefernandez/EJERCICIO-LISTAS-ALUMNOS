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
            limpiar_array(lista_notas)
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
            suma_notas = sumar_array(lista_notas)
            cantidad_notas = len(lista_notas)
            promedio_total = calcular_promedio(suma_notas,cantidad_notas)
            mostrar_suma_promedio_notas(suma_notas,promedio_total)
        elif opcion == 3:
            suma_promocionados = sumar_por_rango(lista_notas,6,10)
            cantidad_promocionados = contar_por_rango(lista_notas,6,10)
            promedio_promocionados = calcular_promedio(suma_promocionados,cantidad_promocionados,"No hay promocionados")
            informar_promedio(promedio_promocionados,"Promedio de promocionados:")
        elif opcion == 4:
            suma_aprobados = sumar_por_rango(lista_notas,4,5)
            cantidad_aprobados = contar_por_rango(lista_notas,4,5)
            promedio_aprobados = calcular_promedio(suma_aprobados,cantidad_aprobados,"No hay aprobados")
            informar_promedio(promedio_aprobados,"Promedio de aprobados:")
        elif opcion == 5:
            cantidad_aprobados = contar_por_rango(lista_notas,4,5)
            informar_cantidad(cantidad_aprobados,"Cantidad de aprobados:")
        elif opcion == 6:
            cantidad_desaprobados = contar_por_rango(lista_notas,1,3)
            informar_cantidad(cantidad_desaprobados,"Cantidad de desaprobados:")
        elif opcion == 7:
            mostrar_array_rango(lista_notas,6,10,"Error. No hay ningun alumno promocionado","ALUMNOS PROMOCIONADOS\n","Nota alumno")
        elif opcion == 8:
            mostrar_array_rango(lista_notas,4,5,"Error. No hay ningun alumno aprobado","ALUMNOS APROBADOS\n","Nota alumno")

        refrescar_menu()