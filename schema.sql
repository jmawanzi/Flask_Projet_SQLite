-- Création de la table des Livres
CREATE TABLE Livres (
    livre_id INT PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(255) NOT NULL,
    auteur_id INT,
    genre_id INT,
    stock INT,
    FOREIGN KEY (auteur_id) REFERENCES Auteurs(auteur_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);

-- Création de la table des Utilisateurs
CREATE TABLE Utilisateurs (
    utilisateur_id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role ENUM('lecteur', 'bibliothecaire', 'administrateur') NOT NULL
);

-- Création de la table des Emprunts
CREATE TABLE Emprunts (
    emprunt_id INT PRIMARY KEY AUTO_INCREMENT,
    utilisateur_id INT,
    livre_id INT,
    date_emprunt DATE,
    date_retour_prevue DATE,
    date_retour_effective DATE,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs(utilisateur_id),
    FOREIGN KEY (livre_id) REFERENCES Livres(livre_id)
);

-- Création de la table des Auteurs
CREATE TABLE Auteurs (
    auteur_id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100)
);

-- Création de la table des Genres
CREATE TABLE Genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL
);

-- Exemple d'insertion de données
INSERT INTO Auteurs (nom, prenom) VALUES ('Rowling', 'J.K.');
INSERT INTO Genres (nom) VALUES ('Fantasy');
