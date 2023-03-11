def distance_toilettes(marches, hauteur):
    distance_jour = 2 * marches * hauteur
    distance_semaine = 7 * distance_jour / 100
    return round(distance_semaine / 100, 2)
marches = 50
hauteur = 20
distance = distance_toilettes(marches, hauteur)
print(f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance} m par semaine.")
