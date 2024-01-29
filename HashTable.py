class HashTable:
    def __init__(self, table_name, num_columns, num_places_per_column):
        self.table_name = table_name
        self.num_columns = num_columns
        self.num_places_per_column = num_places_per_column
        self.hash_table = {}

    def create_table(self):
        for column in range(self.num_columns):
            column_name = f"Column_{column + 1}"
            self.hash_table[column_name] = [column + 1] + [None] * (self.num_places_per_column - 1)

    def add_element(self, element):
        # Appliquer la fonction de hachage à l'élément
        hashed_value = self.hash_function(element)

        # Trouver la colonne correspondante dans la table
        column_index = hashed_value % self.num_columns
        column_name = f"Column_{column_index + 1}"  # Ajouter 1 pour ajuster l'index de colonne

        # Trouver la première case inoccupée dans la colonne
        places = self.hash_table[column_name]
        for i in range(1, len(places)):
            if places[i] is None:
                # Place inoccupée trouvée, placer l'élément
                places[i] = element
                return

        # Si toutes les places sont occupées, ne rien faire ou gérer le cas selon vos besoins

    def get_column_content(self, column_name):
        # Récupérer le contenu de la colonne spécifiée
        return self.hash_table.get(column_name, [])

    def hash_function(self, element):
        # Utiliser la fonction de hachage standard de Python
        return hash(element)

    def display_table(self):
        print(f"Hash Table: {self.table_name}")
        for column, places in self.hash_table.items():
            print(f"{column}: {places}")

# Exemple d'utilisation
table_name = "MaTable"
num_columns = 100
num_places_per_column = 2

# Création de la table de hachage avec les numéros de colonne
my_table = HashTable(table_name, num_columns, num_places_per_column)
my_table.create_table()

# Ajout d'éléments à la table de hachage
elements_to_add = [
    "python", "programmation", "intelligence", "artificielle", "apprentissage",
    "algorithmes", "développement", "données", "modélisation", "analyse",
    "scientifique", "machine", "réseaux", "neuronaux", "codage", "projet",
    "open-source", "innovation", "technologie", "informatique", "syntaxe",
    "bibliothèques", "framework", "programmeur", "web", "serveur", "clients",
    "interface", "utilisateur", "base de données", "sécurité", "cryptographie",
    "système", "exploitation", "cloud", "computing", "devops", "agile",
    "méthodologie", "déploiement", "API", "gestion", "versions", "collaboration",
    "repository", "documentation", "test", "validation", "intégration",
    "débogage", "optimisation", "performances", "frontend", "backend",
    "responsive", "design", "agilité", "scrum", "kanban", "workflow",
    "productivité", "efficacité", "qualité", "maintenance", "support",
    "communauté", "contributions", "opensource", "communication", "réunion",
    "équipe", "compétences", "expertise", "domaine", "fonctionnalités",
    "solutions", "conception", "architecture", "ingénierie", "logiciel"
]
for element in elements_to_add:
    my_table.add_element(element)

# Affichage de la table de hachage avec les éléments ajoutés
my_table.display_table()

# Récupération du contenu d'une colonne spécifique
column_name_to_get = "Column_1"
column_content = my_table.get_column_content(column_name_to_get)
print(f"Contenu de la colonne {column_name_to_get}: {column_content}")
