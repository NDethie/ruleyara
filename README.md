# ruleyara
Prérequis pour  run  le projet


Installation Django sous Linux
$ sudo apt-get install python3-pip
$ sudo aptitude install python3-django

pip pour installer Django
$ pip install django

Créer l’environnement virtuel et y accéder
$ mkvirtualenv myvenv



commande pour accéder à l’environnement virtuel 
$ workon myvenv


Accéder au projet avec cette commande
$ git clone https://github.com/NDethie/ruleyara
$ cd ruleyara

Créer la base de donnée : créer puis appliquer les migrations
$ python manage.py makemigrations
$ python manage.py migrate

Démarrer le projet
$ python manage.py runserver



