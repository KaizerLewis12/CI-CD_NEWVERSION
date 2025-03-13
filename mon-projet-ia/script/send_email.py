import smtplib
import sys
from email.message import EmailMessage
import os


def send_email(zip_filepath):
    """
    Envoie un email avec le fichier ZIP en pièce jointe.
    """
    if not os.path.exists(zip_filepath):
        print("Fichier ZIP non trouvé.")
        return

    # Paramètres de l'email
    sender_email = "contactshydra0@gmail.com"  # Remplacez par l'email de l'expéditeur
    receiver_emails = ["issabachir6@gmail.com", "simocurtis1207@gmail.com"]  # Liste des destinataires
    subject = "Modèle et Documentation - Projet IA de Mr Fomekong"
    body = "Bonjour,\n\nVeuillez trouver ci-joint le modèle déployé et la documentation générée.\n\nCordialement,\nL'équipe IA"

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

    # Paramètres SMTP
    smtp_server = "smtp.example.com"  # Remplacer par le serveur SMTP
    smtp_port = 587

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # Récupération des credentials depuis les variables d'environnement (définies via GitHub Secrets)
            smtp_username = os.environ.get('SMTP_USERNAME')
            smtp_password = os.environ.get('SMTP_PASSWORD')

            if not smtp_username or not smtp_password:
                raise ValueError("Les identifiants SMTP ne sont pas définis dans les variables d'environnement.")

            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            print("Email envoyé avec succès.")
    except Exception as e:
        print("Erreur lors de l'envoi de l'email :", e)


def main():
    if len(sys.argv) != 2:
        print("Usage: python send_email.py <chemin_vers_zip>")
        sys.exit(1)
    zip_filepath = sys.argv[1]
    send_email(zip_filepath)


if __name__ == "__main__":
    main()
