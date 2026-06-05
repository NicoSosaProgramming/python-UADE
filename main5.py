with open("Archivos/MarcaCelus.txt", "r+") as archivoCelus:
    celus = archivoCelus.read()
    archivoCelus.write("Xiomi\nsamsung\n")
    archivoCelus.seek(0)
    celus = archivoCelus.read()

print("Celus:")
print(celus)