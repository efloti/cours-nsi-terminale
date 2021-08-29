CREATE TABLE membres (
--  nom col        type
    mbr_id         integer
    prenom         varchar(40), 
    nom            varchar(40), 
    adresse        varchar(100), 
    code_postal    char(5),
    telephone      char(10), 
    recommande_par integer,
    date_entree    date
);

CREATE TABLE activites (
    act_id                   integer, 
    nom                      varchar(30), 
    prix_membre              numeric, 
    prix_invite              numeric,
    cout_initial             numeric,
    cout_maintenance_mensuel numeric
);

-- une erreur...
CREATE TABLE reservations (
    reserv_id     integer,
    act_id        integer,
    mbr_id        integer,
    heure_debut   timestamp,
    nb_demi_heure integer,
);