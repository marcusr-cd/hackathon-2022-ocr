import numpy as np
from flask import Flask, request
from flask_cors import CORS
import pytesseract, cv2
from pytesseract.pytesseract import Output
from pdf2image import convert_from_bytes
from io import BytesIO
from PIL import Image
import json

######################################################## PRE PROCESS ########################################################
MIN_CONF = 10.0

def convert2Image(file, filename):
  img = file
  if (filename.lower().endswith('.pdf')):
    page = convert_from_bytes(file)[0]
    buffer = BytesIO()
    page.save(buffer, format="jpeg")
    img = buffer.getbuffer()
  return cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_UNCHANGED)

def preprocess(file, filename):
  img = convert2Image(file, filename)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  return otsu

######################################################## POST PROCESS ########################################################
CONFIG_TESSERACT = '--tessdata-dir ../tessdata'
LANG='eng'
class Object:
  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

response = Object()

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
      return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def checkValidation(layout, data):
    validation = layout['validation']
    if (validation):
      validationText = getValue(data, validation).upper()
      return validationText == validation['text']
    return True

def getValue(data, fieldContent):
  top = fieldContent['top']
  fromLeft = fieldContent['from']
  toLeft = fieldContent['to']
  resultText = ''
  for i in range(0, len(data['text'])):
    confidence = float(data['conf'][i])
    if (confidence > MIN_CONF and len(data['text'][i]) > 0):
      if (top == int(data['top'][i]) and fromLeft <= int(data['left'][i]) and toLeft >= int(data['left'][i])):
        resultText += ' ' + data['text'][i]
        resultText = resultText.strip()
  return resultText

def getValues(layout, data):
  response = Object()
  for field in layout['fields']:
    for i in range(0, len(layout['fields'][field])):
      if (hasattr(response, field)):
        currentValue = getattr(response, field)
        setattr(response, field, currentValue + ' ' + getValue(data, layout['fields'][field][i]))
      else:
        setattr(response, field, getValue(data, layout['fields'][field][i]))
  return response.toJSON()

def postprocess(image):
  f = open('layouts/bc-hydro-bill.json')
  layout = json.loads(f.read())
  f.close()
  
  data = pytesseract.image_to_data(image, lang=LANG, config=CONFIG_TESSERACT, output_type=Output.DICT)
  text = pytesseract.image_to_string(image, lang=LANG, config=CONFIG_TESSERACT, output_type=Output.DICT)

  if checkValidation(layout, data):
    return getValues(layout, data)
  return 'This file is not supported yet'


############################################################################################################################################
app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def ocr():

  file = request.files['image'].read()
  image_preprocessed = preprocess(file, request.files['image'].filename)
  text = postprocess(image_preprocessed)

  return text


app.run(debug=True)


