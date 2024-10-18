# Téléchargeur de vidéos YouTube avec yt-dlp

Ce projet vous permet de télécharger des vidéos YouTube à partir d'une liste d'URLs contenues dans un fichier texte. Il utilise `yt-dlp`, un fork amélioré de `youtube-dl`, pour effectuer les téléchargements.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Journal des modifications](#journal-des-modifications)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Fonctionnalités

- Téléchargement des vidéos à la meilleure qualité disponible.
- Gestion des échecs de téléchargement avec journalisation.
- Option de réessayer plusieurs fois en cas d'échec.
- Sauvegarde des URLs échouées dans un fichier.

## Prérequis

- Python 3.x
- `yt-dlp.exe` (téléchargeable [ici](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe))
- Un fichier texte contenant les URLs des vidéos à télécharger.

## Installation

1. Clonez ce dépôt ou téléchargez le code source.
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo
