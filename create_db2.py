import sqlite3

def create_database():
    # Connexion à la base de données (si la base de données n'existe pas, elle sera créée)
    conn = sqlite3.connect('bibliotheque.db')

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = conn.cursor()

    # Création de la table des Livres
    cursor.execute('''CREATE TABLE IF NOT EXISTS Livres (
                       livre_id INTEGER PRIMARY KEY,
                       titre TEXT NOT NULL,
                       auteur TEXT,
                       genre TEXT,
                       stock INTEGER
                       )''')

    # Création de la table des Utilisateurs
    cursor.execute('''CREATE TABLE IF NOT EXISTS Utilisateurs (
                       utilisateur_id INTEGER PRIMARY KEY,
                       nom TEXT NOT NULL,
                       prenom TEXT NOT NULL,
                       email TEXT UNIQUE NOT NULL,
                       role TEXT NOT NULL
                       )''')

    # Création de la table des Emprunts
    cursor.execute('''CREATE TABLE IF NOT EXISTS Emprunts (
                       emprunt_id INTEGER PRIMARY KEY,
                       utilisateur_id INTEGER,
                       livre_id INTEGER,
                       date_emprunt DATE,
                       date_retour_prevue DATE,
                       date_retour_effective DATE,
                       FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs(utilisateur_id),
                       FOREIGN KEY (livre_id) REFERENCES Livres(livre_id)
                       )''')

    # Commit des changements et fermeture de la connexion
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
