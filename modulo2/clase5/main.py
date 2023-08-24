from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# font https://fonts.google.com/specimen/Roboto

def get_image(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.mode)
        print(image.format)
        
        #image.show()
        
        #image_blackwhite = image.convert('L')
        #image_blackwhite.show()
        #image_blackwhite.save('edcamp22_bn.jpg')
        
        font = ImageFont.truetype('fonts/Roboto-Bold.ttf',120)
        draw = ImageDraw.Draw(image)
        draw.text(
            (500,0),
            "EDCAMP 2022",
            (255,255,255),
            font
        )
        image.show()
        image.save('edcamp22_font.jpg')
        
        #create thumbnail
        image.thumbnail((500,500))
        image.show()
        image.save('edamp22_thumnail.jpg')
        
        
    except:
        print('no se encontro la imagen')

if __name__ == '__main__':
    get_image('edcamp22.jpg')