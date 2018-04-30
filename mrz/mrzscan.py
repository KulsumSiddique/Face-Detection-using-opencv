import numpy as np
import cv2
# from passporteye.mrz.image import MRZPipeline
from passporteye import read_mrz 

# p = MRZPipeline("passport_01.jpg")
# mrz = p.result

mrz = read_mrz("passport_01.jpg", save_roi=True)
mrz.to_dict(mrz)
# mrz = read_mrz("passport_01.jpg")


# import Image
# from tesseract import image_to_string

# print image_to_string(Image.open('test.png'))
# print image_to_string(Image.open('test-english.jpg'), lang='eng')