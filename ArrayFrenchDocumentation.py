class EmptyCell:
    def __init__(self, value=None):
        """Initialise une cellule vide avec une valeur optionnelle."""
    
    def __str__(self):
        """Retourne la représentation en chaîne de la cellule."""

def CreateArray(n, name, nb_line):
    """Crée un tableau de données.

    Args:
        n (int): Nombre de listes à créer.
        name (str): Nom du tableau.
        nb_line (int): Nombre d'objets à ajouter dans chaque liste.

    Returns:
        dict: Tableau de données créé.
    """

def ajout(element, indice_liste, indice_objet, tableau_name, tableau):
    """Ajoute un élément à une position spécifique dans le tableau.

    Args:
        element: Élément à ajouter.
        indice_liste (int): Indice de la liste où ajouter l'élément.
        indice_objet (int): Indice de l'objet où ajouter l'élément.
        tableau_name (str): Nom du tableau.
        tableau (dict): Tableau de données.

    Returns:
        None
    """

def del_cells(indice_liste, indice_objet, tableau_name, tableau):
    """Vide le contenu d'une cellule spécifique dans le tableau.

    Args:
        indice_liste (int): Indice de la liste où se trouve la cellule à vider.
        indice_objet (int): Indice de la cellule à vider dans la liste.
        tableau_name (str): Nom du tableau.
        tableau (dict): Tableau de données.

    Returns:
        None
    """

def del_row(indice_liste, tableau_name, tableau):
    """Vide tous les éléments d'une liste spécifique dans le tableau.

    Args:
        indice_liste (int): Indice de la liste à vider.
        tableau_name (str): Nom du tableau.
        tableau (dict): Tableau de données.

    Returns:
        None
    """

def get_row(indice_liste, tableau_name, tableau, exclude_empty=False):
    """Récupère les éléments d'une liste spécifique du tableau.

    Args:
        indice_liste (int): Indice de la liste à récupérer.
        tableau_name (str): Nom du tableau.
        tableau (dict): Tableau de données.
        exclude_empty (bool, optional): Exclut les cases vides si True. Par défaut, False.

    Returns:
        list: Liste des éléments de la liste spécifiée.
    """

def get_coll(tableau_name, n, tableau):
    """Récupère les éléments à une position spécifique dans chaque liste du tableau.

    Args:
        tableau_name (str): Nom du tableau.
        n (int): Position des éléments à récupérer dans chaque liste.
        tableau (dict): Tableau de données.

    Returns:
        list: Liste des éléments à la position spécifiée dans chaque liste.
    """

def get_cells(tableau_name, indice_liste, indice_objet, tableau):
    """Récupère le contenu d'une cellule spécifique du tableau.

    Args:
        tableau_name (str): Nom du tableau.
        indice_liste (int): Indice de la liste où se trouve la cellule.
        indice_objet (int): Indice de la cellule dans la liste.
        tableau (dict): Tableau de données.

    Returns:
        Any: Contenu de la cellule spécifiée.
    """

def afficher_tableau(tableau):
    """Affiche le tableau avec un espacement égal pour tous les éléments.

    Args:
        tableau (dict): Le tableau à afficher.

    Returns:
        None
    """
