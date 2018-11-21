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
