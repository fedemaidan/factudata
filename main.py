import argparse
# from factura_helper import dame_datos_de_factura
import os
import sys
import csv
import functions_framework

@functions_framework.http
def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'filename' in request.args:
        filename = request.args.get('filename')
        # row = dame_datos_de_factura(filename)
        return request.args.get('filename')
    elif request_json and 'message' in request_json:
        # row = dame_datos_de_factura(filename)
        return request.args.get('filename')
    else:
        return f'Hello World!'


# parser = argparse.ArgumentParser(description='Ejemplo de argumentos en Python')
# parser.add_argument('archivo', type=str, help='Nombre del archivo')
# args = parser.parse_args()
# path = args.archivo


# archivo = open("resultado_one.csv", "w", newline='')
# escritor_csv = csv.writer(archivo)
# escritor_csv.writerow(["emisor","condicion_iva", "numero_factura", "fecha", "valor_neto_iva", "total"])
# row = dame_datos_de_factura(path)


# try:
#     escritor_csv.writerow([row["emisor"], row["condicion_iva"], row["numero_factura"], row["fecha"], row["valor_neto_iva"], row["total"]])
#     archivo.close()
# except KeyError:
#     print("Error en el archivo: ", path)
#     print("Row: ", row)
    
