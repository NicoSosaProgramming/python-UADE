with open("Archivos/Componentes.txt", "a") as archivoComponentes:
    archivoComponentes.write("Placa de Video\nMother\n")
    print("archivo guardado")
    
with open("Archivos/Componentes.txt", "r") as archivoComponentes1:
    componentes = archivoComponentes1.read()
    
print("Componentes:")
print(componentes)
