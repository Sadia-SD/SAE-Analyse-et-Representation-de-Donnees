import os
import requests
from bs4 import BeautifulSoup
import zipfile

# URL de la page contenant les fichiers
url = 'https://www.3gpp.org/ftp/tsg_sa/WG2_Arch/TSGS2_164_Maastricht_2024-08/Docs'

# Fonction pour télécharger un fichier à partir de son URL
def download_file(file_url, save_path):
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Fichier téléchargé avec succès : {save_path}")
    else:
        print(f"Échec du téléchargement pour {file_url}")

# Fonction pour décompresser un fichier ZIP
def unzip_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Fichier décompressé avec succès : {zip_path}")
        # Supprimer le fichier ZIP après décompression
        os.remove(zip_path)
        print(f"Fichier ZIP supprimé : {zip_path}")
    except zipfile.BadZipFile:
        print(f"Le fichier n'est pas un ZIP valide : {zip_path}")

# Récupérer la page HTML
response = requests.get(url)
if response.status_code != 200:
    print(f"Échec de la récupération de la page HTML : {url}")
else:
    # Parser la page HTML pour extraire les liens vers les fichiers
    soup = BeautifulSoup(response.text, 'html.parser')

    # Rechercher tous les liens (balises <a>) dans la page
    links = soup.find_all('a', href=True)

    # Créer un dossier pour les fichiers téléchargés
    download_dir = os.path.join('D:\IUT Villetaneuse\PROJET IUT\projet thales\Données')
    os.makedirs(download_dir, exist_ok=True)

    for link in links:
        file_url = link['href']

        # S'assurer que le lien est un fichier (en général, les liens de fichiers ont une extension comme .zip, .pdf, etc.)
        if file_url.endswith(('.zip', '.pdf', '.docx', '.pptx','.csv')):  # Ajoutez d'autres extensions si nécessaire
            full_url = url + '/' + file_url if not file_url.startswith('http') else file_url
            file_name = os.path.basename(file_url)
            save_path = os.path.join(download_dir, file_name)

            # Télécharger le fichier
            download_file(full_url, save_path)

            # Si le fichier est un ZIP, le décompresser
            if file_name.endswith('.zip'):
                unzip_file(save_path, download_dir)
