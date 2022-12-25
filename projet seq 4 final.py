import os
import six

def menu():                             #j'ai utilisé la fonction menu pour définir mon programme entier car il était demandé 3 fontions (dans le cahier des charges).
    print('0-quitter\n1-écrire dans le répertoire\n2-Rechercher dans le répertoire')
    a=int(input('votre choix ?\n'))
    while a!=0:                         #je créer ma boucle while pour que la fonction lecture et écriture soit valable tant que l'utilisateur n'a pas appuyé sur 0 (comme demandé dans le cahier des charges).
        while a==1:                     #une autre boucle pour recommencer le programme (pour la valeur 1) tant que l'utilisateur appuie sur cette même touche.
             nom=input('Nom (0 pour terminer): ')
             if nom==str(0):
                 print('0-quitter\n1-écrire dans le répertoire\n2-Rechercher dans le répertoire')
                 a=int(input('votre choix ?\n'))
                 if a==0:               #je casse la boucle si a==0. Autrement dit, je renvoie l'utilisateur sur l'interface (là où il fait son choix).
                     break
             else:
                 numéro=input('téléphone : ')
                 def écriture():        #la définition de ma fonction écriture().
                     monFichier=open('fichier.txt','a')
                     monFichier.write(nom)
                     monFichier.write('\n')
                     monFichier.close()

                     monFichier=open('fichier.txt','a')
                     monFichier.write(numéro)
                     monFichier.write('\n')
                     monFichier.write('\n')
                     monFichier.close()
                 écriture()
        while a==2:
            def lecture():              #la définition de ma fonction lecture().
                monFichier=open("fichier.txt","r")
                ok=input('Entrer un nom : ')
                while ok.isdigit():
                    print("\nRentrez une chaine de caractère !")
                    ok=input('Entrer un nom : ')
                    if not ok.isdigit() :
                        break
                tableau=monFichier.readlines()
                y=0
                numéro=0
                
                for line in tableau:    #je met mon fichier dans un tableau pour pouvoir lire chaque ligne de ce tableau facilement.
                    if ok in tableau[y]:
                        numéro=tableau[y+1]
                    else:
                        y=y+1

                if type(numéro) is str:
                    numéro=int(numéro)
                if numéro !=0 :
                    print('le numéro recherché est : ', numéro)
                else:
                    print('Nom inconnu\n')
            lecture()
            print('0-quitter\n1-écrire dans le répertoire\n2-Rechercher dans le répertoire')
            a=int(input('votre choix ?\n'))
            if a==0:                    #je casse la boucle si a==0 (pareil qu'au début).
                break
menu()                                  #j'affiche la fonction menu(), donc le programme entier ^^

