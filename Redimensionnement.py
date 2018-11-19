from PillowPIL import Image

def resize(patern_path):
    for file in patern_path :
        o_file=Image.open(file)
        Image.thumbnail(300,300)
        Image.save(str(file)[:-3]+'_resized')

