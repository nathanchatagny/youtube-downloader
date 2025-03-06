import yt_dlp
import os

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
    Télécharge une vidéo depuis YouTube à l'aide de yt-dlp.

    Paramètres:
    - url (str) : URL de la vidéo YouTube à télécharger.
    - chemin_destination (str) : Dossier de destination.

    Retourne : Aucun, mais affiche des messages de statut.
    """
    try:
        # Vérifier si le dossier de destination existe
        if not os.path.exists(chemin_destination):
            os.makedirs(chemin_destination)

        options = {
            "format": "bv*+ba/best",  # Meilleur format vidéo + audio
            "outtmpl": os.path.join(chemin_destination, "%(title)s.%(ext)s"),
            "progress_hooks": [afficher_progression],
            "noplaylist": True,
            "nocheckcertificate": True,  # Évite les erreurs SSL
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            print(f"Début du téléchargement de : {url}")
            ydl.download([url])
            print(f"Téléchargement terminé ! Vidéo enregistrée dans : {chemin_destination}")
    
    except Exception as e:
        print(f"❌ Erreur lors du téléchargement : {e}")

if __name__ == "__main__":
    url_video = input("Entrez l'URL de la vidéo YouTube : ").strip()
    chemin = input("Entrez le chemin de destination (laisser vide pour le dossier actuel) : ").strip() or "."

    if not url_video:
        print("L'URL ne peut pas être vide.")
    else:
        telecharger_video(url_video, chemin)

#/Users/nathanchatagny/Desktop/Code/youtube-downloader
#python3 -m yt_dlp "https://www.youtube.com/watch?v=48egIgP27W4"