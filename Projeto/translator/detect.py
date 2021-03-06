from PIL import Image
from tensorflow import keras
import numpy as np
import tensorflow as tf
from PIL import Image
from urllib import request
from io import BytesIO

class DetectorImg:

    MODEL = keras.models.load_model('IA.pth')
    CLASS_NAMES = ['bee', 'spider', 'bicycle', 'butterfly', 'dog', 'car', 'horse', 'rabbit', 'dandelion', 'elephant', 'squirrel', 'grasshopper', 'chicken', 'cat', 'giraffe', 'sunflower', 'hamster', 'ladybug', 'lion', 'dragonfly', 'daisy', 'monitor', 'mosquito', 'motorcycle', 'mouse', 'sheep', 'panda', 'rose', 'turtle', 'keyboard', 'tulip', 'cow', 'deer', 'zebra']
    SCORE = ""

    def callIa(self,contents):
        
        img_height = 130
        img_width = 130

        res = request.urlopen(contents).read()
        img = Image.open(BytesIO(res)).resize((img_height,img_width))

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = self.MODEL.predict(img_array)
        return predictions

    def getScore(self,contents):
        predictions = self.callIa(contents)
        score = tf.nn.softmax(predictions[0])
        self.SCORE = score
        return "{:.2f}%".format(100 * np.max(score))
        
    def getResult(self):
        result = self.CLASS_NAMES[np.argmax(self.SCORE)]
        return result
    
