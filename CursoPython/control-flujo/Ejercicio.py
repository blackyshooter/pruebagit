
n1 = 0

if n1 == 0:
        
        leer_n1 = input("Ingrese un número ")
        n1 = int(leer_n1)
while n1 != 0 or leer_op == "salir":
        leer_op = input("\nIngrese la operacion ")
        leer_n2 = input("\nIngrese el siguiente numero ")
        n2 = int(leer_n2)
        if leer_op.lower() == "suma":
            resultado = n1 + n2
            print("El resultado es ",resultado)
            n1 = resultado
        elif leer_op.lower() == "resta":
            resultado = n1 - n2
            print("El resultado es ",resultado)
            n1 = resultado
        elif leer_op.lower() == "multi":
              resultado = n1 * n2
              print("El resultado es ",resultado)
              n1 = resultado
        elif leer_op.lower() == "div":
              resultado = n1 / n2
              print("El resultado es ",resultado)
              n1 = resultado

    
    

