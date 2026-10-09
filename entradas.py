def pedir_entero_rango(minimo: int, maximo: int, mensaje: str = "Ingrese un numero", mensaje_error: str = "ERROR") -> int:
    numero = int(input(mensaje))

    while numero < minimo or numero > maximo:
        print(mensaje_error)
        numero = int(input(mensaje))

    return numero