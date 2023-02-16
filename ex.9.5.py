"""
Scrivete una funzione di nome usa_tutte che richieda una parola e una stringa di
lettere richieste e che restituisca True se la parola utilizza tutte le lettere richieste almeno una volta.
"""

def usa_tutte(parola, lettere_richieste):
    for lettera in lettere_richieste:
        if lettera not in parola:
            return False
    return True

print(usa_tutte("hello", "oelh"))