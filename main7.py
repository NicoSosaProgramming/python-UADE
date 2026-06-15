# **3- Resumen de Reporte de Campaña**

# **Consigna:** Estás generando un archivo de resumen diario para una campaña publicitaria. Crea un script de Python que capture el nombre de la campaña y sus resultados clave.

# El programa debe seguir el siguiente flujo de tres pasos:

# 1. **PEDIR INFO:** Solicita al usuario que ingrese el **nombre de la campaña** y un **resumen breve** de 
# sus resultados (ej. "ROI positivo del 15%") usando `input()`.
# 2. **ESCRIBIR EN TXT:** Utailiza la operación de **escritura** (`'w'`) para guardar el nombre y el resumen 
# en línes separadas dentro del archivo `reporte_campana.txt`. Esta operación **sobrescribirá** cualquier contenido anterior, 
# asegurando que solo esté el reporte más reciente.
# 3. **LEER TXT:** Finalmente, **lee** el archivo `reporte_campana.txt` y muestra el resumen completo guardado en la consola.

nombre_campania = input("Ingrese el nombre de la campaña: ")
resultados = input("Ingrese un resumen breve de los resultados: ")


with open("reporte.txt", "w", encoding="utf-8") as archivoReporte:
    archivoReporte.write(f"{nombre_campania}\n")
    archivoReporte.write(f"{resultados}\n")

print("se agregaron correctamente")


with open("reporte.txt", "r", encoding="utf-8") as archivoReporte:
    reporte = archivoReporte.read()
    
print(reporte)
