DROP TABLE IF EXISTS membres;
DROP TABLE IF EXISTS articles;

CREATE TABLE membres ( -- user
  id    INTEGER         PRIMARY KEY AUTOINCREMENT,
  login VARCHAR(20)     UNIQUE NOT NULL,
  mdp   VARCHAR(100)    NOT NULL
);

CREATE TABLE articles ( -- post
  id        INTEGER     PRIMARY KEY AUTOINCREMENT,
  auteur_id INTEGER     NOT NULL REFERENCES membres (id),
  cree_le   TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  titre     VARCHAR(50) NOT NULL,
  contenu   TEXT        NOT NULL
);

-- et quelques données
INSERT INTO membres (login, mdp) VALUES ('alice', 'alice'), ('bob', 'bob');
INSERT INTO articles (auteur_id, titre, contenu)
VALUES ('1', 'Le lièvre et la tortue', 'Rien ne sert de courir, il faut partir à point.'),
       ('2', 'Maxime de La Rochefoucauld', 'Le soleil ni la mort ne se peuvent regarder en face.'),
       ('1', 'Le loup et l''agneau', 'La raison du plus fort est toujours la meilleure.'),
       ('2', 'Les Essais', 'Vivre c''est apprendre à mourir.');