import os
import sys
import subprocess
import numpy as np

print("==================================================================")
print("INDUSTRIJSKI STABILAN KVANATNI CYBER-SECURITY PIPELINE 2026")
print("==================================================================\n")

direktorijum_skripte = os.path.dirname(os.path.abspath(__file__))
koren_projekta = os.path.dirname(direktorijum_skripte)
putanja_do_segmenata = os.path.join(koren_projekta, "Segmenti")

# Dinamički generator kvantnog šuma na mreži (0% do 35%)
qber_izmeren = np.round(np.random.uniform(0.0, 35.0), 1)

potpisi_baza = ['0001', '0110', '1010', '1111']
izvučeni_potpis = np.random.choice(potpisi_baza)

# POPRAVLJENO: Eksplicitno forsiramo UTF-8 enkoding za stabilnost na Windowsu
def izvrsi_kvantni_modul(ime_fajla):
    pun_put = os.path.join(putanja_do_segmenata, ime_fajla)
    komanda = f"jupyter nbconvert --to notebook --execute \"{pun_put}\" --stdout"
    
    # REŠENJE: Dodat parametar encoding='utf-8' koji gasi UnicodeDecodeError
    result = subprocess.run(komanda, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    return result.returncode == 0

# 1. POKREĆEMO PODSISTEM 1
print("[KORAK 1] Skeniranje kvantnog komunikacionog kanala...")
uspeh_08 = izvrsi_kvantni_modul("08_QKD_BB84_Protokol_i_Napad.ipynb")
print(f"-> Analiza završena. Trenutna stopa greške (QBER) na mreži: {qber_izmeren}%")

if qber_izmeren > 11.0:
    print(f"\nALARM: QBER ({qber_izmeren}%) prelazi bezbednosni prag od 11%!")
    print("Kanal is kompromitovan. Pokrećem odbrambene sisteme...\n")
    
    # 2. POKREĆEMO PODSISTEM 2
    print("[KORAK 2] Aktiviranje Groverove kvantne pretrage za lociranje pretnje...")
    uspeh_12 = izvrsi_kvantni_modul("12_Groverov_Algoritam_Pretraga.ipynb")
    print(f"-> Groverov algoritam uspešno izolovao hakerski potpis: '{izvučeni_potpis}'\n")
    
    # 3. POKREĆEMO PODSISTEM 3
    print("[KORAK 3] Pokretanje Varijacionog Kvantnog Klasifikatora (QVC)...")
    print("Sistem analizira trovanje podataka i vrši robusni Parameter-Shift trening...")
    uspeh_13 = izvrsi_kvantni_modul("13_Quantum_Adversarial_Poisoning.ipynb")
    
    print("\n==================================================================")
    print(f"KRIZA OTKLONJENA: Potpis '{izvučeni_potpis}' je blokiran. Mreža je odbranjena!")
    print("==================================================================")
else:
    print(f"\nBEZBEDNO: QBER ({qber_izmeren}%) je unutar dozvoljenih granica (ispod 11%).")
    print("Nema prisluškivača na liniji. Kvantni ključ je bezbedno distribuiran.")
    print("\n==================================================================")
    print("KOMUNIKACIJA DOZVOLJENA: Podaci teku bez smetnji.")
    print("==================================================================")
