import json
import os
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("==================================================================")
print("POKRETANJE REALNOG QML ALGORITMA: UČENJE IZ JSON DATOTEKE")
print("==================================================================\n")

# HAKOVANJE PUTANJE: Nalazimo tačan folder u kome se nalazi ova skripta
direktorijum_skripte = os.path.dirname(os.path.abspath(__file__))
apsolutna_putanja_json = os.path.join(direktorijum_skripte, "podaci.json")

# 1. UCITAVANJE PODATAKA IZ JSON FAJLA PREKO APSOLUTNE PUTANJE
print("[KORAK 1] Čitanje datoteke 'podaci.json'...")

if not os.path.exists(apsolutna_putanja_json):
    raise FileNotFoundError(f"\n🚨 KRIZA: Fajl 'podaci.json' nije pronađen na lokaciji:\n{apsolutna_putanja_json}\n"
                            f"Proveri da li je fajl u istom folderu kao i skripta qml_json_trening.py!")

with open(apsolutna_putanja_json, "r") as f:
    sirovi_podaci = json.load(f)

# Pakujemo podatke u NumPy nizove koje naš AI razume
X = [] # Karakteristike (iznos i anomalija)
y = [] # Tačne oznake (0 = bezbedno, 1 = rizik)

for stavka in sirovi_podaci:
    X.append([stavka["iznos"] * np.pi, stavka["anomalija"] * np.pi]) # Množimo sa pi da dobijemo uglove za sferu
    y.append(stavka["rizik"])

X = np.array(X)
y = np.array(y)
print(f"-> Uspešno učitano {len(X)} uzoraka iz JSON-a.\n")

# 2. POSTAVLJANJE PARAMETARA ZA KVANATNI AI
epohe = 10
stopa_ucenja = 0.3
tezina = 0.1 # Početni nasumični ugao našeg kvantnog neurona
istorija_greske = []

print("[KORAK 2] Pokretanje kvantne trening petlje (Parameter-Shift)...")

# Pomoćna funkcija koja računa grešku sistema za trenutni ugao (težinu)
def izracunaj_gresku(trenutna_tezina):
    ukupna_greska = 0
    for i in range(len(X)):
        kolo = QuantumCircuit(1)
        kolo.rx(X[i][0], 0) # Kodiramo prvi parametar iz JSON-a (iznos)
        kolo.ry(trenutna_tezina, 0) # Naš promenljivi kvantni neuron
        
        stanje = Statevector.from_instruction(kolo)
        verovatnoca_jedinice = np.abs(stanje.data[1])**2
        
        # Kvadratna greška između predikcije i prave oznake iz JSON-a
        ukupna_greska += (verovatnoca_jedinice - y[i])**2
    return ukupna_greska / len(X)

# 3. GLAVNA PETLJA UČENJA
for epoha in range(epohe):
    trenutna_greska = izracunaj_gresku(tezina)
    istorija_greske.append(trenutna_greska)
    
    # Parameter-Shift pravilo za računanje smera (gradijenta)
    shift = 0.01
    greska_plus = izracunaj_gresku(tezina + shift)
    greska_minus = izracunaj_gresku(tezina - shift)
    
    numericki_gradijent = (greska_plus - greska_minus) / (2 * shift)
    tezina = tezina - stopa_ucenja * numericki_gradijent
    
    print(f"Epoha {epoha+1}/{epohe} | Greška modela: {trenutna_greska:.4f} | Ugao neurona: {tezina:.2f} rad")

print("\n--- TRENING ZAVRŠEN ---")
print(f"Konačni optimizovani ugao tvog kvantnog neurona: {tezina:.2f} radijana")

# 4. GRAFIČKI PRIKAZ KAKO JE NAŠ AI SAVLADAO JSON PODATKE
plt.plot(range(1, epohe+1), istorija_greske, marker='o', color='#2ecc71', linewidth=2)
plt.xlabel('Epoha učenja')
plt.ylabel('Nivo greške (Loss)')
plt.title('Uspelo učenje iz JSON-a: Kako kvantni AI smanjuje grešku')
plt.grid(True)
plt.show()
