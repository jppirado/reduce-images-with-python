# from PIL import Image

# import os, sys 

# caminho = (os.path.join('img'))

# dirs =  os.listdir(caminho)

# def resize():
#     for item in dirs: 
#         if os.path.isfile(item):
#             im = Image.open(item)
#             f, e = os.path.splitext(item)
#             size = im.size
        
#             ratio = float(final_size) / max(size)

#             new_image_size = tuple([int(x*ratio) for x in size])

#             im = im.resize(new_image_size, Image.ANTIALIAS)
#             new_im = Image.new("RGB", (final_size, final_size))
#             new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
#             new_im.save(f + 'resized.jpg', 'JPEG', quality=10)

# resize()

from genericpath import isdir
from PIL import Image
import os, sys

path = caminho = (os.path.join('img'))
save_path = caminho = (os.path.join('img2'))
images = os.listdir(path)
resize_ratio = 0.5 

if not os.path.isdir(save_path):
    os.makedirs(save_path)


for image in images:
    image_path = os.path.join(path, image)
    iamge_save_path = os.path.join(save_path, image)
    if image.split(".")[1] not in ["jpg", "png" , "jpeg"]:
        continue
    if os.path.exists(image_path):
        im = Image.open(image_path)
        new_image_height = int(im.size[0] / (1/resize_ratio))
        new_image_length = int(im.size[1] / (1/resize_ratio))
        image = im.resize((new_image_height, new_image_length), Image.ANTIALIAS)

        # image_resized = im.resize((1024,1024))
        
        image.save(iamge_save_path, quality=90)
        print("saved")
