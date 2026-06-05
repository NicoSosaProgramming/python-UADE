with open("Medios/mis_medios.txt", "a") as archivoMedios:
    for i in range(3):
        medio = input(f"Ingrese el nombre del medio {i+1}: ")
        archivoMedios.write(medio + "\n")
    print("agregado")
    
with open("Medios/mis_medios.txt", "r") as archivo:
    medios = archivo.read()
    
print("Medios:")
print(medios)

#----------------------------------------------------------------------

with open("Medios/programas_radio.txt", "w") as archivoRadio:
    numeroIngresado = int(input("¿Cuantos medios queres ingresar:?"))
    for i in range(numeroIngresado):
        programa = input(f"Ingresa el programa {i+1}: ")
        archivoRadio.write(programa +"\n")
print("Agregado")

with open("Medios/programas_radio.txt", "r") as archivoRadio:
    radio = archivoRadio.read()
print("Radios: ")
print(radio)


#----------------------------------------------------------------------
with open("Medios/clasificados.txt", "w") as archivoClasificado:
    for i in range(3):
        tipo = input("Ingrese el tipo del medio (Tv, Radio, Web): ")
        nombre = input("Ingrese el nombre del medio: ")
        archivoClasificado.write(f"{tipo} - {nombre}\n")
print("agregados")

with open("Medios/clasificados.txt", "r") as archivoClasificado:
    medios = archivoClasificado.read()
    
print("Medios:")
print(medios)

#----------------------------------------------------------------------