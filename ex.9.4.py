"""
Scrivete una funzione di nome usa_solo che richieda una parola e una stringa di
lettere, e che restituisca True se la parola contiene solo le lettere indicate.
"""

def usa_solo(parola, lettere_valide):
    for lettera in parola:
        if lettera not in lettere_valide:
            return False
    return True

print(usa_solo("hello", "acefhlo"))