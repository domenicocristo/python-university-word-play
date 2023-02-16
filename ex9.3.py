"""
Scrivete una funzione di nome evita che richieda una parola e una stringa di lettere 
vietate, e restituisca True se la parola non contiene alcuna lettera vietata.

Modifica poi il programma in modo che chieda all'utente di inserire delle parole e
una stringa di lettere vietate, poi stampa il numero di parole che non ne contengono alcuna.
"""

def evita(parola, lettere_vietate):
    for lettera in lettere_vietate:
        if lettera in parola:
            return False
    return True

parole = input("Inserisci una lista di parole, separate da uno spazio: ").split()
lettere_vietate = input("Inserisci una stringa di lettere vietate: ")
parole_senza_lettere_vietate = [parola for parola in parole if evita(parola, lettere_vietate)]

print("Ci sono", len(parole_senza_lettere_vietate), "parole che non contengono le lettere vietate.")