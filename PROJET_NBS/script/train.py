import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib


def load_data():
    """
    Charge les données pour l'entraînement.
    Pour l'exemple, nous générons des données aléatoires.
    """
    X = np.random.rand(100, 10)  # 100 échantillons, 10 caractéristiques
    y = np.random.randint(0, 2, size=100)  # 100 étiquettes (0 ou 1)
    return X, y


def train_model(X, y):
    """
    Entraîne un modèle de régression logistique.
    """
    model = LogisticRegression()
    model.fit(X, y)
    return model


def main():
    print("Chargement des données...")
    X, y = load_data()

    print("Entraînement du modèle...")
    model = train_model(X, y)

    # Sauvegarde du modèle dans le dossier ../model/
    model_path = 'model.pkl'
    joblib.dump(model, model_path)
    print(f"Modèle entraîné et sauvegardé dans {model_path}")


if __name__ == "__main__":
    main()
