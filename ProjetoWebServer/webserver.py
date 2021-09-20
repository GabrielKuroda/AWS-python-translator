from http.server import BaseHTTPRequestHandler, HTTPServer
from tensorflow import keras
import numpy as np
import tensorflow as tf
from PIL import Image
from urllib import request
from io import BytesIO
import logging
import boto3
import pykakasi
import json

class Requests(BaseHTTPRequestHandler):

    var = ""
    language = ""
    accessKey = ""
    secretAccessKey = ""

    def translate(self,phrase):

        global language
        global accessKey
        global secretAccessKey

        kks = pykakasi.kakasi()

        client = boto3.client('translate', region_name="us-east-1",aws_access_key_id= accessKey,
            aws_secret_access_key= secretAccessKey)

        result = client.translate_text(Text=phrase, SourceLanguageCode="auto",TargetLanguageCode=language)

        text = result['TranslatedText']

        if language in "ja":
           return kks.convert(text)[0]['passport']
        else:
           return text

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global var
        self._set_response() 
        class_names = ['borboleta', 'cachorro', 'dente-de-leao', 'gafanhoto', 'gato', 'girassol', 'joaninha', 'libelula', 'margarida', 'monitor', 'mosquito', 'mouse', 'rosa', 'teclado', 'tulipa']
        model = keras.models.load_model('projetoUsandoTransferLearning.pth')
        img_height = 130
        img_width = 130
        url = var
        res = request.urlopen(url).read()
        img = Image.open(BytesIO(res)).resize((img_height,img_width))

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        result = class_names[np.argmax(score)]

        tranlated = self.translate(result)

        self.wfile.write(bytes("<html><head><title>IA Projeto 6</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Result: %s</p>" % result, "utf-8"))
        self.wfile.write(bytes("<p>Result Translated: %s</p>" % tranlated, "utf-8"))
        self.wfile.write(bytes("<br>{:.2f}%<br>".format(100 * np.max(score)), "utf-8"))
        self.wfile.write(bytes("<img src=\"%s\" alt=\"Image\" width=\"500\" height=\"600\">" % url, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        global var
        global language
        global accessKey
        global secretAccessKey

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        resultPost = json.loads(post_data.decode('utf-8'))
        var = resultPost['image']
        language = resultPost['language']
        accessKey = resultPost['accessKey']
        secretAccessKey = resultPost['secretAccessKey']
        
        self._set_response()
        self.wfile.write("Image Link: {}".format(var).encode('utf-8'))
        self.wfile.write("Language: {}".format(language).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=Requests, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()



