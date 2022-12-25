import os
import six

path = os.getcwd()

def menu():                             #j'ai utilisé la fonction menu pour définir mon programme entier car il était demandé 3 fontions (dans le cahier des charges).   
    print('1-quitter\n2-écrire dans le répertoire\n3-Rechercher dans le répertoire')
    a=int(input('votre choix ?\n'))

    while a!=1:                         #je créer ma boucle while pour que la fonction lecture et écriture soit valable tant que l'utilisateur n'a pas appuyé sur 1
                                        #(comme demandé dans le cahier des charges).
        while a==2:                     #une autre boucle pour recommencer le programme (pour la valeur 1) tant que l'utilisateur appuie sur cette même touche.
             nom=input('Nom (1 pour terminer): ')
             if nom==str(1):
                 print('1-quitter\n2-écrire dans le répertoire\n3-Rechercher dans le répertoire')
                 a=int(input('votre choix ?\n'))
                 if a==1:               #je casse la boucle si a==1. Autrement dit, je renvoie l'utilisateur sur l'interface (là où il fait son choix).
                     break
             else:
                 numéro=input('téléphone : ')
                 def écriture():        #la définition de ma fonction écriture().
                     monFichier=open(path+'/fichier.txt','a')
                     monFichier.write(nom)
                     monFichier.write('\n')
                     monFichier.close()

                     monFichier=open(path+'/fichier.txt','a')
                     monFichier.write(numéro)
                     monFichier.write('\n')
                     monFichier.write('\n')
                     monFichier.close()
                 écriture()
        while a==3:
            def lecture():              #la définition de ma fonction lecture().
                monFichier=open("fichier.txt","r")
                ok=input('Entrer un nom : ')
                while ok.isdigit():         #je vérifie que l'input est bien un str sinon je rentre dans une boucle while
                    print("\nRentrez une chaine de caractère !")        #je dis à l'utilisateur de rentrer une chaine de caractère
                    ok=input('Entrer un nom : ')                        #je redemande de rentrer un nom
                    if not ok.isdigit() :                               #si il rentre une chaine de caractère alors je quitte la boucle while
                        break
                tableau=monFichier.readlines()
                y=0
                numéro=None
                
                for line in tableau:            #je met mon fichier dans un tableau pour pouvoir lire chaque ligne de ce tableau facilement.
                    if ok in tableau[y]:        #si le nom rentré correspond à une valeur dans le fichier
                        numéro=tableau[y+1]     #le numéro prendra la ligne en dessous du nom
                    else:
                        y=y+1                   #sinon j'itère sur la suite de mon tableau

                if type(numéro) is str:         #si le numéro est une chaine de caractère
                    numéro=int(numéro)          #je la transforme en int (le write la transforme en str)
                if numéro is not None :
                    print('le numéro recherché est : ', numéro)     #j'affiche le numéro si le numéro n'est pas nul
                else:
                    print('Nom inconnu\n')                          #sinon je dis que l'utilisateur est inconnu
            lecture()
            print('1-Quitter\n2-Écrire dans le répertoire\n3-Rechercher dans le répertoire')
            a=int(input('votre choix ?\n'))
            if a==1:                    #je casse la boucle si a==1 (pareil qu'au début).
                break
menu()                                  #j'affiche la fonction menu(), donc le programme entier ^^

if os.path.exists(path+"/fichier.txt"):
    os.remove(path+"/fichier.txt")    # Supprime le fichier "mon_fichier.txt"
    print("le fichier a été supprimé")
else:
    print("le fichier n'existait pas")