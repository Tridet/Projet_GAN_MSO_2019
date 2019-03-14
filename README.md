# Projet_GAN

Ce projet a pour point de départ l'article de Reed Scott [Generative Adversarial Text-to-Image Synthesis](https://arxiv.org/abs/1605.05396) et s'appuie sur l'implémentation qui en a été faite par [Alaa El-Nouby](https://github.com/aelnouby/Text-to-Image-Synthesis). L'originalité de notre travail consiste en deux points : 
* l'implémentation d'une fonction de test qui n'était pas présente à la base chez Alaa El-Nouby ;
* la création d'embeddings basés sur [InferSent](https://github.com/facebookresearch/InferSent) qui constitue un modèle de langage différent de celui utilisé par Reed Scott.

## Fonctionnement

### Entrainement

Pour entrainer le modèle, il faut : 
* choisir les arguments pertinents dans `runtime.py`
  * `--inference, default=False` pour l'entrainement et `default=True` pour le test.
  * `--cls`, sélectionner la valeur désirée.
  * `--pre_trained_disc` et `--pre_trained_gen` avec `default=None` pour l'entrainement et le chemin correspondant aux modèles pré-entrainés pour le test.
  * `--dataset` avec la valeur `birds` ou `flowers`.
  * `--num_workers, default=0` changer la valeur si on utilise le multiprocessing.
  * `--epochs, default=200` c'est la valeur recommandée.
  * vous n'avez pas besoin de modifier les autres valeurs.
* lancer `visdom`.
* lancer `python runtime.py`.

### Test

Pour tester le modèle, il faut :
* choisir les arguments pertinentes dans `runtime.py`
  * `--inference, default=True` pour le test.
  * `--pre_trained_disc` et `--pre_trained_gen` avec `default=/my/path/disc_190.pth` (par exemple) pour le test.
  * `--dataset` avec la valeur `birds` ou `flowers`.
  * les autres valeurs n'ont pas d'importance.
* lancer `python runtime.py`

## Datasets

Pour reproduire les résultats obtenus, vous pouvez télécharger les datasets [Caltech-UCSD Birds 200](http://www.vision.caltech.edu/visipedia/CUB-200.html) et [Flowers](http://www.robots.ox.ac.uk/~vgg/data/flowers/102/) qui contiennent les images, leurs légendes et les embeddings correspondants. Cependant, nous utiliserons les embeddings que nous avons conçu grâce à Infersent.

## Embeddings

Lien vers les modèles de langage, nécessaire pour faire soi-même les tests : [birds](https://drive.google.com/open?id=1VISSkPvNZebwAazCtDVbry2YadDjA2iy) et [flowers](https://drive.google.com/open?id=1EFsmlcL19rSXTdpJF7v71og6YOapkGUW).

Si vous souhaitez les générer vous-même, les fichiers utilisés sont dans le dossier InferSent, et il faut se référer au [GitHub de Infersent](https://github.com/facebookresearch/InferSent) pour les faire fonctionner.

## Pre-trained models

Lien vers les discriminateurs et générateurs pré-entrainés [flowers](https://drive.google.com/open?id=1XtlZflv0Hz_Fjz3eKpPm3uHpscaH6Js9), [birds](https://drive.google.com/open?id=1GHaASXrzDqqyxiS8pMn_lw_ceVpQdlTb) et [birds_cls](https://drive.google.com/open?id=1RLsRETS2jIrLXzvTJaEMd4rUV8dR_mNu)


### Remerciements
Merci à M. Liming Chen d'avoir été notre tuteur pour ce projet, ainsi qu'à Daniel Muller et à Mohsen Ardabilian pour leurs critiques constructives.
