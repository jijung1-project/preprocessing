import os
import glob
from skimage.transform import resize
import skimage.io as io
from skimage.io import imsave
from PIL import Image

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        if filename !='.DS_store':
             full_dirname = os.path.join(dirname, filename)
             filenames = os.listdir(full_dirname)
        for i in range(0, 300):
            img = Image.open(full_dirname+'/'+filenames[i])
            img = img.convert("RGB")
            img_resize = img.resize((128,128))
            img_resize.save(full_dirname+'/'+filenames[i], "JPEG", quality=95)

search("/Users/jaewan/Desktop/food_img")





