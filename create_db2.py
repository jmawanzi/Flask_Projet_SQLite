import sqlite3

def create_database():
    # Connexion à la base de données (si la base de données n'existe pas, elle sera créée)
    conn = sqlite3.connect('bibliotheque.db')

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = conn.cursor()

cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(1, 'Emilie', 'Victor', 2024, 10))
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(2, 'Didier', 'Laurent', 2023, 5))
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(3, 'Georges', 'Hugo', 2020, 3))
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(2, 'Lars', 'Sullivan', 2021, 6))

    # Commit des changements et fermeture de la connexion
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
