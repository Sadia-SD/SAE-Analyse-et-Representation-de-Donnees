# Acquisition Automatique de Données 3GPP

## Description du Projet
Ce projet vise à automatiser l'extraction, le stockage et l'analyse des documents techniques des réunions d'un Working Group (WG) du 3GPP, en les récupérant à partir des serveurs FTP du 3GPP. L'application fournit une interface interactive permettant de visualiser et analyser ces données.

## Fonctionnalités Principales
### 1. Acquisition et Stockage
- Connexion automatique aux serveurs FTP du 3GPP.
- Téléchargement et extraction des fichiers (PDF, DOCX, XLSX, etc.).
- Filtrage des documents pertinents (Discussion Papers, Liaison Statements, etc.).
- Organisation et sauvegarde des fichiers localement et sur le cloud.

### 2. Extraction et Analyse des Données
- Extraction des métadonnées à partir du fichier TDoc (Excel).
- Analyse automatique du contenu des documents.
- Génération de résumés et extraction des problèmes/solutions à l'aide d'un LLM.
- Classification des documents par sujet.

### 3. Interface Utilisateur et Visualisation
- Tableau de bord interactif avec statistiques et suivi en temps réel.
- Visualisation des documents avec filtres (thème, type, période, etc.).
- Modification et téléchargement des fichiers Excel traités.

## Technologies Utilisées
| Fonction | Technologie |
|----------|------------|
| Téléchargement FTP | `ftplib` (Python) |
| Extraction ZIP | `zipfile` |
| Lecture PDF | `PyMuPDF`, `pdfminer.six` |
| Lecture Word | `python-docx` |
| Manipulation Excel | `pandas`, `openpyxl` |
| Modèle NLP | `transformers`, `spaCy` |
| Interface Web | `Streamlit`, `Dash` |
| Visualisation | `matplotlib`, `seaborn`, Power BI |
| Automatisation | `cron`, `task scheduler` |
| Sauvegarde cloud | API Google Drive, OneDrive |

## Installation
### Prérequis
- Python 3.8+
- Clé API pour accéder au LLM (Groq ou autre)
- Accès à un serveur FTP du 3GPP

### Installation des dépendances
```bash
pip install -r requirements.txt
```

## Utilisation
1. **Configurer les paramètres FTP** dans `config.json`.
2. **Lancer l'acquisition des données** :
   ```bash
   python acquisition.py
   ```
3. **Exécuter l'analyse et l'extraction des informations** :
   ```bash
   python analyse.py
   ```
4. **Démarrer l'interface utilisateur** :
   ```bash
   streamlit run app.py
   ```

## Améliorations Futures
- Ajout d'une gestion avancée des utilisateurs.
- Intégration d'une recherche avancée par mot-clé.
- Optimisation des performances pour le traitement des gros volumes de données.

## Auteurs
