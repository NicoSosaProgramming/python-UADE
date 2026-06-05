
#----------------------------------------------------------------------------
with open("Medios/tv.txt", "r") as archivoMedios:
    medios = archivoMedios.read()
print("Medios Tv:")
print(medios)



#----------------------------------------------------------------------------
with open("Medios/radio.txt", "w") as archivoRadio:
    radio = archivoRadio.write("Aspen\nRadio Disney\nRockAndPop\n")

with open("Medios/radio.txt", "r") as archivoRadio:
    radio = archivoRadio.read()

print("LAS RADIOSS:")
print(radio)
#----------------------------------------------------------------------------



#bloque + ejercicio5
#----------------------------------------------------------------------------
with open("Medios/tv.txt", "r+") as archivoTv:
    tv = archivoTv.read()
    archivoTv.write("Canal Encuentro\n")
    archivoTv.seek(0)
    tv_final = archivoTv.read()

print("Tv:")
print(tv_final)
#----------------------------------------------------------------------------