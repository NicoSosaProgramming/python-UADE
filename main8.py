
contador = 0

while contador < 3:
    
    tarea = input(f"Ingrese la tarea {contador + 1}: ")
    
    with open("tareas_semana.txt", "a") as archivoSemana:
        archivoSemana.write(f"{tarea}\n")

    contador += 1

print("agregado")


with open("tareas_semana.txt", "r") as archivoSemana:
    leo = archivoSemana.read()
    
print(leo)