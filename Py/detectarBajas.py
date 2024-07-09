import pandas as pd
from datetime import datetime, timedelta
import calendar

def calcularNombres():
    now = datetime.now()
    mesActual = now.strftime('%m%y')

    mesAnterior = (now - timedelta(days=calendar.monthrange(now.year, now.month)[1])).strftime('%m%y')

    return f"Reporte {mesActual}.xlsx", f"Reporte {mesAnterior}.xlsx"

reporteMesActual, reporteMesAnterior = calcularNombres()

df = pd.read_excel(reporteMesActual)
try:
    columnaMesActual = df['Correo electrónico']
except KeyError:
    print(f"El archivo: '{reporteMesActual}' no posee una columna llamanda 'Correo electrónico'. Favor de revisar el archivo.")
    input()
    raise KeyError()

df = pd.read_excel(reporteMesAnterior)
try:
    columnaMesAnterior = df['Correo electrónico']
except KeyError:
    print(f"El archivo: '{reporteMesAnterior}' no posee una columna llamanda 'Correo electrónico'. Favor de revisar el archivo.")
    input()
    raise KeyError()


faltantes = []

for value in columnaMesAnterior.tolist():
    if(not columnaMesActual.tolist().__contains__(value)):
        faltantes.append(value)

if (faltantes.__len__()==0):
    print("No hay bajas por efectuar.")
else:
    print("Bajas:")
    for indice, elemento in enumerate(faltantes, start=1):
        print(f"{indice}. {elemento}")

input()
