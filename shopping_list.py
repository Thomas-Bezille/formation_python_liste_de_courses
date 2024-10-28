shopping_list = []

while True:
    choice = input("Choisissez parmi les 5 options suivantes :\n\t1: Ajouter un article à la liste\n\t2: Supprimer un article de la liste\n\t3: Afficher la liste\n\t4: Vider la liste\n\t5: Quitter\n👉 Votre choix : ")
    
    match choice:
        case "1":
            item = input("Quel article souhaitez-vous ajouter à la liste ? ")
            shopping_list.append(item)
            print(f"{item} a été ajouté à la liste.\n---------------------------------")
        case "2":
            item = input("Quel article souhaitez-vous supprimer de la liste ? ")
            shopping_list.remove(item)
            print(f"{item} a été supprimé de la liste.\n---------------------------------")
        case "3":
            if shopping_list:
                print("Voici votre liste de courses :")
                for index, item in enumerate(shopping_list):
                    print(f"{index + 1}: {item}")
            else:
                print("La liste est vide.")
            print("---------------------------------")
        case "4":
            shopping_list.clear()
            print("La liste a été vidée.\n---------------------------------")
        case "5":
            print("Au revoir !")
            break
        case _:
            print("Choix invalide. Veuillez taper un nombre qui correspond à un choix (1 - 5).\n---------------------------------")