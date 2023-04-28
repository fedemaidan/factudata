import argparse
from factura_helper import dame_datos_de_factura
import os
import sys
import csv

parser = argparse.ArgumentParser(description='Ejemplo de argumentos en Python')
parser.add_argument('archivo', type=str, help='Nombre del archivo')
args = parser.parse_args()
path = args.archivo
path = "example_folder/MARZO/Facturación Nro 00003-00021793.PDF"

archivo = open("resultado_one.csv", "w", newline='')
escritor_csv = csv.writer(archivo)
escritor_csv.writerow(["emisor","condicion_iva", "numero_factura", "fecha", "valor_neto_iva", "total"])
row = dame_datos_de_factura(path)


try:
    escritor_csv.writerow([row["emisor"], row["condicion_iva"], row["numero_factura"], row["fecha"], row["valor_neto_iva"], row["total"]])
    archivo.close()
except KeyError:
    print("Error en el archivo: ", path)
    print("Row: ", row)
    
