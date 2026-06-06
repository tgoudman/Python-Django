# Commandes utiles

## Django

```bash
# Créer une app
python manage.py startapp nom_app

# Créer les migrations
python manage.py makemigrations
python manage.py makemigrations nom_app

# Appliquer les migrations
python manage.py migrate
python manage.py migrate nom_app

# Annuler les migrations d'une app
python manage.py migrate nom_app zero

# Charger des fixtures
python manage.py loaddata fichier.json

# Vider les tables
python manage.py flush

# Lancer le serveur
python manage.py runserver

# Collecter les fichiers statiques
python manage.py collectstatic
```

## PostgreSQL

```bash
# Se connecter à la base
psql -U tgoudman -d 42_bdd

# Afficher toutes les tables
psql -U tgoudman -d 42_bdd -c "\dt"

# Afficher les tables avec filtre
psql -U tgoudman -d 42_bdd -c "\dt ex10*"

# Compter les lignes d'une table
psql -U tgoudman -d 42_bdd -c "SELECT COUNT(*) FROM nom_table;"

# Afficher le contenu d'une table
psql -U tgoudman -d 42_bdd -c "SELECT * FROM nom_table;"

# Supprimer une table
psql -U tgoudman -d 42_bdd -c "DROP TABLE nom_table;"

# Vider une table
psql -U tgoudman -d 42_bdd -c "TRUNCATE TABLE nom_table CASCADE;"

# Afficher les migrations Django
psql -U tgoudman -d 42_bdd -c "SELECT * FROM django_migrations WHERE app='nom_app';"

# Supprimer les migrations d'une app
psql -U tgoudman -d 42_bdd -c "DELETE FROM django_migrations WHERE app='nom_app';"
```

## Environnement virtuel

```bash
# Activer l'environnement virtuel
source ../day04/ex00/envDay04/bin/activate

# Désactiver
deactivate

# Installer un package
pip install nom_package
```

## Fichiers statiques

```bash
# Créer le dossier static
mkdir -p static/css
touch static/css/style.css
```