# 我已经把识别的tesseract 放在了环境变量里面.  C:\Program Files (x86)\Tesseract-OCR 地址是这个
from PIL import Image
from pytesser import *
from pyocr import pyocr
def mian() :
    # im = Image.open('fnord.tif')
    # im = Image.open('phototest.tif')
    # im = Image.open('eurotext.tif')
    im = Image.open(r'C:\Users\Administrator\Desktop\tps-550\ocr\11.png')

    text = image_to_string(im)
    print text

    # width = 60 * 4
    # height = 60
    # image = Image.new('RGB', (width, height), (255, 255, 255))
    #
    # # create Font object
    # # font = ImageFont.truetype('Arial.ttf', 36)
    # # draw = ImageDraw.Draw(image)
    # image = image.filter(ImageFilter.BLUR)
    # image.save('code.jpg', 'jpeg')



if __name__ == '__main__':
    mian()
