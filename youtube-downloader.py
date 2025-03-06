import yt_dlp

def afficher_progression(progress):
    """
    Affiche la progression du téléchargement.

    Paramètres :
    - progress (dict) : Informations sur l'état actuel du téléchargement.
    """
    if progress.get('status') == 'downloading':
        downloaded = progress.get('downloaded_bytes', 0) / 1024 / 1024
        total = progress.get('total_bytes', 0) / 1024 / 1024
        print(f"Téléchargement en cours : {downloaded:.2f} MB sur {total:.2f} MB")
    elif progress.get('status') == 'finished':
        print("Téléchargement terminé !")

def telecharger_video(url, chemin_destination="."):
    """
    Télécharge une vidéo depuis YouTube à l'aide de yt-dlp, sans fusionner les flux vidéo et audio.
    
    Paramètres:
    - url (str) : URL de la vidéo YouTube à télécharger.
    - chemin_destination (str) : Dossier de destination pour enregistrer la vidéo.
    
    Retourne : Aucun, mais affiche des messages de statut.
    """
    try:
        # Options de téléchargement sans fusionner les flux vidéo et audio
        options = {
            "format": "best",  # Télécharge la meilleure qualité vidéo disponible (avec audio intégré)
            "outtmpl": f"{chemin_destination}/%(title)s.%(ext)s",  # Définir le modèle de nom pour le fichier téléchargé
            "progress_hooks": [afficher_progression],  # Afficher la progression pendant le téléchargement
            "noplaylist": True,  # Ne pas télécharger les vidéos d'une playlist
        }

        # Initialisation de yt-dlp et téléchargement
        with yt_dlp.YoutubeDL(options) as ydl:
            print(f"Début du téléchargement de la vidéo depuis : {url}")
            ydl.download([url])
            print(f"Téléchargement terminé ! La vidéo est enregistrée dans : {chemin_destination}")
    
    except Exception as e:
        print(f"Une erreur s'est produite lors du téléchargement : {e}")

if __name__ == "__main__":
    # Demander à l'utilisateur l'URL de la vidéo et le dossier de destination
    url_video = input("Entrez l'URL de la vidéo YouTube : ").strip()
    chemin = input("Entrez le chemin de destination (laisser vide pour le dossier actuel) : ").strip() or "."

    # Vérification de l'URL
    if not url_video:
        print("L'URL de la vidéo ne peut pas être vide.")
    else:
        # Lancer le téléchargement
        telecharger_video(url_video, chemin)

#//Users/nathanchatagny/Desktop/Code/youtube-downloader