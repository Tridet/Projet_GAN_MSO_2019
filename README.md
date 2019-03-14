# Projet_GAN

Ce projet a pour point de départ l'article de Reed Scott [Generative Adversarial Text-to-Image Synthesis](https://arxiv.org/abs/1605.05396) et s'appuie sur l'implémentation qui en a été faite par [Alaa El-Nouby](https://github.com/aelnouby/Text-to-Image-Synthesis). L'originalité de notre travail consiste en deux points : 
* l'implémentation d'une fonction de test qui n'était pas présente à la base chez Alaa El-Nouby ;
* la création d'embeddings basés sur [InferSent](https://github.com/facebookresearch/InferSent) qui constitue un modèle de langage différent de celui utilisé par Reed Scott.

## Fonctionnement

## Datasets

Pour reproduire les résultats obtenus, vous pouvez télécharger les datasets [Caltech-UCSD Birds 200](http://www.vision.caltech.edu/visipedia/CUB-200.html) et [Flowers](http://www.robots.ox.ac.uk/~vgg/data/flowers/102/) qui contiennent les images, leurs légendes et les embeddings correspondants. Cependant, nous utiliserons les embeddings que nous avons conçu grâce à Infersent.

## Embeddings

Lien vers les modèles de langage, nécessaire pour faire soi-même les tests : [birds](https://drive.google.com/open?id=1VISSkPvNZebwAazCtDVbry2YadDjA2iy) et [flowers](https://drive.google.com/open?id=1EFsmlcL19rSXTdpJF7v71og6YOapkGUW)

## Pre-trained models

Lien vers les discriminateurs et générateurs pré-entrainés [flowers](https://drive.google.com/open?id=1XtlZflv0Hz_Fjz3eKpPm3uHpscaH6Js9), [birds](https://drive.google.com/open?id=1GHaASXrzDqqyxiS8pMn_lw_ceVpQdlTb) et [birds_cls](https://drive.google.com/open?id=1RLsRETS2jIrLXzvTJaEMd4rUV8dR_mNu)


### Remerciements
Merci à M. Liming Chen d'avoir été notre tuteur pour ce projet, ainsi qu'à Daniel Muller et à Mohsen Ardabilian pour leurs critiques constructives.
