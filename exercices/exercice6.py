import cv2 as cv
import numpy as np
def exercice6():
    # Chargement des images étiquette lait
    etalon = cv.imread('ressources/images/1.BMP', cv.IMREAD_GRAYSCALE)
    lait_ko = cv.imread('ressources/images/LAIT_KO.bmp', cv.IMREAD_GRAYSCALE)
    lait_ok = cv.imread('ressources/images/LAIT_OK.bmp', cv.IMREAD_GRAYSCALE)

    # Calcul des projections
    projection_lignes = np.sum(lait_ok, axis=1) # somme par ligne=projection verticale
    projection_colonnes = np.sum(lait_ok, axis=0) # somme par colonne=projection horizontale

    # Identifier les bords de l'image
    seuil_projection = np.max(projection_lignes) / 2
    ligne_debut = np.argmax(projection_lignes > seuil_projection) # front montant
    ligne_fin = len(projection_lignes) - np.argmax(projection_lignes[::-1] > seuil_projection) #front descendant
    seuil_projection = np.max(projection_colonnes) / 2
    colonne_debut = np.argmax(projection_colonnes > seuil_projection) # front montant
    colonne_fin = len(projection_colonnes) - np.argmax(projection_colonnes[::-1] >seuil_projection) # front descendant

    # Affichage des lignes et colonnes de l'extraction
    print(f"Ligne début : {ligne_debut} ; Ligne fin : {ligne_fin}\n"
    f"Colonne début : {colonne_debut} ; Colonne fin : {colonne_fin}")

    # Affichage de l'extraction d'après les projections
    lait_ok_extrait = lait_ok[ligne_debut:ligne_fin, colonne_debut:colonne_fin]
    cv.imshow("lait OK", lait_ok)
    cv.waitKey(0)
    cv.imshow("lait OK extrait", lait_ok_extrait)
    cv.waitKey(0)

    ### Extraction de la date
    X_decalage = 57
    Y_decalage = 303
    date_lait_ok = lait_ok_extrait[Y_decalage:Y_decalage + 95, X_decalage:X_decalage + 41]
    cv.imshow("date lait OK", date_lait_ok)
    cv.waitKey(0)
    _, date_lait_ok_binary = cv.threshold(date_lait_ok, 0, 255, cv.THRESH_BINARY_INV +cv.THRESH_OTSU)
    cv.imshow("date lait OK binarise", date_lait_ok_binary)
    cv.waitKey(0)
    ## Extraction du premier caractère de la date
    # Trouver les contours
    contours_date,_= cv.findContours(date_lait_ok_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # print(f"Nb caractères détectés: {len(contours_date)}")
    # extraire le premier contour détecté (le plus à gauche donc)
    x, y, w, h = cv.boundingRect(contours_date[0])
    premier_caractere_date = date_lait_ok_binary[y:y + h, x:x + w]
    cv.imshow("premier caractere date (1)", premier_caractere_date)
    cv.waitKey(0)