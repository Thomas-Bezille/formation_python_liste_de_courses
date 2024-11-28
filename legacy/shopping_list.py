import os, sys, json

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = "liste.json"


if os.path.isfile(DATA_FILE):
    with open(f"{CUR_DIR}\\{DATA_FILE}", "r") as f:
        datas = json.load(f)
else:
    with open(f"{CUR_DIR}\\{DATA_FILE}", "w") as f:
        json.dump([], f, indent=4)
    with open(f"{CUR_DIR}\\{DATA_FILE}", "r") as f:
        datas = json.load(f)


while True:
    choice = input("Choisissez parmi les 5 options suivantes :\n\t1: Ajouter un article à la liste\n\t2: Supprimer un article de la liste\n\t3: Afficher la liste\n\t4: Vider la liste\n\t5: Sauvegarder\n👉 Votre choix : ")
    
    match choice:
        case "1":
            item = input("Quel article souhaitez-vous ajouter à la liste ? ")
            datas.append(item)
            print(f"{item} a été ajouté à la liste.\n---------------------------------")
        case "2":
            item = input("Quel article souhaitez-vous supprimer de la liste ? ")
            datas.remove(item)
            print(f"{item} a été supprimé de la liste.\n---------------------------------")
        case "3":
            if datas:
                print("Voici votre liste de courses :")
                for index, item in enumerate(datas):
                    print(f"{index + 1}: {item}")
            else:
                print("La liste est vide.")
            print("---------------------------------")
        case "4":
            datas.clear()
            print("La liste a été vidée.\n---------------------------------")
        case "5":
            with open(f"{CUR_DIR}\\{DATA_FILE}", "w") as f:
                json.dump(datas, f, indent=4)
            print("Votre liste de course a bien été sauvegarder. Au revoir !")
            sys.exit()
        case _:
            print("Choix invalide. Veuillez taper un nombre qui correspond à un choix (1 - 5).\n---------------------------------")