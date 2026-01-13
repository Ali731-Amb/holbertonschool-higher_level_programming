#!/usr/bin/python3
# Boucle unique pour parcourir tous les codes ASCII des lettres minuscules
for code in range(97, 123):  # 97 = 'a', 122 = 'z'
    print(f"{chr(code)}", end="")
