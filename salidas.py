from funciones import validar_rango,validar_numerico

def mostrar_array(array:list,titulo:str = "",dato:str = "") -> None:
    print(f"{titulo}",end="")
    for i in range(len(array)):
        print(f"{dato} {i + 1}°: {array[i]}")

def mostrar_array_rango(array:list, minimo:int, maximo:int,mensaje_error:str = "",titulo:str = "",dato:str = "") -> None:
    bandera = False
    print(f"{titulo}",end="")
    if type(array) == list and validar_numerico(maximo) and validar_numerico(minimo):
        for i in range(len(array)):
            if validar_rango(array[i],minimo,maximo):
                print(f"{dato} {i + 1}°: {array[i]}")
                bandera = True

    if bandera == False:
        print(mensaje_error)

def mostrar_suma_promedio_notas(suma_total:int , promedio_total:float) -> None:
    print(f"Suma total de las notas: {suma_total}")
    informar_promedio(promedio_total,"Promedio total de las notas: ")

def informar_promedio(promedio : float | str,mensaje:str = "El promedio es: ") -> None:
    if type(promedio) == float:
        print(f"{mensaje} {promedio:.2f}")
    else:
        print(f"{mensaje} {promedio}")

def informar_cantidad(cantidad:int, mensaje:str = "La cantidad es: ") -> None:
    print(f"{mensaje} {cantidad}")