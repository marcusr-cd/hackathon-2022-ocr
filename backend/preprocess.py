from ssl import ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
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

# def transform_image(image):
#   original = image.copy()
#   (H, W) = image.shape[:2]
#   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#   blur = cv2.GaussianBlur(gray, (7, 7), 0)
#   edged = cv2.Canny(blur, 60, 160)
#   contours = find_contours(edged.copy())

#   for c in contours:
#     peri = cv2.arcLength(c, True)
#     aprox = cv2.approxPolyDP(c, 0.02 * peri, True)

#     if len(aprox) == 4:
#       maior = aprox
#       break
#   cv2.drawContours(image, maior, -1, (120, 255, 0), 28)
#   cv2.drawContours(image, [maior], -1, (120, 255, 0), 2)
#   pontonsMaior = ordenar_pontos(maior)
#   pts1 = np.float32(pontosMaior)
#   pts2 = np.float32([[0,0], [W, 0], [W, H], [0, H]])

#   matriz = cv2.getPerspectiveTransform(pts1, pts2)
#   transform = cv2.warpPerspective(original, matriz, (W, H))

#   return transform

# def processamento_img(img)

def preprocess(file, filename):
  img = convert2Image(file, filename)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  return otsu