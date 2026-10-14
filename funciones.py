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

def validar_rango(elemento:any, minimo:int, maximo:int) -> bool:
    return validar_numerico(elemento) and elemento >= minimo and elemento <= maximo

def verificar_indice(lista:list,indice:int) -> bool:
    return type(indice) == int and indice < len(lista) and indice >= -1

def sumar_array(array:list) -> int | float:
    acumulador = 0
    if type(array) == list:
        for i in range(len(array)):
            if validar_numerico(array[i]):
                acumulador += array[i]

    return acumulador

def sumar_por_rango(array:list, minimo:int, maximo:int) -> int | float:
    acumulador = 0
    if type(array) == list:
        for i in range(len(array)):
            if validar_rango(array[i],minimo,maximo):
                acumulador += array[i]

    return acumulador

def contar_por_rango(array:list, minimo:int, maximo:int) -> int:
    contador = 0
    if type(array) == list:
        for i in range(len(array)):
            if validar_rango(array[i],minimo,maximo):
                contador += 1

    return contador

def calcular_promedio(acumulador: int | float, contador: int, mensaje_error: str = "ERROR") -> float | str:
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = mensaje_error

    return promedio

#VER CLEAR CASERO


def eliminar_dato_indice(lista:list,indice:int = -1) -> any | None: #Pop casero
    if type(lista) == list and verificar_indice(lista,indice):
        elemento_eliminado = lista[indice]
        del lista[indice]
        return elemento_eliminado

    return None

def limpiar_array(array:list) -> bool:
    if type(array) == list:
        while len(array) > 0:
            eliminar_dato_indice(array,0)#FORMA A
            # eliminar_dato_indice(array)#FORMA B
        return True
    else:
        return False

def limpiar_array_pares(array:list) -> bool:
    #Eliminar solo los numeros pares de un arrey
    pass

# lista_numeros = [5,8,10,20,30,15,4]
# print(f"ANTES DEL LIMPIAR ARRAY --> {lista_numeros}")
# limpiar_array(lista_numeros)
# print(f"DESPUES DEL LIMPIAR ARRAY --> {lista_numeros}")
# # print(sumar_por_rango(lista_numeros,5,10))
# # print(contar_por_rango(lista_numeros,5,10))
