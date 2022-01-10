import numpy as np
from flask import Flask, request
import pytesseract, cv2
from pytesseract.pytesseract import Output

app = Flask(__name__)


MIN_CONF = 40


def preprocess(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  return otsu

def postprocess(image):
  config_tesseract = '--tessdata-dir ../tessdata'
  result = pytesseract.image_to_data(image, lang='eng', config=config_tesseract, output_type=Output.DICT)
  text = ''

  for i in range(0, len(result['text'])):
    # confidence = int(result['conf'][i])
    # if (confidence > MIN_CONF and len(result['text'][i]) > 0):
    #   text += '['+str(i)+']'+result['text'][i]+';'

    response = {
      'surname': result['text'][8][:-1],
      'firstname': result['text'][10],
      'dob': result['text'][22],
      'address': result['text'][63] + ' ' + result['text'][64]+ ' ' + result['text'][65]+ ' ' + result['text'][67]+ ' ' + result['text'][68]+ ' ' + result['text'][69]+ ' ' + result['text'][70],
    }

  return response


@app.route("/", methods=['POST'])
def ocr():

  img = cv2.imdecode(np.fromstring(request.files['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image_preprocessed = preprocess(img)
  text = postprocess(image_preprocessed)

  return text


app.run(debug=True)


