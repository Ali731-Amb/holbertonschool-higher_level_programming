#!/usr/bin/python3


def read_file(filename=""):
    """
    Lit un fichier texte (UTF-8) et affiche son contenu sur la sortie standard.

    Args:
        filename (str): Le chemin du fichier à lire. Par défaut, une chaîne vide.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for ligne in f:
            print(ligne, end='')
