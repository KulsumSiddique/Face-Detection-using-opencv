# try:
#     import Image
# except ImportError:
#     from PIL import Image
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# # Include the above line, if you don't have tesseract executable in your PATH
# # Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

# # Simple image to string
# print(pytesseract.image_to_string(Image.open('test.jpg')))

from PIL import Image
from pytesser import *
 
image_file = 'test.tiff'
im = Image.open(image_file)
text = image_to_string(im)
text = image_file_to_string(image_file)
text = image_file_to_string(image_file, graceful_errors=True)
print ("=====output=======\n")
print (text)