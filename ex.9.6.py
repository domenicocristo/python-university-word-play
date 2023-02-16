"""
Scrivete una funzione di nome alfabetica che restituisca True se le lettere di una
parola compaiono in ordine alfabetico (le doppie valgono).
"""

def alfabetica(parola):
    precedente = parola[0]
    for lettere in parola:
        if lettere < precedente:
            return False
        precedente = lettere
    return True

print(alfabetica("abcd"))