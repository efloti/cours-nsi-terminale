CREATE TABLE infos (
    id serial PRIMARY KEY,
    nom varchar(100) NOT NULL,
    prenom varchar(100) NOT NULL,
    annee_naissance DATE NOT NULL,
    taille INT NOT NULL
);
INSERT INTO infos (nom, prenom, annee_naissance, taille) VALUES ('éric', 'Fuchmol', '2003', 177);
INSERT INTO infos (nom, prenom, annee_naissance, taille) VALUES ('alice', 'Ginger', '2000', 160);
INSERT INTO infos (nom, prenom, annee_naissance, taille) VALUES ('éloïse', 'Félicie', '2008', 153);
INSERT INTO infos (nom, prenom, annee_naissance, taille) VALUES ('tom', 'Bompard', '1995', 192);
