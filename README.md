# Projet IA : Entraînement, Validation, Déploiement et Automatisation

Ce projet a pour objectif de développer un modèle d'intelligence artificielle (IA) et de mettre en place un workflow CI/CD complet en utilisant Git, GitHub Actions et Git LFS. Le projet inclut les étapes suivantes :

- **Entraînement** du modèle via `script/train.py`
- **Validation** des performances via `script/validate.py`
- **Déploiement** du modèle via `script/deploy.py`
- **Automatisation de l'envoi d'email** contenant le modèle et la documentation via `script/send_email.py`
- **Exploration interactive** et analyses via `notebook/exploration.ipynb` (ou `exploration.py`)

## Structure du Projet

mon-projet-ia/
│
├── .github/
│    └── workflows/
│         └── ci-cd.yml         # Workflow GitHub Actions
│
├── script/                     # Scripts Python (entraînement, validation, déploiement, envoi d'e-mail, etc.)
│     ├── train.py
│     ├── validate.py
│     ├── deploy.py
│     └── send_email.py
│
├── notebook/                   # Jupyter Notebooks (analyses exploratoires, explications)
│     └── exploration.ipynb
│
├── model/                      # Modèles d'IA entraînés
│     └── model.h5             # Exemple de modèle
│
├── data/                       # Données du projet (gérées avec Git LFS)
│     └── dataset.csv          # Exemple de dataset (fichier de plus de 10 Mo)
│
├── doc/                        # Documentation générée (sera ignoré par git)
│     └── index.html
│
├── keys/                       # Secrets ou configurations (sécurisés via Git Secrets)
│     └── config.json
│
└── .gitignore                  # Fichier pour ignorer doc/ et keys/



## Prérequis

- **Python 3.8+**
- **pip** (gestionnaire de packages Python)
- **Git** et **Git LFS** pour la gestion des fichiers volumineux (ex. `dataset.csv`)
- **Jupyter Notebook** ou **JupyterLab** pour ouvrir et exécuter les notebooks

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/votre-utilisateur/mon-projet-ia.git
   cd mon-projet-ia

2. **Configurer Git LFS pour les fichiers volumineux :**
git lfs install
git lfs track "*.csv"
git add .gitattributes

3. **Installer les dépendances :**
pip install numpy matplotlib seaborn scikit-learn joblib


# Configuration
## Secrets et configurations :
Le fichier keys/config.json contient les paramètres SMTP (serveur, port, identifiants) pour l'envoi d'email. Ce fichier doit être protégé et est exclu du suivi Git grâce à .gitignore.
Pour les workflows GitHub Actions, stockez les informations sensibles (par exemple SMTP_USERNAME et SMTP_PASSWORD) dans GitHub Secrets.
Utilisation
Entraînement du Modèle
Exécutez le script d'entraînement :

- bash
- Copier
- Modifier
  ### python script/train.py
Ce script charge (ou génère) les données, entraîne un modèle de régression logistique et sauvegarde le modèle dans le dossier model.

### Validation du Modèle
Pour évaluer le modèle entraîné :

- bash
- Copier
- Modifier
- python script/validate.py
  
Ce script charge le modèle sauvegardé, effectue des prédictions sur un jeu de données de validation et affiche des métriques telles que la précision et le rapport de classification.

### Déploiement du Modèle
Pour simuler le déploiement du modèle :

- bash
- Copier
- Modifier
- python script/deploy.py
Ce script copie le modèle entraîné vers un emplacement de déploiement (exemple : model/deployed_model.pkl).

### Envoi par Email
Pour envoyer par email un fichier ZIP contenant le modèle et la documentation :

- bash
- Copier
- Modifier
- python script/send_email.py output.zip
- Assurez-vous que le fichier ZIP (contenant le modèle et la documentation) a été généré au préalable.

## Exploration Interactive
Ouvrez le notebook dans Jupyter Notebook ou JupyterLab :

- bash
- Copier
- Modifier
- jupyter notebook notebook/exploration.ipynb
Ce notebook vous permet d'explorer les données, d'entraîner le modèle et de visualiser les résultats.

# Workflow CI/CD
Le fichier .github/workflows/ci-cd.yml définit un workflow GitHub Actions qui s'exécute à chaque push sur la branche main. Ce workflow :

- **Installe les dépendances.**
- **Exécute les scripts d'entraînement, de validation et de déploiement.**
- **Génère la documentation via pydoc.**\
  
## Crée un fichier ZIP contenant le modèle et la documentation.
Envoie automatiquement un email aux membres du projet avec ce fichier ZIP en pièce jointe.
Contribution
- Branches :
- Chaque membre du projet doit travailler dans sa branche personnelle et effectuer des commits significatifs.
- Pull Requests :
- Les modifications doivent être fusionnées dans la branche main via des pull requests, revues par au moins un autre membre du projet.



# Remerciements
Merci à tous les membres de l'équipe notamment NTONGA BABONG, ISSA BACHIR, SIMO CURTIS pour leur contribution et aux outils tels que GitHub Actions pour faciliter l'automatisation du workflow.
