def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.
    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)
    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """
    alerte = False
    # Vérification température
    if temp < 18:
        print("⚠️Température trop basse.")
        alerte = True
    elif 18 >= temp <=27:
        print("✅Bonne température.")
    elif temp > 27:
        print("⚠️Température trop élevée.")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("⚠️Humidité trop basse.")
        alerte = True
    elif 30 >= humidite <= 50:
        print("✅Bonne humidité.")
    elif humidite >= 50:
        print("⚠️Humidité trop élevée.")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("⚠️Trop de poussière")
        alerte = True
    else:
        print("✅Poussière acceptable.")

    # Retour final
    if not alerte:
        return "✅Tout est sous contrôle!✅"
    else:
        return "⚠️Environnement non optimal!⚠️"

if __name__ == "__main__":
    #TODO : demander le nombre d'ordinateurs [avec gestion d'erreur].
    #TODO : créer une liste. (température, poussière, humidité).

    #TODO : Pour nombres d'ordinateurs.
        #TODO : Demander température, humidité et poussière. [avec gestion d'erreur]
        #TODO : Ajouter les trois valeurs dans le listes respectives.

    #TODO : Pour nombre d'ordinateurs.
        #TODO: Vérifier l'environnement : utiliser la fonction et afficher le résultat.

    temp = float(input("Entrez la température de l'ordinateur: "))
    humidite = float(input("Entrez l'humidité de l'ordinateur: "))
    poussiere = str.lower(input("Entrez le niveau de poussière (faible, moyenne, élevée): "))
    print(environnement_optimal(temp, poussiere, humidite))
