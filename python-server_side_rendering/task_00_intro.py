def generate_invitations(template, attendees):
    """
    Génère des invitations personnalisées en respectant strictement
    les messages d'erreur et les contraintes de types demandés.
    """

    # 🔹 2. Vérification des types
    if not isinstance(template, str):
        print(f"Invalid input type for template: {type(template).__name__}")
        return

    if not isinstance(attendees, list):
        print(f"Invalid input type for attendees: {type(attendees).__name__}")
        return

    # Vérification que chaque élément est un dictionnaire
    for person in attendees:
        if not isinstance(person, dict):
            print("Invalid input type for attendees: list must contain dicts")
            return

    # 🔹 3. Vérification des cas vides
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 🔹 4. Boucle principale
    for index, person in enumerate(attendees, start=1):

        # 5.1 -> Copie du template
        invitation_content = template

        # 5.2 & 5.3 -> Récupérer, nettoyer et remplacer
        fields = ["name", "event_title", "event_date", "event_location"]

        for field in fields:
            # Récupération avec get()
            value = person.get(field)

            # Remplacement par "N/A" si la valeur est None ou vide
            if value is None or value == "":
                clean_value = "N/A"
            else:
                clean_value = str(value)

            # Remplacement dans la copie du template
            placeholder = "{" + field + "}"
            invitation_content = invitation_content.replace(
                placeholder, clean_value
            )

        # 🔹 6. Création du fichier (output_X.txt)
        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(invitation_content)
        except IOError as e:
            print(f"Error writing to {filename}: {e}")
