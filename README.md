# Rendu de projet

## Analyse de texte avec Python

* Les exercices à résoudre:

1. Ecrire une fonction hascap(s) qui renvoie tout les mots de la chaîne s commençant par une majuscule.

Pour ce faire utiliser la fonction ord() pour obtenir le code ASCII des lettres (Les lettres majuscule ont un code allant de 65 à 90).

2. Proposer une fonction inflation(s) qui va doubler la valeur de tout les nombre dans la chaine s. Exemple : « Le prix est de 27 euros » devient « Le prix est de 54 euros ».

Utiliser la fonction enumerate() pour lancer une boucle for (Taper dans Google « enumerate boucle for ».)

3. Proposer une fonction lignes qui à partir d’une long chaîne s (>100 caractères) renvoie une liste de chaîne de caractères contenant chacun 24 caractères maximum et terminant par un espace.

Voici un exemple de chaîne sur le quel vous pouvez travailler :
s = "Onze ans déjà que cela passe vite Vous "
s += "vous étiez servis simplement de vos armes la "
s += "mort n‘éblouit pas les yeux des partisans Vous «
s += "aviez vos portraits sur les murs de nos villes«
* Les solutions de ces exercices se trouvent dans le fichier .py

4. Proposer un programme qui renvoie la liste de tout les nombres (y compris décimaux et négatifs) d’une chaîne de caractères.

A tester sur la chaîne : « Les 2 maquereaux valent 6.50 euros ».

5. Proposer une fonction arrondi(s) qui dans la chaîne s troncature tout les nombre décimaux. On autorise les nombres négatifs.

Pour ce faire, vous avez la possibilité d’utiliser :
Des () pour désigner des blocs de données dans l’expression rationnelle.
Pour remplacer chacun des blocs l’expression est r’\1_\2_’.