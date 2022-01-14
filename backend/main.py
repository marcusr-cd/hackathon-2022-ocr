from flask import Flask, request
from flask_cors import CORS
from preprocess import preprocess
from postprocess import postprocess

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def ocr():

  file = request.files['image'].read()
  image_preprocessed = preprocess(file, request.files['image'].filename)
  response = postprocess(image_preprocessed)

  return response


app.run(debug=True)


