
# Dégradation de la photo

import tinify as tnf

tnf.key='TZJwLKXznS28ZD89zj68489qn3RjtqkT'          #clé API

source = tnf.from_file('C:/Users/gui-f/CW2/AIY_Projet-semaine-2/MACRON_001.png')       #origine de l'image à compresser
source.to_file("compressed.jpg")                                                  #nom de l'image compressé




