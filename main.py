import os, glob
from pathlib import Path
from os import walk

# Lister et identifier les fichiers et dossiers
input_path = input('Entrez le chemin dun dossier : ')

dossier = Path(input_path)

for fichier in dossier.iterdir():
    if os.path.isdir(fichier):
        print(f'Dossier : {fichier.name}')
    elif os.path.isfile(fichier):
        print(f'Fichier : {os.path.basename(fichier)}')

# Création de dossiers
creation_dossier = input('Entrez le chemin du dossier à créer : ')
if os.path.exists(creation_dossier) == True:
    print('Le dossier deja existe')
else:
    os.mkdir(creation_dossier)
    print('Le dossier a été créé avec succès')

# Recherche d’un fichier spécifique
chercher_dossier = input('Entrez le nom du fichier à rechercher : ')
dossier_of_search = input('Entrez le dossier de recherche : ')
if os.path.exists(f'{dossier_of_search}/{chercher_dossier}'):
    print(f'Fichier trouvé :  {os.path.abspath(chercher_dossier)}')

if dossier_of_search == '.':
    for (root,dirs,files) in os.walk('.'):
        if chercher_dossier in files:
            print(os.path.join(root, chercher_dossier))
    
elif os.path.exists(f'{dossier_of_search}/{chercher_dossier}') == False:
    print('Fichier non trouvé')

# Suppression d’un fichier
delete_file = input('Entrez le chemin du fichier à supprimer :  ')
if(os.path.exists(delete_file) == True):
    os.remove(delete_file)
    print('Le fichier a été supprimé avec succès')
else:
    print('Le fichier n’existe pas')


# # Arborescence complète d'un dossier
# tree_path = input('Entrez le chemin du dossier : ')


# Ecriture dans un fichier
fruits = ['Pomme', 'Banane', 'Orange', 'Mangue', 'Fraise']
pathfruits = 'data/fruits.txt'

def addFruits(fruitslsit, pathfruits):
    with open(pathfruits, "w") as fichier:
        fichier.write('\n'.join(fruitslsit))

addFruits(fruits, pathfruits)

print(f'Fruits écrits dans le fichier : {pathfruits}')
print('Contenu du fichier :')
with open(pathfruits, "r") as fichier:
    print(fichier.read())

# Copie d’un fichier
fileforcopy = input('Entrez le chemin du fichier à copier : ')
wherecopyfile = input('Entrez le chemin de destination : ')
if os.name == 'nt':  # Windows
    cmd = f'copy "{fileforcopy}" "{wherecopyfile}"'
else:  # Unix/Linux
    cmd = f'cp "{fileforcopy}" "{wherecopyfile}"'

if os.path.exists(fileforcopy):
    os.system(cmd)
    print('Le fichier a été copié avec succès')
    print(f'Contenu du fichier {wherecopyfile} :')
    with open(wherecopyfile, "r") as fichier:
        print(fichier.read())
else:
    print('Le fichier n’existe pas')


# Statistiques sur un répertoire
statpath = input('Entrez le chemin du dossier : ')
statdossier = Path(statpath)
countfichier = 0
countdossier = 0

for fichier in statdossier.iterdir():
    if os.path.isdir(fichier):
        countdossier = countdossier + 1
    elif os.path.isfile(fichier):
        countfichier = countfichier + 1

print(f'Nombre de fichiers : {countfichier}')
print(f'Nombre de dossiers : {countdossier}')


# Recherche de fichiers par extension
extencion = input('Entrez extension de fichier à rechercher (ex. : .txt) : ')
path_exten =  input('Entrez le chemin du dossier à rechercher : ')
count_exten = 0

if path_exten == '.':
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".txt"):
                count_exten = count_exten + 1
else:
    for file in os.listdir(path_exten):
        if file.endswith(".txt"):
            count_exten = count_exten + 1

print(f'Nombre de fichiers trouvés : {count_exten}')

if path_exten == '.':
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".txt"):
                print(f'Fichier trouvé :  {os.path.abspath(file)}')
else:
    for file in os.listdir(path_exten):
        if file.endswith(".txt"):
            print(f'Fichier trouvé :  {os.path.abspath(file)}')

