import pytest #Importe le module pytest pour faire des test unitaires.
from ExDebug1 import environnement_optimal #Lien avec la fonction de l'autre fichier.

#Le test unitaire pour la fonction environnement_optimal.
def test_evironnement_optimal():
    #Arrange: préparer les valeurs des variables d'entrées et le résultat attendu.
    temperature = 25
    humidite = 40
    poussiere = "faible"
    resultat_attendu = "✅Tout est sous contrôle!✅"

    #Acte: appele la foction.
    resultat_obtenu = environnement_optimal(temperature,poussiere,humidite)

    #Assert: vérifie si le résultat obtenu correspond au résultat attendu.
    assert resultat_attendu == resultat_obtenu

def test_evironnement_optimal2():
    temperature = 30
    humidite = 40
    poussiere = "faible"
    resultat_attendu = "⚠️Environnement non optimal!⚠️"

    resultat_obtenu = environnement_optimal(temperature,poussiere,humidite)

    assert resultat_attendu == resultat_obtenu

def test_evironnement_optimal3():
    temperature = 25
    humidite = 20
    poussiere = "faible"
    resultat_attendu = "⚠️Environnement non optimal!⚠️"

    resultat_obtenu = environnement_optimal(temperature,poussiere,humidite)

    assert resultat_attendu == resultat_obtenu

def test_evironnement_optimal4():
    temperature = 30
    humidite = 25
    poussiere = "faible"
    resultat_attendu = "⚠️Environnement non optimal!⚠️"

    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    assert resultat_attendu == resultat_obtenu