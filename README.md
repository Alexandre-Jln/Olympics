 # Olympics

Ce projet est un exemple d’application Python permettant de voir diverses
informations sur les Jeux Olympiques de Paris 2024.

Certaines données de la base de données viennent du dépôt
https://github.com/22Ranjan15/Paris-2024-Olympic_Dashboard

Il comprend 4 manières d’accéder aux données :

- une interface web dans `olympics/api.py`.
- une interface en ligne de commande dans `olympics/__main__.py`,
- une bibliothèque pour afficher des résultats dans le terminal dans `olympics/cli.py`,
- une bibliothèque bas-niveau pour accéder à la base de données dans `olympics/db.py`,

Cette application est écrite à des fins éducatives, et ne suit pas toutes les
bonnes pratiques du développement d’applications en Python.

**Au-delà de Python, le but de cette évaluation est de vous familiariser avec
les multiples facettes du développement : lecture et compréhension de code,
découverte d’outils, lecture de documentation, qualité logicielle,
architecture, intégration continue…**

Le sujet d’évaluation, comprenant des opérations à réaliser et des questions,
est inclus en bas de ce document.

Si vous avez des réponses à donner ou des remarques à faire, une section est
dédiée à cela en bas de ce document : écrivez ce que vous souhaitez, commitez
et pushez ce document README.md. **N’écrivez pas de texte ailleurs que dans
cette section !**

Les devoirs dont le contenu est trop proche, dont l’historique Git est douteux,
ou dont le code est si stupide qu’il ne peut pas avoir été écrit par vous,
seront sanctionnés d’un D ou d’un E.


## Comment l’installer

