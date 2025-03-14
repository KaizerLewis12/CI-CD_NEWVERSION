import shutil
import os
import zipfile  # Pour créer un fichier ZIP


def deploy_model():
    """
    Simule le déploiement du modèle en copiant le fichier du modèle et en le compressant en un fichier ZIP.
    """
    source = 'models.pkl'  # Le modèle d'origine
    destination = 'deployed_model.pkl'  # Le modèle déployé

    try:
        # Copier le modèle vers le dossier de déploiement
        shutil.copy(source, destination)
        print("Modèle déployé avec succès.")

        # Créer un fichier ZIP contenant le modèle déployé
        zip_filename = 'deployed_model.zip'  # Le nom du fichier ZIP
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(destination, os.path.basename(destination))  # Ajouter le fichier déployé dans le ZIP

        print(f"Modèle compressé dans le fichier ZIP : {zip_filename}")

        # Optionnel : supprimer le fichier déployé une fois qu'il est compressé
        os.remove(destination)
        print(f"Le fichier déployé a été supprimé après compression.")

    except Exception as e:
        print("Échec du déploiement :", e)


def main():
    deploy_model()


if __name__ == "__main__":
    main()
