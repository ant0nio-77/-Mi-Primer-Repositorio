#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Silvio Antonio Lobo Alvarado"
edad = 13
estatura = 1.63
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("lobx_77s", "42__lobx")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "ZOMBI", "artista": "Trueno", "duracion": "2:34"},
{"titulo": "Luciérnagas", "artista": "Milo j,Silvio Rodríguez", "duracion": "3:06"},
{"titulo": "Pensando En El Dream - Remix", "artista": "Saigo", "duracion": "4:20"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
for cancion in Playlist:
    print(f"{cancion['titulo']} - {cancion['artista']} ({cancion['duracion']}) min")
print ("----------------------------------")
