try:
	with open("Archivos/medios_digitales.txt", "x") as archivo_digital:
		archivo_digital.write("Infobae\nPágina 12\n")
	print("Archivo medios_digitales.txt creado.")
except:
	print("El archivo medios_digitales.txt ya existe.")
