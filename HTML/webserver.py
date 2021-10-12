from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import boto3
from tensorflow import keras
import numpy as np
import tensorflow as tf
from PIL import Image
import pandas as pd
import base64
import json

class Requests(BaseHTTPRequestHandler):

    languageOrigin = ""
    languageTarget = ""
    imageLink = ""
    imageCode = ""

    def translate(self,phrase,target,origin):
        credencials = pd.read_csv('credencials\Credencials.csv', sep=',', encoding='utf-8')
        
        client = boto3.client('translate', region_name="us-east-1",aws_access_key_id= credencials['Access key ID'][0],
            aws_secret_access_key= credencials['Secret access key'][0])

        return client.translate_text(Text=phrase, SourceLanguageCode=origin,TargetLanguageCode=target)['TranslatedText']

    def getReturn(self,result,score):

        translatedInsert = self.translate(result,languageOrigin,'en')
        translated = self.translate(result,languageTarget,languageOrigin)

        self.wfile.write(bytes("<html><head><title>Return</title></head><meta charset=\"utf-8\"/>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<center>", "utf-8"))
        self.wfile.write(bytes("<p><h1>Result</h1></p>", "utf-8"))
        self.wfile.write(bytes("<p><h2>%s</h2></p>" % translatedInsert, "utf-8"))
        self.wfile.write(bytes("<p><h1>Traslated</h1></p>", "utf-8"))
        self.wfile.write(bytes("<p><h2>%s</h2</p>" % translated, "utf-8"))
        self.wfile.write(bytes("<br>{:.2f}%<br>".format(100 * np.max(score)), "utf-8"))
        self.wfile.write(bytes("<img alt='Embedded Image' src='data:image/png;base64,%s' height=\"500\" width=\"500\"/>" % imageCode, "utf8"))
        self.wfile.write(bytes("<form>", "utf-8"))
        self.wfile.write(bytes("<input type=\"button\" value=\"Return\" onclick=\"history.back()\">", "utf-8"))
        self.wfile.write(bytes("</form>", "utf-8"))
        self.wfile.write(bytes("</center>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()


    def do_GET(self):
        self._set_response()

        class_names = ['butterfly', 'dog', 'dandelion', 'locust', 'cat', 'sunflower', 'ladybird', 'dragonflies', 'daisy', 'monitor', 'mosquito', 'mouse', 'rose', 'keyboard', 'tulip']

        model = keras.models.load_model('projetoUsandoTransferLearning.pth')
        img_height = 130
        img_width = 130

        image_result = open('image.jpg', 'wb') # create a writable image and write the decoding result
        image_result.write(imageLink)

        img = keras.preprocessing.image.load_img('image.jpg', target_size=(img_height, img_width))

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        result = class_names[np.argmax(score)]
        
        logging.info(languageOrigin)
        logging.info(languageTarget)

        self.getReturn(result,score)
        

    def do_POST(self):
        self._set_response()
        logging.info('POST\n')

        global languageOrigin
        global languageTarget
        global imageCode
        global imageLink

        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length)
        resultPost = json.loads(post_data.decode('utf-8'))

        #if(self.path == "/image"):
        imageCode = resultPost['image']
        imageLink = base64.b64decode(imageCode)
        
        logging.info("Image Code: "+imageCode+"\n")
        #else:
        languageOrigin = resultPost['origin']
        languageTarget = resultPost['target']
        logging.info("Origin: "+languageOrigin+"\n")
        logging.info("Target: "+languageTarget+"\n")


def run(server_class=HTTPServer, handler_class=Requests, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.timeout = 60
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    run()

