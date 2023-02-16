"""
Scrivete una funzione di nome niente_e che restituisca True se una data parola non contiene la 
lettera "e".
"""

def niente_e(parola):
    for lettera in parola:
        if lettera == "e":
            return False  
    return True

print(niente_e("hello"))