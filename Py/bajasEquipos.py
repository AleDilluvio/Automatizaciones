import pandas as pd

def obtenerPrimeraColumna(path):
    df = pd.read_excel(path)
    try:
        columna = df['Hostnames']
        return columna
    except KeyError:
        print(f"El archivo: '{path}' no posee una columna llamanda 'Hostnames'. Favor de revisar el archivo.")
        input()
    raise KeyError()

# Se debe ejecutar desde la misma carpeta en la que se encuentran los archivos y el script.
equiposA = obtenerPrimeraColumna(r"Equipos A.xlsx")
equiposB = obtenerPrimeraColumna(r"Equipos B.xlsx")

faltantes = []

for value in equiposA.tolist():
    if(not equiposB.tolist().__contains__(value)):
        faltantes.append(value)

if (len(faltantes)==0):
    print("No hay bajas por efectuar.")
else:
    print("Bajas:")
    for indice, elemento in enumerate(faltantes, start=1):
        print(f"{indice}. {elemento}")

input()
