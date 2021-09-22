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

    urlImage = ""
    languageOrigin = ""
    languageTarget = ""
    accessKey = ""
    secretAccessKey = ""
    
    def callAWSTranslate(self,phrase):

        global languageTarget
        global accessKey
        global secretAccessKey

        client = boto3.client('translate', region_name="us-east-1",aws_access_key_id= accessKey,
            aws_secret_access_key= secretAccessKey)

        return client.translate_text(Text=phrase, SourceLanguageCode=languageOrigin,TargetLanguageCode=languageTarget)

    def translate(self,phrase):
        return self.callAWSTranslate(phrase)['TranslatedText']

    def getLanguageName(self,languageCode):
        global languageOrigin

        languages = ['Portuguese','Japanese','English','Spanish']
        if languageOrigin in "pt":
            languages = ['Português','Japonês','Inglês','Espanhol']
        elif languageOrigin in "ja":
            languages = ['ポルトガル語','日本語','英語','スペイン語']
        elif languageOrigin in "en":
            languages = ['Portuguese','Japanese','English','Spanish']
        
        if languageCode in "pt":
            return languages[0]
        elif languageCode in "ja":
            return languages[1]
        elif languageCode in "en":
            return languages[2]
        elif languageCode in "sp":
            return languages[3]
        else:
            return "Unknown"
            

    def getLanguageFrom(self,phrase):

        result = self.callAWSTranslate(phrase)

        return self.getLanguageName(result['SourceLanguageCode'])
        
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global urlImage
        global languageTarget
        global languageOrigin

        self._set_response()

        class_namesPT = ['borboleta', 'cachorro', 'dente-de-leao', 'gafanhoto', 'gato', 'girassol', 'joaninha', 'libelulas', 'margarida', 'monitor', 'mosquito', 'mouse', 'rosa', 'teclado', 'tulipa']
        class_namesJA = ['蝶', '犬', 'タンポポ', 'イナゴ', '猫', 'ひまわり', 'テントウムシ', 'トンボ', 'デイジー', 'モニター', '蚊', 'マウス', 'バラ', 'キーボード', 'チューリップ']
        class_namesEN = ['butterfly', 'dog', 'dandelion', 'locust', 'cat', 'sunflower', 'ladybird', 'dragonflies', 'daisy', 'monitor', 'mosquito', 'mouse', 'rose', 'keyboard', 'tulip']

        if languageOrigin in "pt":
            class_names = class_namesPT
        elif languageOrigin in "ja":
            class_names = class_namesJA
        elif languageOrigin in "en":
            class_names = class_namesEN

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

        tranlated = self.translate(result)

        if languageOrigin in "pt":
            self.wfile.write(bytes("<html><head><title>Tradutor</title></head><meta charset=\"utf-8\" />", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Idioma Origem: %s</p>" % self.getLanguageFrom(result), "utf-8"))
            self.wfile.write(bytes("<p>Resultado: %s</p>" % result, "utf-8"))
            self.wfile.write(bytes("<p>Idioma alvo: %s</p>" % self.getLanguageName(languageTarget), "utf-8"))
            self.wfile.write(bytes("<p>Resultado Tradução: %s</p>" % tranlated, "utf-8"))
            self.wfile.write(bytes("<br>{:.2f}%<br>".format(100 * np.max(score)), "utf-8"))
            self.wfile.write(bytes("<img src=\"%s\" alt=\"Image\" width=\"500\" height=\"600\">" % urlImage, "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif languageOrigin in "ja":
            self.wfile.write(bytes("<html><head><title>翻訳</title></head><meta charset=\"utf-8\" />", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>ソース言語: %s</p>" % self.getLanguageFrom(result), "utf-8"))
            self.wfile.write(bytes("<p>結果: %s</p>" % result, "utf-8"))
            self.wfile.write(bytes("<p>目標言語: %s</p>" % self.getLanguageName(languageTarget), "utf-8"))
            self.wfile.write(bytes("<p>翻訳結果: %s</p>" % tranlated, "utf-8"))
            self.wfile.write(bytes("<br>{:.2f}%<br>".format(100 * np.max(score)), "utf-8"))
            self.wfile.write(bytes("<img src=\"%s\" alt=\"Image\" width=\"500\" height=\"600\">" % urlImage, "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif languageOrigin in "en":
            self.wfile.write(bytes("<html><head><title>Translator</title></head><meta charset=\"utf-8\" />", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Origin Language: %s</p>" % self.getLanguageFrom(result), "utf-8"))
            self.wfile.write(bytes("<p>Result: %s</p>" % result, "utf-8"))
            self.wfile.write(bytes("<p>Target Language: %s</p>" % self.getLanguageName(languageTarget), "utf-8"))
            self.wfile.write(bytes("<p>Result Translated: %s</p>" % tranlated, "utf-8"))
            self.wfile.write(bytes("<br>{:.2f}%<br>".format(100 * np.max(score)), "utf-8"))
            self.wfile.write(bytes("<img src=\"%s\" alt=\"Image\" width=\"500\" height=\"600\">" % urlImage, "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.wfile.write(bytes("<html><head><title>Translator</title></head><meta charset=\"utf-8\" />", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Origin Language: %s</p>" % self.getLanguageFrom(result), "utf-8"))
            self.wfile.write(bytes("<p>Result: %s</p>" % result, "utf-8"))
            self.wfile.write(bytes("<p>Target Language: %s</p>" % self.getLanguageName(languageTarget), "utf-8"))
            self.wfile.write(bytes("<p>Result Translated: %s</p>" % tranlated, "utf-8"))
            self.wfile.write(bytes("<br>{:.2f}%<br>".format(100 * np.max(score)), "utf-8"))
            self.wfile.write(bytes("<img src=\"%s\" alt=\"Image\" width=\"500\" height=\"600\">" % urlImage, "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

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



