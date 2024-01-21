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
        # Appliquer la fonction de hachage à l'élément (vous pouvez remplacer hash_function par votre propre fonction de hachage)
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

    def hash_function(self, element):
        # Exemple de fonction de hachage simple (vous pouvez la remplacer par une fonction plus complexe si nécessaire)
        return len(element)

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
elements_to_add = ["Hello", "World", "Python", "Hash", "Table", "Overflow"]
for element in elements_to_add:
    my_table.add_element(element)

# Affichage de la table de hachage avec les éléments ajoutés
my_table.display_table()
