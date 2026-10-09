import platform
import subprocess
import time
from entradas import pedir_entero_rango

def limpiar_consola() -> None:
    if platform.system() == "Windows":
        subprocess.run("cls",shell=True)
        subprocess.run("cls",shell=True)
    else:
        subprocess.run("clear",shell=True)
        subprocess.run("clear",shell=True)

def refrescar_carga(tiempo_menu:int = 0,mensaje_menu:str = "Toque enter para continuar...", ) -> None:
    time.sleep(tiempo_menu)
    if tiempo_menu == 0:
        input(mensaje_menu)
    limpiar_consola()

def cargar_notas(array_notas:list,cantidad_elementos:int,mensaje:str = "Ingrese la nota",mensaje_error:str = "ERROR") -> bool:
    if type(array_notas) == list and validar_cantidad_elementos(cantidad_elementos):
        for i in range(cantidad_elementos):
            # nota = int(input(f"{mensaje} {i + 1}°: "))
            nota = pedir_entero_rango(1,10,f"{mensaje} {i + 1}°: ",mensaje_error)
            array_notas.append(nota)
            refrescar_carga()
        return True
    else:
        return False

def validar_cantidad_elementos(cantidad:int) -> bool:
    return type(cantidad) == int and cantidad > 0

def validar_numerico(elemento:any) -> bool:
    return type(elemento) == int or type(elemento) == float

def sumar_array(array:list) -> int | float:
    acumulador = 0
    if type(array) == list:
        for i in range(len(array)):
            if validar_numerico(array[i]):
                acumulador += array[i]

    return acumulador

def calcular_promedio(acumulador: int | float, contador: int, mensaje_error: str = "ERROR") -> float | str:
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = mensaje_error

    return promedio