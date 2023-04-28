from PIL import Image
import pytesseract
from extraer_pdf import pdf_text
from chatgpt_helper import pedirle_datos_a_chatgpt
import json
import re
import os

extra = ".txt_json"
folder_db = "request_db/"

def create_custom_path(path):
    path = path.replace("/","__")
    return folder_db + path + extra

def guardar_json_txt(path, json_txt):
    custom_path = create_custom_path(path)
    with open(custom_path, 'w') as file:
        file.write(json_txt)

def chatgpt_saved(nombre_archivo):
    custom_path = create_custom_path(nombre_archivo)
    if os.path.exists(custom_path):
        with open(custom_path, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    else:
        return None

def limpiar(texto):
    texto = borrar_previo_json(texto)
    return texto

def borrar_previo_json(texto):

    match = re.search(r'\{', texto)
    
    if match:
        # Si encontramos una ocurrencia, retornamos el texto a partir de esa posición
        return texto[match.start():]
    else:
        # Si no encontramos una ocurrencia, retornamos el texto original
        return texto 

def dame_tipo(string):
    return string[-3:]

def dame_datos_de_factura(path):
    try:
        if (dame_tipo(path) == "pdf" or dame_tipo(path) == "PDF"):
            texto = pdf_text(path)
        else:
            # Abrimos la imagen
            im = Image.open(path)
            texto = pytesseract.image_to_string(im)
        chatgpt_response = chatgpt_saved(path)
        if not chatgpt_response:
            print("Debo pedir datos a chatgpt")
            chatgpt_response = pedirle_datos_a_chatgpt(texto)
            print("Voy a guardar: ", chatgpt_response)
            guardar_json_txt(path, chatgpt_response)
            print("Guardé")
        
        json_txt =  limpiar(chatgpt_response)
        return json.loads(json_txt)
    except Exception as e:
        print(e)
        return { "success": False }