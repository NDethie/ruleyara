# Gérer les règles yara

PRerequis  pour run le  projet

Installation Django sous Linux

$sudo apt-get install python3-pip     

$sudo aptitude install python3-django   


pip pour installer Django

$pip install django

Créer l’environnement virtuel et y accéder

$mkvirtualenv myvenv    




Commande pour accéder à l’environnement virtuel 

$workon myvenv    




Accéder au projet avec cette commande

$git clone https://github.com/NDethie/ruleyara

$cd ruleyara    


Mettre en place la base de données : créer puis appliquer les migrations

$python manage.py makemigrations  

$python manage.py migrate   



Démarrer le projet

$pythron manage.py runserver    



Accéder à la page d’accueil


127.0.0.1:8000/yararule/
