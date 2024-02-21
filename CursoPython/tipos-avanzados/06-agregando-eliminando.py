mascotas = ["Pelusa", "Pulga", "Felipe",
            "Wolfgang", "Chanchito Feliz", "Pulga"]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")  # insertar al final

mascotas.remove("Pulga")  # Elimina solo 1 duplicado
mascotas.pop(1)
del mascotas[0]
mascotas.clear()
print(mascotas)
