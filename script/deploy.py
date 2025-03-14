import shutil
import os


def deploy_model():
    """
    Simule le déploiement du modèle en copiant le fichier du modèle.
    """
    source = 'model.pkl'
    destination = 'deployed_model.pkl'

    try:
        shutil.copy(source, destination)
        print("Modèle déployé avec succès.")
    except Exception as e:
        print("Échec du déploiement :", e)


def main():
    deploy_model()


if __name__ == "__main__":
    main()
