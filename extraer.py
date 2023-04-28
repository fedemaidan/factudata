import argparse
from factura_helper import dame_datos_de_factura
import os
import sys
import csv
from limpiar_numero import limpiar_numero

parser = argparse.ArgumentParser(description='Ejemplo de argumentos en Python')
parser.add_argument('limite', type=str, help='Cantidad maxima de archivos')
parser.add_argument('carpeta', type=str, help='Nombre de la carpeta')
args = parser.parse_args()
carpeta = args.carpeta
limite = int(args.limite)

# carpeta = 'example_folder/MARZO'
contador = 0
archivo = open("resultado.csv", "w", newline='')
escritor_csv = csv.writer(archivo)
escritor_csv.writerow(["filename","emisor","condicion_iva", "numero_factura", "fecha", "valor_neto_sin_iva", "total"])

# Recorremos la carpeta y mostramos el nombre de los archivos
for filename in os.listdir(carpeta):
    try:
        contador = contador + 1
        print("Row " + str(contador) + "/" + str(limite))
        path = os.path.join(carpeta, filename)
        row = dame_datos_de_factura(path)
        escritor_csv.writerow([filename, row["nombre_emisor"], row["condicion_iva"], row["numero_factura"], row["fecha"], limpiar_numero(row["valor_neto_sin_iva"]), limpiar_numero(row["total"])])
        if contador == limite:
            archivo.close()
            sys.exit()
    except KeyError:
        print("error con")
        print(row)
        escritor_csv.writerow([filename])
    
archivo.close()






