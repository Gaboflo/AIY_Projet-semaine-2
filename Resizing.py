import tinify as tnf
import os
import os.path
tnf.key = "sVpXGh6F76fcvx3D7LBCf2ZRfVYHnFKn"


def resized_only(path):
    extension_list =['jpg', 'jpeg', 'png', 'gif']
    ###Création d'un nouveau dossier pour mettre les images resizer###
    new_dossier = path + '/resized/'
    print(new_dossier)
    if not os.path.exists(new_dossier):
        os.mkdir(new_dossier)

    ###listing de tous les fichiers photos###
    picture_list = [ f for f in os.listdir(path) if (os.path.isfile(os.path.join(path,f)) and f.split(".")[1]in extension_list)]

    ###Création des fichiers compressés###
    for element in picture_list :
        extension=element.split(".")                                        #sous le format [nom du fichier, extension]
        source = tnf.from_file(path+ '/'+ element)                          #On prend un fichier du path
        new_path = new_dossier + extension[0] + '_resized.' + extension[1]  #Nouvelle direction du fichier compressé
        source.to_file(new_path)                                            #Ecriture du fichier compressé
        print('Resizing suceed in ' + new_path)                             #Message de validation


resized_only(r"E:/tests_politique")
