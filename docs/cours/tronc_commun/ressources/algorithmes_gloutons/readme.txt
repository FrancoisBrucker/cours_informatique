Pour créer le fichier latex, tapez la commande : `pandoc -s algorithmes_gloutons.md --output=./ressources/algorithmes_gloutons/latex/algorithmes_gloutons.tex` 

Il ne reste plus qu'à nettoyer un peu le code produit :

1. supprimer les références aux td en pdf et au corrigé dans la partie "but"
2. remplacer les \[ par des \( et les \] par des \)