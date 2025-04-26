# DarMarket - Site d'annonces immobilières

DarMarket est une plateforme d'annonces immobilières développée avec Django. Elle permet aux utilisateurs de publier et de consulter des annonces immobilières.

## Fonctionnalités

- Consultation des annonces immobilières
- Création d'annonces (utilisateurs connectés)
- Modification d'annonces (propriétaires)
- Filtrage par type de bien et type de transaction
- Interface d'administration
- Système de pagination

## Technologies utilisées

- Django 4.2.10
- Bootstrap 5
- Docker
- GitHub Actions (CI/CD)
- Railway (Déploiement)

## Installation locale

1. Cloner le dépôt :
```bash
git clone https://github.com/votre-username/darmarket.git
cd darmarket
```

2. Créer un environnement virtuel et l'activer :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Appliquer les migrations :
```bash
python manage.py migrate
```

5. Créer un superutilisateur :
```bash
python manage.py createsuperuser
```

6. Lancer le serveur de développement :
```bash
python manage.py runserver
```

## Déploiement avec Docker

1. Construire l'image :
```bash
docker-compose build
```

2. Lancer les conteneurs :
```bash
docker-compose up -d
```

## Déploiement sur Railway

Le déploiement sur Railway est automatisé via GitHub Actions. Pour déployer :

1. Configurer les secrets GitHub :
   - RAILWAY_TOKEN
   - RAILWAY_PROJECT_ID

2. Pousser les modifications sur la branche main :
```bash
git push origin main
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. 