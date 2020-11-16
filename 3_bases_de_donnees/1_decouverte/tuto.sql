-- suppression des tables si elles existent
DROP TABLE meteos;
DROP TABLE villes;

-- création des tables
CREATE TABLE meteos (
    ville    varchar(80),
    t_min    int,     -- température minimale en °C
    t_max    int,     -- température maximale
    prcp     real,    -- précipitation (entre 0 et 1)
    date     date
);
CREATE TABLE villes (
    nom      varchar(80),
    position point -- type particulier à postgresql
);

-- Données fantaisistes!

-- Pour la table meteos
INSERT INTO meteos VALUES ('Tours', 12, 23, 0.2, '2020-11-03');
INSERT INTO meteos VALUES ('Paris', 12, 17, 0.7, '2020-11-03');
INSERT INTO meteos VALUES ('Marseille', 17, 24, 0, '2020-11-03');
INSERT INTO meteos VALUES ('Tours', 17, 21, 0.1, '2020-11-04');
INSERT INTO meteos VALUES ('Paris', 11, 18, 0, '2020-11-04');
INSERT INTO meteos VALUES ('Marseille', 19, 26, 0, '2020-11-04');
INSERT INTO meteos VALUES ('Tours', 9, 16, 0, '2020-11-05');
INSERT INTO meteos VALUES ('Paris', 9, 13, 0, '2020-11-05');
INSERT INTO meteos VALUES ('Marseille', 14, 22, 1.2, '2020-11-05');
INSERT INTO meteos VALUES ('Tours', 5, 15, 0, '2020-11-06');
INSERT INTO meteos VALUES ('Paris', 15, 5, 0, '2020-11-06');
INSERT INTO meteos VALUES ('Marseille', 15, 25, 0.6, '2020-11-06');
INSERT INTO meteos VALUES ('Tours', -2, 7, 0, '2020-11-07');
INSERT INTO meteos VALUES ('Paris', 0, 8, 0.1, '2020-11-07');
INSERT INTO meteos VALUES ('Marseille', 19, 28, 2.1, '2020-11-07');
INSERT INTO meteos VALUES ('Tours', 6, 14, 0, '2020-11-08');
INSERT INTO meteos VALUES ('Paris', 2, 17, 0, '2020-11-08');
INSERT INTO meteos VALUES ('Marseille', 15, 19, 0, '2020-11-08');

-- Pour la table villes
INSERT INTO villes VALUES ('Paris', '(48.85341, 2.3488)');
INSERT INTO villes VALUES ('Marseille', '(43.29695, 5.38107)');
INSERT INTO villes VALUES ('Lyon', '(45.74846, 4.84671)');
INSERT INTO villes VALUES ('Tours', '(47.38333, 0.68333)');