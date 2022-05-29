from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = Image.open("omg.png")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)