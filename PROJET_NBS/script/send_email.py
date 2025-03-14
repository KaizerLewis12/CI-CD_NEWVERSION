import smtplib
import json
from email.message import EmailMessage
import os


def load_config():
    """
    Charge la configuration depuis keys/config.json.
    """
    config_path = os.path.join(os.path.dirname(__file__), '../keys/config.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print("Erreur lors du chargement du fichier de configuration:", e)
        return {}


def send_email(zip_filepath):
    """
    Envoie un email avec le fichier ZIP en pièce jointe.
    Le fichier ZIP doit être présent à l'emplacement donné.
    """
    if not os.path.exists(zip_filepath):
        print("Fichier ZIP non trouvé :", zip_filepath)
        return

    # Paramètres de l'email
    sender_email = "contactshydra0@gmail.com"  # Adresse de l'expéditeur
    receiver_emails = [
        "issabachir6@gmail.com",
        "simocurtis1207@gmail.com",
        "loydxarian@gmail.com"
    ]  # Liste des destinataires
    subject = "Modèle et Documentation - Projet IA de Mr Fomekong"
    body = (
        "Bonjour,\n\n"
        "Veuillez trouver ci-joint le modèle déployé et la documentation générée.\n\n"
        "Cordialement,\n"
        "L'équipe IA NBS (NTONGA - BACHIR - SIMO)"
    )

    # Création du message email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)
    msg.set_content(body)

    # Ajout de la pièce jointe ZIP
    with open(zip_filepath, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(zip_filepath)
    msg.add_attachment(file_data, maintype='application', subtype='zip', filename=file_name)

    # Récupérer la configuration SMTP depuis les variables d'environnement
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = os.environ.get('SMTP_PORT')
    smtp_username = os.environ.get('SMTP_USERNAME')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    # Si une ou plusieurs variables ne sont pas définies, charger depuis le fichier de config
    if not smtp_server or not smtp_port or not smtp_username or not smtp_password:
        config = load_config()
        smtp_server = config.get('smtp_server', 'smtp.gmail.com')
        smtp_port = config.get('smtp_port', 587)
        smtp_username = config.get('smtp_username', 'contactshydra0@gmail.com')
        smtp_password = config.get('smtp_password', 'aerw wpms oyie tspi')

    try:
        smtp_port = int(smtp_port)
    except ValueError:
        print("Le port SMTP doit être un entier.")
        return

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Active la connexion sécurisée
            if not smtp_username or not smtp_password:
                raise ValueError("Les identifiants SMTP ne sont pas définis.")
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            print("Email envoyé avec succès.")
    except Exception as e:
        print("Erreur lors de l'envoi de l'email :", e)


def main():
    # Le fichier ZIP "model_send.zip" est dans le même dossier que ce script.
    current_dir = os.path.dirname(os.path.realpath(__file__))
    zip_filepath = os.path.join(current_dir, "model_send.zip")
    send_email(zip_filepath)


if __name__ == "__main__":
    main()
