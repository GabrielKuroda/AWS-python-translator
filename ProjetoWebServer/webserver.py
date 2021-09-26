from http.server import BaseHTTPRequestHandler, HTTPServer
from tensorflow import keras
import numpy as np
import tensorflow as tf
from PIL import Image
from urllib import request
from io import BytesIO
import logging
import boto3
import json

class Requests(BaseHTTPRequestHandler):

    urlImage = ""
    languageOrigin = ""
    languageTarget = ""
    accessKey = ""
    secretAccessKey = ""
    
    def translate(self,phrase,target,origin):

        client = boto3.client('translate', region_name="us-east-1",aws_access_key_id= accessKey,
            aws_secret_access_key= secretAccessKey)

        return client.translate_text(Text=phrase, SourceLanguageCode=origin,TargetLanguageCode=target)['TranslatedText']

    def getLanguageName(self,languageCode,typeLanguage):
        
        if typeLanguage in "Origin":
            languages = ['Origin Language: Portuguese','Origin Language: Japanese','Origin Language: English','Origin Language: Spanish']
        else:
            languages = ['Target Language: Portuguese','Target Language: Japanese','Target Language: English','Target Language: Spanish']

        if languageCode in "pt":
            return self.translate(languages[0],languageOrigin,"en")
        elif languageCode in "ja":
            return self.translate(languages[1],languageOrigin,"en")
        elif languageCode in "en":
            return self.translate(languages[2],languageOrigin,"en")
        elif languageCode in "es":
            return self.translate(languages[3],languageOrigin,"en")
        else:
            return "Unknown"

    def getTitle(self,languageCode):
        
        title = "Translator with IA"

        if languageCode in "pt":
            return self.translate(title,languageOrigin,"en")
        elif languageCode in "ja":
            return self.translate(title,languageOrigin,"en")
        elif languageCode in "en":
            return self.translate(title,languageOrigin,"en")
        elif languageCode in "es":
            return self.translate(title,languageOrigin,"en")
        else:
            return "Unknown"

    def getIAResult(self,languageCode, result):
        
        text = "IA Result: " + result

        if languageCode in "pt":
            return self.translate(text,languageOrigin,"en") 
        elif languageCode in "ja":
            return self.translate(text,languageOrigin,"en")
        elif languageCode in "en":
            return self.translate(text,languageOrigin,"en")
        elif languageCode in "es":
            return self.translate(text,languageOrigin,"en")
        else:
            return "Unknown"

    def getTranslatorResult(self,languageCode, translated):
        
        text = "Translated: "

        if languageCode in "pt":
            return self.translate(text,languageOrigin,"en") + translated
        elif languageCode in "ja":
            return self.translate(text,languageOrigin,"en") + translated
        elif languageCode in "en":
            return self.translate(text,languageOrigin,"en") + translated
        elif languageCode in "es":
            return self.translate(text,languageOrigin,"en") + translated
        else:
            return "Unknown"

    def getReturn(self,result,score):

        translated = self.translate(result,languageTarget,languageOrigin)

        self.wfile.write(bytes("<html><head><title>%s</title></head><meta charset=\"utf-8\"/>" % self.getTitle(languageOrigin), "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>%s</p>" % self.getLanguageName(languageOrigin,"Origin"), "utf-8"))
        self.wfile.write(bytes("<p>%s</p>" % self.getIAResult(languageOrigin,result), "utf-8"))
        self.wfile.write(bytes("<p>%s</p>" % self.getLanguageName(languageTarget,"Target"), "utf-8"))
        self.wfile.write(bytes("<p>%s</p>" % self.getTranslatorResult(languageOrigin,translated), "utf-8"))
        self.wfile.write(bytes("<br>{:.2f}%<br>".format(100 * np.max(score)), "utf-8"))
        self.wfile.write(bytes("<img src=\"%s\" alt=\"Image\" width=\"500\" height=\"600\">" % urlImage, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
            
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        
        global urlImage
        global languageTarget
        global languageOrigin

        self._set_response()

        class_names = ['butterfly', 'dog', 'dandelion', 'locust', 'cat', 'sunflower', 'ladybird', 'dragonflies', 'daisy', 'monitor', 'mosquito', 'mouse', 'rose', 'keyboard', 'tulip']

        model = keras.models.load_model('projetoUsandoTransferLearning.pth')
        img_height = 130
        img_width = 130
        res = request.urlopen(urlImage).read()
        img = Image.open(BytesIO(res)).resize((img_height,img_width))

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        result = class_names[np.argmax(score)]

        self.getReturn(result,score)

    def do_POST(self):
        global urlImage
        global languageTarget
        global languageOrigin
        global accessKey
        global secretAccessKey

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        resultPost = json.loads(post_data.decode('utf-8'))
        urlImage = resultPost['image']
        languageTarget = resultPost['languageTarget']
        languageOrigin = resultPost['languageOrigin']
        accessKey = resultPost['accessKey']
        secretAccessKey = resultPost['secretAccessKey']
        
        self._set_response()
        self.wfile.write("Image Link: {}".format(urlImage).encode('utf-8'))
        self.wfile.write("language Target: {}".format(languageTarget).encode('utf-8'))
        self.wfile.write("language Origin: {}".format(languageOrigin).encode('utf-8'))

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



