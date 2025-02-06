import subprocess

# def unzip_with_7z(zip_file_path, dest_path, password):
#     try:
#         # Commande pour décompresser le fichier 7z avec mot de passe
#         command = ['7z', 'x', zip_file_path, f'-p{password}', f'-o{dest_path}']
#         subprocess.run(command, check=True)
#         return True  # Si la commande a réussi
#     except subprocess.CalledProcessError:
#         return False  # Si la commande échoue (mot de passe incorrect)
#utils n'était pas trouver sur mon pc donc j'ai fait une fonction qui va avoir la même utilité
#cette fonction n'est plus utile car j'ai rectifier mon problème avec le utils.py
# ----------------------------------------
from utils import unzip_with_7z 

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------


import string

def find_password():
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            find_me = a + b
            secret_password = find_me + 'bcmpda'
            print(f"Trying password: {secret_password}")  # montrer le mot de passe en cours
            if unzip_with_7z(zip_file_path, dest_path, secret_password):
                print(f"Success! The password is: {secret_password}")
                return secret_password
    print("Password not found.")
    return None
find_password()

#résultat "dibcmpda" est le mot de passe

#façon supplémentaire sans l'utilisation de la fonction def find_password() mais avec l'utilisation de exit() pour arreter la boucle
# for a in string.ascii_lowercase:
#         for b in string.ascii_lowercase:
#             find_me = a + b
#             secret_password = find_me + 'bcmpda'
#             print(f"Trying password: {secret_password}")  # montrer le mot de passe en cours
#             if unzip_with_7z(zip_file_path, dest_path, secret_password):
#                 print(f"Success! The password is: {secret_password}")
#                 exit()
#         print("Password not found.")
