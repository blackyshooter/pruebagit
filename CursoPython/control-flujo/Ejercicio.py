resultado = None  # Inicializar resultado fuera del bucle

while True:
    if resultado is None:  # Solo solicitar el primer número si resultado aún no ha sido asignado
        leer_n1 = input("Ingrese un número (o 'salir' para terminar): ")
        if leer_n1.lower() == "salir":
            break
        resultado = int(leer_n1)
    else:
        leer_op = input(
            "\nIngrese la operación (suma, resta, multi, div o 'salir'): ")
        if leer_op.lower() == "salir":
            break
        leer_n2 = input("Ingrese el siguiente número: ")
        n2 = int(leer_n2)

        if leer_op.lower() == "suma":
            resultado += n2
        elif leer_op.lower() == "resta":
            resultado -= n2
        elif leer_op.lower() == "multi":
            resultado *= n2
        elif leer_op.lower() == "div":
            resultado /= n2
        else:
            print("Operación Inválida")
            break

        print(f"El resultado es {resultado}")
