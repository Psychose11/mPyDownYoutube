import os
import subprocess
from datetime import datetime

def download_video(url, output_path):
    """Télécharge une vidéo YouTube avec yt-dlp.exe"""
    try:
       
        command = [
            'yt-dlp.exe',
            '--format', 'best', 
            '--output', os.path.join(output_path, '%(title)s.%(ext)s'),
            '--no-playlist', 
            '--retries', '3', 
            url
        ]
        
        print(f"\nTéléchargement de : {url}")
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Téléchargement terminé avec succès")
            return True
        else:
            print(f"❌ Erreur : {result.stderr}")
            return False

    except Exception as e:
        print(f"❌ Erreur : {str(e)}")
        return False

def main():
    input_file = 'zova.txt'
    output_path = 'downloads'
    log_file = 'download_log.txt'
    
    if not os.path.exists('yt-dlp.exe'):
        print("❌ Erreur : yt-dlp.exe non trouvé dans le dossier courant")
        print("Veuillez télécharger yt-dlp.exe depuis : ")
        print("https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe")
        return
    

    os.makedirs(output_path, exist_ok=True)
    
    try:
       
        if not os.path.exists(input_file):
            print(f"❌ Le fichier {input_file} n'existe pas.")
            return
        
      
        with open(input_file, 'r', encoding='utf-8') as file:
            urls = [line.strip() for line in file if line.strip()]
        
        if not urls:
            print("❌ Le fichier est vide.")
            return
        
        print(f"📥 {len(urls)} vidéos à télécharger")
        
      
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entries = [f"=== Session de téléchargement du {current_time} ==="]
        
       
        successful = 0
        failed = []
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Traitement de la vidéo")
            if download_video(url, output_path):
                successful += 1
                log_entries.append(f"✓ {url}")
            else:
                failed.append(url)
                log_entries.append(f"❌ {url}")
        
        
        print("\n=== Rapport final ===")
        print(f"✓ Téléchargements réussis : {successful}/{len(urls)}")
        
        if failed:
            print("\n❌ Échecs :")
            for url in failed:
                print(f"- {url}")
            
            with open('failed_downloads.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(failed))
            print("\nURLs en échec sauvegardées dans 'failed_downloads.txt'")
        
       
        log_entries.append(f"\nRésumé : {successful} réussis, {len(failed)} échecs")
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write('\n'.join(log_entries) + '\n\n')
        
    except Exception as e:
        print(f"\n❌ Erreur générale : {str(e)}")

if __name__ == "__main__":
    main()