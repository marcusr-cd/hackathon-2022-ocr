import numpy as np
import cv2
from pdf2image import convert_from_bytes
from io import BytesIO

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

  _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  return otsu