def get_product(**datos):  # kword argument
    print(datos["id"], datos["name"])


# Colocar el nombre del parametro asignado#
get_product(id="23", name="iPhone", desc="Es un iphone")
