def mostrar_array(array:list,titulo:str = "",dato:str = ""):
    print(f"{titulo}",end="")
    for i in range(len(array)):
        print(f"{dato} {i + 1}°: {array[i]}")

def mostrar_suma_promedio_notas(suma_total:int , promedio_total:float) -> None:
    print(f"Suma total de las notas: {suma_total}")
    informar_promedio(promedio_total,"Promedio total de las notas: ")

def informar_promedio(promedio : float | str,mensaje:str = "El promedio es: ") -> None:
    if type(promedio) == float:
        print(f"{mensaje} {promedio:.2f}")
    else:
        print(f"{mensaje} {promedio}")