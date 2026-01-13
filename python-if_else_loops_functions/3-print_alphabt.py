#!/usr/bin/python3
# Boucle unique pour parcourir tous les codes ASCII des lettres minuscules
for code in range(97, 123):  # 'a' à 'z'
    if code != 101 and code != 113:  # ignorer 'e' et 'q'
        print(f"{chr(code)}", end="")
