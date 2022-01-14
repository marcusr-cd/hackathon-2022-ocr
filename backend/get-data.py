# This file return a JSON with all the text positions of some image

from flask import Flask, request
import pytesseract
from pytesseract.pytesseract import Output
from pdf2image import convert_from_bytes
import json
import preprocess

app = Flask(__name__)

MIN_CONF = 10.0

######################################################## POST PROCESS ########################################################

def postprocess(image):
  config_tesseract = '--tessdata-dir ../tessdata'
  data = pytesseract.image_to_data(image, lang='eng', config=config_tesseract, output_type=Output.DICT)

  class Result:
    top = 0
    left = 0
    text = ""
    conf = 0

    def __init__(self, top, left, text, conf):
        self.top = top
        self.left = left
        self.text = text
        self.conf = conf

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

  result = []
  for i in range(0, len(data['text'])):
    confidence = float(data['conf'][i])
    if (confidence > MIN_CONF and len(data['text'][i]) > 0):
      result.append(Result(data['top'][i], data['left'][i], data['text'][i], data['conf'][i]).toJSON())


  return json.dumps(result)

############################################################################################################################################

@app.route("/", methods=['POST'])
def ocr():

  file = request.files['image'].read()
  image_preprocessed = preprocess.preprocess(file, request.files['image'].filename)
  text = postprocess(image_preprocessed)

  return text


app.run(debug=True)


