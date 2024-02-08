
resultado = ""

while True:
    if not resultado:
        leer_n1 = input("Ingrese un número ")
    if leer_n1.lower == "salir":
        break
    resultado = int(leer_n1)
    leer_op = input("\nIngrese la operacion ")
    if leer_op.lower() == "salir":
        break
    leer_n2 = input("\nIngrese el siguiente numero ")
    n2 = int(leer_n2)
    if leer_op.lower() == "suma":
        resultado += n2
        n1 = resultado
    elif leer_op.lower() == "resta":
        resultado -= n2
        n1 = resultado
    elif leer_op.lower() == "multi":
        resultado *= n2
        n1 = resultado
    elif leer_op.lower() == "div":
        resultado /= n2
        n1 = resultado
    else:
        print("Operacion Invalida")
        break

    print(f"El resultado es {resultado}")
