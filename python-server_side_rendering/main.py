from task_00_intro import generate_invitations

# 1. Lecture du template
try:
    with open('template.txt', 'r', encoding='utf-8') as file:
        template_content = file.read()
except FileNotFoundError:
    print("Erreur : Le fichier template.txt est introuvable.")
    template_content = None

# 2. Données de test
attendees = [
    {"name": "Alice", "event_title": "Python Conference",
    "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop",
    "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit",
    "event_date": None, "event_location": "Boston"}
]

# 3. Exécution
if template_content is not None:
    generate_invitations(template_content, attendees)