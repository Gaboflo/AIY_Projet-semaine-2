from PIL import Image
import numpy as np
from resizeimage import resizeimage

def resize(patern_path):
    for file in patern_path :
        with open(file, 'r+b') as f:

            with Image.open(f) as image:
                matrice_taille=misc.imread(file)
                ratio=matrice_taille.shape[0,1]

                image_resized= image +  '_resized'
                cover = resizeimage.resize_cover(image, ratio[0],ratio[1])

                #identification(cover)
