#tâche n°3: Ecriture du code qui ressort un fichier excel avec le nom de la personne associé à un numéro de photo (c’est une table d’une base de données)

from xlwt import Workbook


def fichier_excel(Listcouplephotopers):
    # création du fichier excel
    book=Workbook()

    # création de la feuille 1
    feuil1=book.add_sheet('feuille 1')

    # ajout des en-têtes
    feuil1.write(0,0,'identifiant photo')
    feuil1.write(0,1,'nom personne')
    for rangcouple in range(len(Listcouplephotopers)):
        lignerangcouple=feuil1.row(rangcouple+1)
        lignerangcouple.write(0,Listcouplephotopers[rangcouple][0])
        lignerangcouple.write(1,Listcouplephotopers[rangcouple][1])
    book.save('excel_photo_personne')
    return

monRepertoire="C:/Users/pc antoine/Desktop/semaine2/AIY_Projet-semaine-2/tache 1 base de données groupe de 5/Bee4 photos pics"
from os import listdir
from os.path import isfile, join



def listeImages_noms(monRepertoire):
    fichiers=[f for f in listdir(monRepertoire) if isfile(join(monRepertoire, f))]
    L=[]
    for image in fichiers:



