import nltk.data
from factura_helper import dame_texto_desde_path
# nltk.download("punkt")

path = "/home/fede/workspace/factudata/examples/ticket-palo-alto-1.jpg"
texto = dame_texto_desde_path(path)
texto = texto.replace("\n\n","\n")
texto = texto.replace("\n"," . ")
tokenizer = nltk.data.load('nltk:tokenizers/punkt/spanish.pickle')
result = tokenizer.tokenize(texto)
i=0
for item in result:
    print(i)
    i=i+1
    print(item)
