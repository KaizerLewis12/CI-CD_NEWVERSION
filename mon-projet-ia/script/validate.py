import numpy as np
import joblib
from sklearn.metrics import accuracy_score


def load_data():
    """
    Génère des données aléatoires pour la validation.
    """
    X = np.random.rand(50, 10)  # 50 échantillons
    y = np.random.randint(0, 2, size=50)
    return X, y


def main():
    print("Chargement des données de validation...")
    X, y = load_data()

    # Chargement du modèle entraîné
    try:
        model = joblib.load('../model/model.pkl')
    except Exception as e:
        print("Erreur lors du chargement du modèle :", e)
        return

    print("Validation du modèle...")
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    print(f"Précision (accuracy) : {accuracy:.2f}")


if __name__ == "__main__":
    main()
