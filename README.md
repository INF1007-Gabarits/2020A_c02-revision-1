[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Chatbot pour Twitch! (révision)

<!-- Avant de commencer. Consulter les instructions à suivre dans [instructions.md](instructions.md) -->

Nous allons écrire un chatbot, c'est-à-dire un programme qui lit le texte dans le clavardage d'un stream Twitch et qui répond à des commandes en utilisant un compte Twitch.

## Avant tout, il faut un compte pour le chatbot

Les sessions de clavardage associés aux streams Twitch utilisent le protocole IRC (*Internet Relay Chat*) pour communiquer. C'est un vieux protocole (début années 90) très populaire et utilisé pour beaucoup de choses. Pour que votre chatbot puisse se connecter au IRC de Twitch, il lui faut un compte Twitch valide avec lequel se connecter. Vous ne pouvez pas simplement entrer votre nom d'utilisateur et votre mot de passe, il vous faut un jeton d'identification. Ce jeton vous sert essentiellement de mot de passe pour vous connecter au IRC, mais sans réellement utiliser votre mot de passe.

Vous pouvez utiliser votre propre compte pour le chatbot, ce qui fait que celui-ci va parler pour vous dans le *chat*. Pour générer facilement un jeton, connectez-vous à votre compte Twitch dans votre fureteur puis allez sur https://twitchapps.com/tmi/. On vous demandera la première fois de connecter l'application de génération de jetons à votre compte (vous approuvez), puis on vous donnera un jeton sous la forme `oauth:séquence-de-lettres-et-de-chiffres`.

<img src="doc/assets/oauth_token_gen.png">

C'est ce jeton (incluant le `oauth:`) que vous utilisez comme mot de passe IRC. Écrivez-le en quelque part et ayez-le à portée de main pour faire les exercices.

## Révision chapitre 7 (fonctions)

### Répondre avec une salutation

TODO: Utilisation sommaire de la classe `TwitchBot` et quel format de callback est attendu.

TODO: Callbacks, fermetures lexicales and shit.

## Révision chapitre 8 (format de fichiers)

### Répondre avec une citation aléatoire

TODO: Rappel sur les fichiers INI et JSON.

TODO: Explication sur le choix aléatoire d'une citation.

## Révision chapitre 9 (bonnes pratiques)

### Passer des arguments au script

TODO: Rappel sur `argparse`

## Révision chapitre 11 (orientée-objet)

### Matière additionnelle

TODO: `dataclasses`

TODO: Décorateurs

### Créer une classe de chatbot qui met tout le reste ensemble

TODO: Utilisation attendue de la classe `TwitchBot`; Diagramme de classe de la librairie.

TODO: Donner une citation aléatoire dans une catégorie ou dans tout.

