shopping_list = []

while True:
    choice = input("Choisissez parmi les 5 options suivantes :\n1: Ajouter un article à la liste\n2: Supprimer un article de la liste\n3: Afficher la liste\n4: Vider la liste\n5: Quitter\n👉 Votre choix : ")
    
    match choice:
        case "1":
            item = input("Quel article souhaitez-vous ajouter à la liste ? ")
            shopping_list.append(item)
            print(f"{item} a été ajouté à la liste.\n---------------------------------")
        case "2":
            item = input("Quel article souhaitez-vous supprimer de la liste ? ")
            shopping_list.remove(item)
            print(f"{item} a été supprimé de la liste.\n---------------------------------")
        