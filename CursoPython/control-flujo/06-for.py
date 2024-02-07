
buscar = 10

for numero in range(5):  # Iterable
    print(numero)
    if numero == buscar:
        print("Aca estoy rey", buscar)
        break
else:
    print("No esta :(")

for char in "Ultimate Python":
    print(char)
