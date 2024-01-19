class EmptyCell:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value is None:
            return "#"
        else:
            return str(self.value)

def CreateArray(n, name, nb_line):
    tableau = {name: []}  # Initialise la liste principale avec un nom donné
    for _ in range(n):
        nouvelle_liste = [EmptyCell() for _ in range(nb_line)]  # Crée une liste avec des objets EmptyCell
        tableau[name].append(nouvelle_liste)  # Ajoute la nouvelle liste à 'tableau'
    return tableau

def ad_cell(element, indice_liste, indice_objet, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if indice_objet < len(tableau[tableau_name][indice_liste]):
                tableau[tableau_name][indice_liste][indice_objet].value = element
                print(f"L'élément '{element}' a été ajouté à la case {indice_objet} de la liste {indice_liste} de '{tableau_name}'.")
            else:
                print(f"L'indice d'objet spécifié est hors de la plage de '{tableau_name}[{indice_liste}]'.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

def del_cell(indice_liste, indice_objet, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if indice_objet < len(tableau[tableau_name][indice_liste]):
                tableau[tableau_name][indice_liste][indice_objet].value = None
                print(f"La case {indice_objet} de la liste {indice_liste} de '{tableau_name}' a été vidée.")
            else:
                print(f"L'indice d'objet spécifié est hors de la plage de '{tableau_name}[{indice_liste}]'.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

def del_row(indice_liste, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            for cellule in tableau[tableau_name][indice_liste]:
                cellule.value = None
            print(f"La liste {indice_liste} de '{tableau_name}' a été vidée.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

def get_row(indice_liste, tableau_name, tableau, exclude_empty=False):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if exclude_empty:
                return [cellule.value for cellule in tableau[tableau_name][indice_liste] if cellule.value is not None]
            else:
                return [cellule.value for cellule in tableau[tableau_name][indice_liste]]
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
            return []
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")
        return []

def get_coll(tableau_name, n, tableau):
    if tableau_name in tableau:
        return [liste[n].value for liste in tableau[tableau_name] if n < len(liste)]
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")
        return []

def get_cells(tableau_name, indice_liste, indice_objet, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if indice_objet < len(tableau[tableau_name][indice_liste]):
                return tableau[tableau_name][indice_liste][indice_objet].value
            else:
                print(f"L'indice d'objet spécifié est hors de la plage de '{tableau_name}[{indice_liste}]'.")
                return None
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
            return None
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")
        return None

def del_coll(n, tableau_name, tableau):
    if tableau_name in tableau:
        for liste in tableau[tableau_name]:
            if n < len(liste):
                liste[n].value = None
            else:
                print(f"L'indice de colonne spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

def afficher_tableau(tableau):
    max_length = 0  # Longueur maximale des éléments dans le tableau
    for key, value in tableau.items():
        for liste in value:
            for cellule in liste:
                cellule_length = len(str(cellule))
                if cellule_length > max_length:
                    max_length = cellule_length

    for key, value in tableau.items():
        print(f"{key}:")
        for liste in value:
            for cellule in liste:
                cellule_str = str(cellule)
                espacement = " " * ((max_length - len(cellule_str)) // 2)
                print(f"{espacement}{cellule_str}{espacement}", end=" ")
            print()
        print()

# Exemple d'utilisation :
nom_tableau = input("Entrez un nom pour le tableau : ")
nombre_de_listes = int(input("Entrez le nombre de listes : "))
nombre_d_objets = int(input("Entrez le nombre d'objets à ajouter dans chaque liste : "))
resultat = CreateArray(nombre_de_listes, nom_tableau, nombre_d_objets)
print("Tableau initial:")
afficher_tableau(resultat)

element_a_ajouter = input("Entrez l'élément à ajouter : ")
indice_liste_a_modifier = int(input("Entrez l'indice de la liste où ajouter l'élément : "))
indice_objet_a_modifier = int(input("Entrez l'indice de l'objet où ajouter l'élément : "))

ad_cell(element_a_ajouter, indice_liste_a_modifier, indice_objet_a_modifier, nom_tableau, resultat)
print("\nTableau après ajout:")
afficher_tableau(resultat)


indice_liste_a_recuperer = int(input("Entrez l'indice de la liste à récupérer : "))
liste_recuperee = get_row(indice_liste_a_recuperer, nom_tableau, resultat)
print(f"\nListe récupérée de '{nom_tableau}[{indice_liste_a_recuperer}]':")
print(liste_recuperee)

indice_liste_a_recupererbis = int(input("Entrez l'indice de la liste à récupérer : "))
liste_recupereebis = get_row(indice_liste_a_recupererbis, nom_tableau, resultat,exclude_empty=True)
print(f"\nListe récupérée de '{nom_tableau}[{indice_liste_a_recupererbis}]':")
print(liste_recupereebis)

indice_liste_a_lire = int(input("Entrez l'indice de la liste à lire : "))
indice_objet_a_lire = int(input("Entrez l'indice de l'objet à lire : "))

valeur_lue = get_cells(nom_tableau, indice_liste_a_lire, indice_objet_a_lire, resultat)
print(valeur_lue)

coll_test1 = int(input("Entrez l'indice de la liste à lire : "))
coll_test = get_coll(nom_tableau,coll_test1, resultat)
print(coll_test)

indice_liste_a_vider = int(input("Entrez l'indice de la liste à vider : "))

del_row(indice_liste_a_vider, nom_tableau, resultat)
print("\nTableau après suppression de la liste spécifiée :")
afficher_tableau(resultat)
