#si usamos el with
with open("nombre_del_archivo.txt", "r") as variable:
    nombreArchivo= variable.read()
    print("archivo agregado")

#si no usamos el with
f = open("datos.txt", "r")
contenido = f.read()
f.close()  # ¡ACÁ ES OBLIGATORIO! Si no lo ponés, el archivo queda bloqueado.
print("archivo agregado")

