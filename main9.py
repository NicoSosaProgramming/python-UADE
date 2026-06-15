nombres = []
carreras = []
materias = []
valoraciones = []


for i in range(3):
    nombre = input("ingrese su nombre: ")
    carrera = input ("ingrese su carrera: ")
    materia = input("ingrese su materia favorita: ")
    
    print("\nValoración del docente:")
    print("1 = Excelente desempeño académico")
    print("2 = Buen desempeño, puede mejorar")
    print("3 = Desempeño bajo, necesita apoyo adicional")
    valor = int(input("Evaluación del docente sobre el desempeño académico (1,2 o 3): "))
    
    nombres.append(nombre)
    carreras.append(carrera)
    materias.append(materia)
    valoraciones.append(valor)
    

for i in range(3):
    
    if valoraciones[i] == 1:
        texto_valor = "Excelente desempeño académico"
    elif valoraciones[i] == 2:
        texto_valor = "Buen desempeño, puede mejorar"
    elif valoraciones[i] == 3:
        texto_valor = "Desempeño bajo, necesita apoyo adicional"
    
    print(f"{nombres[i]} - {carreras[i]} - {materias[i]} - {texto_valor}")
    
    
with open("observaciones_docente.txt", "w") as archivos:
    for i in range(3):
        nombre = nombres[i]
        valor = valoraciones[i]
        
        if valor == 1:
            mensaje = "Demuestra compromiso y gran capacidad académica."
        elif valor == 2:
            mensaje = "Puede mejorar si mantiene la constancia."
        elif valor == 3:
            mensaje = "Requiere seguimiento y acompañamiento adicional."
            
        archivos.write(f"{nombre}: {mensaje}\n")
        
print("archivo observaciones_docente.txt creado")