1. [Importez](https://github.com/new/import) le dépôt en privé.

2. Partagez votre dépôt en lecture avec moi.

   Sur la page de votre fork GitHub, dans l’onglet « Settings », la section
   « Collaborators and teams », vous avez un bouton « Add people ». Ajoutez
   l’utilisateur « liZe » (Guillaume Ayoub).

3. Clonez votre fork.

   `git clone git@github.com:YourNickName/olympics.git`

4. Allez dans votre dépôt cloné.

   `cd olympics`

5. Créez un environnement virtuel appelé `venv`.

   `python -m venv venv`

6. Activez votre environnement virtuel.

7. Installez les dépendances du projet.

   `pip install -e .`


## Comment l’utiliser

Pour utiliser l’application ou lancer les tests, veillez bien à être à la
racine du dépôt que vous avez cloné et à activer l’environnement virtuel.

### Pour utiliser l’API web

`fastapi dev olympics`

Vous avez alors accès à l’adresse `http://127.0.0.1:8000` et aux différentes
routes de l’application.

Une documentation automatique, avec une interface de test, est disponible à
l’adresse `http://127.0.0.1:8000/docs`.

Vous pouvez arrêter le serveur avec `Ctrl+C`.

### Pour utiliser la CLI

`python -m olympics --help`

Différentes commandes s’offrent à vous. Pour afficher le top 5 des médailles
individuelles, vous pouvez par exemple lancer :

`python -m olympics individual --top=5`

### Pour utiliser la bibliothèque

`python`

Dans l’interpréteur Python :

```python
>>> from olympics import cli
>>> help(cli)
```

Différentes fonctions sont disponibles. Pour afficher le top 3 des pays pour
les médailles collectives, vous pouvez par exemple lancer :

```python
>>> cli.top_collective(top=3)
```

Pour quitter l’interpréteur, utilisez `exit()`.

### Pour utiliser les fonctions bas-niveau de la base de données

`python`

Dans l’interpréteur Python :

```python
>>> from olympics import db
>>> help(db)
```

Différentes fonctions sont possibles. Pour récupérer une liste de tous les
athlètes et afficher les informations du premier, vous pouvez par exemple
lancer :

```python
>>> athletes = db.get_athletes()
>>> dict(athletes[0])
{'id': 1, 'name': 'Artur ALEKSANYAN', 'gender': 'male', 'country_id': 8}
```

Vous pouvez également lancer des requêtes SQL de cette manière :

```python
>>> cursor = db.get_connection().cursor()
>>> athletes = cursor.execute('SELECT id, name FROM athlete LIMIT 5').fetchall()
>>> dict(athletes[0])
{'id': 1, 'name': 'Artur ALEKSANYAN'}
```

Le schéma de la base de données est dans `database/model.sql`.

Pour quitter l’interpréteur, utilisez `exit()`.

### Pour lancer les tests

Quelques tests basiques sont disponibles dans le dossier `tests`.

Pour lancer les tests, lancez `python -m pytest`


## Sujet

Le but de cette évaluation est d’améliorer cette application.

**Vérifiez d’avoir bien tout commité et pushé à la fin de votre travail, en
vérifiant les fichiers sur GitHub.**

**Faites des commits atomiques, avec des messages lisibles.**

**Si vous n’arrivez pas à faire une question, ne perdez pas trop de temps,
passez à la suivante.**

Les deux premières étapes sont obligatoires. Vous validerez le module si vous
réalisez ces deux étapes parfaitement.

Les autres étapes sont optionnelles. Vous pouvez en faire une ou plusieurs,
dans l’ordre que vous souhaitez. Si vous les réalisez avec succès, vous pourrez
améliorer le résultat de votre évaluation, pour assurer la validation ou aller
chercher le A (si vous écrivez du code vraiment très, très intelligent).

Vous pouvez également proposer vos propres améliorations, en restant dans les
thématiques abordées en cours. Il est sans doute plus sûr de valider vos idées
avec moi avant de coder.

Dans tous les cas, privilégiez l’intelligence à la quantité. Utilisez ce que
vous avez vu en cours, et la documentation des outils vus en cours.

**N’écrivez que du code que vous comprenez.** Commentez votre code, en
particulier lorsqu’il est compliqué ou que vous avez des doutes. Je suis
réellement sévère sur ce point.

Ne me faites pas installer d’autres outils que les dépendances actuelles du
projet ou les bibliothèques que je vous demande d’installer pour cette
évaluation.

### Ajoutez une fonctionnalité (obligatoire)

Le but de cette nouvelle fonctionnalité est d’afficher le top des meilleurs
pays pour une discipline donnée en entrée. Pour cela, vous vous inspirerez du
code pour le top des pays, des athlètes par discipline et des listes de
médailles.

Écrivez d’abord la fonction nécessaire dans `db.py`. Répétez les opérations
dans `api.py`, `cli.py`, `__main__.py`.

Ajoutez cette fonctionnalité en suivant la méthode TDD (Test Driven
Development). À chaque fois, écrivez un test qui ne passe pas, commitez-le,
puis ajoutez le code nécessaire pour faire passer ce test dans un autre commit.

### Ajoutez une interface web (obligatoire)

En utilisant Flask, ajoutez une interface web visant à afficher les mêmes
informations que l’interface en ligne de commande.

Créez un dossier `web` dans lequel vous mettrez un fichier `__init__.py` qui
contiendra l’ensemble de votre code. D’autres fichiers (en particulier un
dossier `templates`) pourront compléter votre application web.

**Ce n’est pas un cours de HTML, de CSS ou de JavaScript.** Ne perdez pas de
temps à faire une interface visuellement jolie, mais construisez vos routes
avec soin. Vous ferez le reste sur votre temps libre, après le rendu !

### Améliorez les tests l’application (facultatif)

Ajoutez des tests pour votre interface web. La documentation de Flask donne des
indications sur la manière dont les tests peuvent être ajoutés, n’hésitez pas à
vous en inspirer.

Les fonctions des modules Python sont faites pour être utilisées avec les bons
types de paramètres, et ne gèrent volontairement pas les appels avec des types
différents : ce ne sont donc pas des bugs. Par contre, les API web et en ligne
de commande doivent rejeter proprement les types inattendus : si l’application
lève une exception, on peut considérer cela comme un bug.

### Utilisez un ORM (facultatif)

Utilisez [SQLAlchemy](https://www.sqlalchemy.org/) à la place du module
`sqlite3`. Inspirez-vous des bonnes pratiques données dans les documentations
de FastAPI et de SQLAlchemy à ce sujet.

### Refactorisez le code de `db.py` (facultatif)

Avec ou sans SQLAlchemy, il est possible d’éviter les nombreuses répétitions de
code dans le fichiers `db.py`. Ne serait-ce pas l’occasion d’utiliser des
décorateurs pour rendre cela moins verbeux et plus élégant ?

### Générez une documentation simple (facultatif)

En utilisant [Sphinx](https://www.sphinx-doc.org/), générez une documentation
simple. Pas la peine d’écrire des pavés de texte, une petite introduction et
une documentation automatique de l’API Python sont largement suffisantes.

Profitez-en pour mettre votre site en ligne avec GitHub Pages !


# Réponses et remarques

## Nouvelle fonctionnalité : Top des pays par discipline

Cette mise à jour ajoute une fonctionnalité qui affiche le **classement des pays pour une discipline donnée**, en prenant en compte toutes les médailles des épreuves associées (individuelles et collectives).

### Objectif

  * Fournir une vue dédiée aux performances par discipline.
  * Étendre l’architecture existante sans la casser, en réutilisant les mêmes patterns (`db → api → cli → __main__`).
  * Garder le code simple et lisible, en restant proche de ce qui est déjà fait dans le projet.

### Implémentation

La fonctionnalité a été intégrée dans les différents modules du projet.

### db.py

**Ajout de la fonction :** `get_top_countries_by_discipline(discipline_id, top)`

Cette fonction :

  * joint les tables `medal`, `event`, `discipline`, `athlete`, `team`, `country` ;
  * utilise `event.discipline_id` pour filtrer sur la discipline demandée ;
  * récupère le pays depuis l’athlète ou l’équipe via : `COALESCE(athlete.country_id, team.country_id)` ;
  * compte le nombre total de médailles par pays ;
  * trie les pays par nombre de médailles décroissant ;
  * limite le résultat au nombre demandé (top).

**Pourquoi comme ça ?**

Parce que le schéma de la base **ne stocke pas** `country_id` directement dans `medal`. J'ai donc reconstruire l’information via `athlete` ou `team`, d’où l’utilisation de `COALESCE`.

Le style de la requête est aligné avec les fonctions existantes (`get_top_countries`, `get_top_collective`, `get_top_individual`).

### api.py

**Ajout d’un endpoint FastAPI :**  
`GET /top-by-discipline/?discipline_id=<id>&top=<n>`

Ce endpoint :

  * appelle `get_top_countries_by_discipline` ;
  * renvoie les données au format JSON ;
  * suit le même modèle que les autres routes déjà présentes (routes de type `/top-*`).

**Pourquoi comme ça ?**

Pour rester **cohérent avec l’API existante** : chaque fonctionnalité SQL a un équivalent dans `api.py`, ce qui garde une structure claire et prévisible.

### cli.py

**Ajout d’une commande interne :**  
`top_countries_by_discipline(discipline_id, top, file=None)`

Cette commande :

  * utilise `db.get_top_countries_by_discipline` ;
  * affiche le résultat dans un tableau formaté;
  * est construite sur le même modèle que `top_countries`, `top_collective` et `top_individual`.

**Pourquoi comme ça ?**

Pour offrir la même expérience en ligne de commande que les autres classements :  
un **tableau lisible**, même style et mêmes conventions.

### __main__.py

**Ajout d’une nouvelle commande publique :**  
`python -m olympics discipline --discipline-id <id> --top <n>`

Modifications :

  * ajout de `discipline` dans la liste des commandes possibles ;
  * ajout de l’option `--discipline-id` ;
  * ajout d’un cas dans le `match` pour appeler `cli.top_countries_by_discipline`.

**Pourquoi comme ça ?**

Pour que la nouvelle fonctionnalité soit accessible de la **même manière** que les autres (`countries`, `collective`, `individual`), sans changer la logique de base du lanceur.

### Tests

J'ai ajoutés des tests pour chaque couche, en suivant le style des fichiers de tests existants :

  * `test_db.py` : vérifie que `get_top_countries_by_discipline` renvoie au plus `top` pays.
  * `test_api.py` : teste le nouvel endpoint `/top-by-discipline/` (code 200, taille du résultat).
  * `test_cli.py` : capture la sortie de `top_countries_by_discipline` et vérifie que le tableau est bien généré.
  * `test_main.py` : vérifie que la commande `discipline` s’exécute sans erreur via `main(argv)`.

**Pourquoi comme ça ?**

Les tests restent **simples et concis**, mais ils couvrent chaque niveau (DB, API, CLI, point d’entrée) comme dans le projet d’origine, tout en respectant la contrainte de ne pas alourdir inutilement la base de tests.

### Résumé des choix

  * **Respect de l’architecture existante** : une nouvelle fonctionnalité, mais intégrée dans tous les niveaux déjà prévus (`db`, `api`, `cli`, `__main__`).
  * **Adaptation au schéma SQL réel** : reconstruction correcte du pays via `athlete` ou `team`.
  * **Lisibilité** : code proche des fonctions déjà présentes, pour rester facile à lire et à maintenir.
  * **Testabilité** : chaque couche est testée, comme le reste du projet.

### Imprévu

Pas de problème particulier, ajout de la fonctionnalité et des tests qui se sont bien déroulés dans l'ensemble.

---

## Interface web (Flask)

Une interface web simple, développée avec **Flask**, a été ajoutée afin d’afficher les mêmes informations que l’interface en ligne de commande.

Conformément aux instructions du sujet, l’objectif est uniquement **fonctionnel** : l’interface **n’a pas vocation à être visuellement travaillée**.

### Structure

L’interface web se trouve dans le dossier :

  olympics/web/

Elle contient :

  * `__init__.py` : code principal de l’application Flask
  * `__main__.py` : permet l’exécution via `python -m olympics.web`
  * `templates/top_discipline.html` : template HTML minimal affichant un tableau

### Lancer l’interface web

Pour démarrer l’application :

<code>
python -m olympics.web
</code>

L’application sera disponible à l’adresse suivante :

<code>
http://127.0.0.1:5000
</code>

## Routes disponibles

### Page d’accueil

<code>
GET /
</code>

Affiche une page simple expliquant comment utiliser l’interface.

### Top des pays pour une discipline

<code>
GET /discipline/&lt;discipline_id&gt;?top=N
</code>

Exemple :

<code>
http://127.0.0.1:5000/discipline/3?top=5
</code>

Cette route :

  * utilise `db.get_top_countries_by_discipline` ;
  * affiche les résultats dans un **tableau HTML** ;
  * accepte un paramètre `top` optionnel (**5 par défaut**).

### Pourquoi cette approche ?

  * Respect total de la structure en couches déjà présente dans le projet (`db → cli → api → main → web`).
  * Code volontairement **minimal**, comme demandé dans l’énoncé.
  * Utilisation de Flask **sans ajout de CSS/JS**, conformément aux consignes.
  * **Séparation propre** entre logique Python et templates HTML.

### Imprévu

Utilisation de Flask assez simple à prendre en main, construction d'une seule route faite sciemment pour éviter de trop mettre de code et de HTML.

----

# Amélioration des tests (facultatif)

En complément des tests fournis avec le projet, une série de **nouveaux tests** a été ajoutée afin de renforcer la **qualité logicielle** et de couvrir **toutes les couches de l’application**, conformément aux recommandations du sujet.

Ces tests permettent également de vérifier que l’application réagit correctement aux **entrées invalides**, notamment pour :

  * l’API web (FastAPI),
  * l’interface Flask,
  * la ligne de commande (CLI).

## Tests de l’interface web (Flask)

Un fichier `tests/test_web.py` a été ajouté.  
Il teste les éléments suivants :

  * la page d’accueil (`/`) ;
  * la route affichant le top des pays pour une discipline (`/discipline/<id>?top=N`) ;
  * la gestion des entrées invalides (ex. `/discipline/abc` → 404).

L’application Flask est testée via son mode test intégré que j'ai vu dans la doc :

<code python>
from olympics.web import app

client = app.test_client()
response = client.get("/")
assert response.status_code == 200
</code>

Ces tests garantissent que l’**interface web fonctionne correctement** et **ne lève pas d’exceptions**.

## Tests de validation des paramètres (API FastAPI)

Les API doivent **rejeter proprement les types inattendus**.

Un test a été ajouté pour s'assurer que **FastAPI renvoie bien une erreur 422** (`Unprocessable Entity`) lorsqu’un paramètre incorrect est transmis :

<code python>
response = client.get("/top-by-discipline/?discipline_id=abc&top=5")
assert response.status_code == 422
</code>

Ce comportement valide la **robustesse du typage automatique** assuré par FastAPI.

## Tests de validation des paramètres (CLI)

La ligne de commande doit également gérer proprement les **erreurs de typage utilisateur**.

Un test a été ajouté pour vérifier qu’un argument invalide pour `--discipline-id` déclenche bien une **erreur `SystemExit`** (levée par `argparse`) :

<code python>
with pytest.raises(SystemExit):
    main(["discipline", "--discipline-id", "abc"])
</code>

Cela évite un **crash Python non contrôlé** et confirme que l’application gère correctement les entrées non valides.
 
## Résultat global

La suite de tests couvre désormais :

  * l’accès bas-niveau à la **base de données** ;
  * les **API FastAPI** ;
  * la **ligne de commande** (CLI) ;
  * l’**interface web Flask** ;
  * la **gestion des erreurs et des types inattendus**.

Grâce à ces ajouts, l’application atteint une **couverture fonctionnelle solide**,  
et se comporte correctement même en présence d’**entrées non valides**.

### Imprévu

Pas d'imprévu à communiquer.

---

# Utilisation de SQLAlchemy (facultatif)

Une version expérimentale de la fonctionnalité **Top des pays par discipline** que j'ai implémentée en utilisant **SQLAlchemy**.  
L’objectif est de montrer comment **remplacer progressivement les requêtes SQL brutes par un ORM moderne** et plus structuré.

## Objectif

  * Introduire SQLAlchemy dans le projet **sans casser l’architecture existante**.
  * Proposer une **version ORM** de la fonctionnalité déjà développée.

Cette partie est **indépendante** du code initial et **ne modifie pas** les fonctions existantes.

## Architecture ORM ajoutée

J'ai ajouté un nouveau fichier :

<code>
olympics/database.py
</code>

Il contient :

  * la configuration SQLAlchemy (`engine`, `SessionLocal`) ;
  * la base déclarative (`Base`) ;
  * les modèles ORM correspondant aux tables SQLite :
    - `Country`
    - `Athlete`
    - `Team`
    - `Discipline`
    - `Event`
    - `Medal`

Ces modèles **reflètent fidèlement le schéma** existant dans `database/olympics.db`.

Un second fichier regroupe la logique métier ORM :

<code>
olympics/db_orm.py
</code>

Il implémente une version ORM de la fonctionnalité principale :

<code python>
get_top_countries_by_discipline_orm(discipline_id, top)
</code>

Cette fonction utilise :

  * `func.count` pour compter les médailles ;
  * `func.coalesce` pour récupérer `country_id` depuis `Athlete` ou `Team` ;
  * des jointures ORM (`join`, `outerjoin`) ;
  * un `group_by` et un `order_by`.

## Intégration avec FastAPI

Une route API dédiée a été ajoutée :

<code>
GET /orm/top-by-discipline/?discipline_id=<id>&top=<n>
</code>

Elle utilise la **version ORM** et renvoie un JSON formaté comme ceci :

<code json>
[
  {"country": "France", "medals": 10},
  {"country": "Japan", "medals": 8}
]
</code>

Un traitement supplémentaire convertit les objets SQLAlchemy en **dictionnaires Python**,  
afin d’éviter les erreurs d’encodage JSON.

## Résultat

La version ORM offre :

  * une alternative **moderne et maintenable** aux requêtes SQL brutes ;
  * une meilleure **abstraction de la base de données** ;
  * un code plus **lisible** pour les futures évolutions ;
  * une **intégration simple** avec FastAPI.

### Imprévu

J'ai eu un imprévu et (ou) j'ai dû faire un traitement supplémentaire. En fait, SQLAlchemy m'a renvoyé des objets qui ne pouvaient pas être encodés directement en JSON par FastAPI. Du coup, sans cette conversion que j'ai ajoutée, cela provoquait une erreur 500. Les résultats ORM ont donc été transformés en dictionnaires Python afin de garantir une réponse JSON valide et compatible avec l’API.
