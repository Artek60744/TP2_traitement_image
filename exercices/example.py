import numpy
def example():
    ecole = 'unilasalle'
    print(ecole[3:7]) # s'affiche: lasa
    print(ecole[5:]) # s'affiche: salle
    print(ecole[:3]) # s'affiche: uni
    # Déclaration en dur d'un tableau T à 2 lignes et 3 colonnes
    T = numpy.array([[1, 2, 3], [4, 5, 6]])
    T2 = T[:, 0:2]
    # T2 vaut : [1, 2],
    # [4, 5]
    # -> extraction de toutes les lignes et des 2 premières colonnes de T