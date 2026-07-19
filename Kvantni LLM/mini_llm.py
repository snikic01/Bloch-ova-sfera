import json
import os
import random
import re

print("==================================================================")
print("🧠 STATISTIČKI JEZIČKI MODEL (MARKOVLJEV LANAC) KOJI STVARNO UČI")
print("==================================================================\n")

direktorijum = os.path.dirname(os.path.abspath(__file__))
putanja_mozga = os.path.join(direktorijum, "model_brain.json")

# 1. UCITAVANJE ILI KREIRANJE MOZGA
if os.path.exists(putanja_mozga):
    with open(putanja_mozga, "r", encoding="utf-8") as f:
        mozak = json.load(f)
    print("AI: Moj mozak je učitan. Već znam neke reči i veze.")
else:
    # Ako fajl ne postoji, kreiramo praznu strukturu
    mozak = {}
    print("AI: Moj mozak je potpuno prazan. Nauči me da pričam!")

def očisti_i_tokenizuj(tekst):
    # Pretvaramo u mala slova i odvajamo reči od znakova interpunkcije
    tekst = tekst.lower().strip()
    reči = re.findall(r"\b\w+\b", tekst)
    return reči

# 2. FUNKCIJA ZA UČENJE U REALNOM VREMENU (Mutacija JSON-a)
def nauci_iz_recenice(tekst):
    reči = očisti_i_tokenizuj(tekst)
    if len(reči) < 2:
        return
    
    # Prolazimo kroz rečenicu i pravimo parove: Reč A -> Reč B
    for i in range(len(reči) - 1):
        trenutna_reč = reči[i]
        sledeća_reč = reči[i+1]
        
        if trenutna_reč not in mozak:
            mozak[trenutna_reč] = {}
            
        if sledeća_reč not in mozak[trenutna_reč]:
            mozak[trenutna_reč][sledeća_reč] = 0
            
        # Povećavamo brojač koliko puta reč B ide nakon reči A
        mozak[trenutna_reč][sledeća_reč] += 1

    # Trajno čuvanje naučenog u JSON fajl na disku
    with open(putanja_mozga, "w", encoding="utf-8") as f:
        json.dump(mozak, f, ensure_ascii=False, indent=4)

# 3. FUNKCIJA ZA GENERISANJE ODGOVORA REČ-PO-REČ
def generisi_odgovor(korisnicki_unos):
    reči_unosa = očisti_i_tokenizuj(korisnicki_unos)
    if not reči_unosa or not mozak:
        return "AI: Moj mozak je trenutno prazan, piši mi još da bih naučio kontekst."
    
    # Biramo početnu reč iz korisnikovog unosa ako je znamo, inače uzimamo nasumičnu iz mozga
    startne_opcije = [w for w in reči_unosa if w in mozak]
    if startne_opcije:
        trenutna_reč = random.choice(startne_opcije)
    else:
        trenutna_reč = random.choice(list(mozak.keys()))
        
    odgovor = [trenutna_reč]
    
    # Generišemo rečenicu od maksimalno 12 reči na osnovu verovatnoće
    for _ in range(12):
        if trenutna_reč not in mozak or not mozak[trenutna_reč]:
            break
            
        # Računamo verovatnoću: izvlačimo reči i njihove učestanosti
        opcije = list(mozak[trenutna_reč].keys())
        tezine = list(mozak[trenutna_reč].values())
        
        # Statistički izbor sledeće reči na osnovu težina
        sledeća_reč = random.choices(opcije, weights=tezine)[0]
        odgovor.append(sledeća_reč)
        trenutna_reč = sledeća_reč
        
    return " ".join(odgovor)

# 4. GLAVNA PETLJA RAZGOVORA
print("AI: Spreman sam za učenje i ćaskanje. (Ukucaj 'izlaz' za kraj)\n")

while True:
    unos = input("Ti: ")
    if unos.lower().strip() == "izlaz":
        print("\nAI: Vidimo se! Pogledaj fajl model_brain.json da vidiš šta sam naučio.")
        break
        
    # AI prvo uči iz tvoje rečenice i ažurira JSON bazu
    nauci_iz_recenice(unos)
    
    # AI generiše odgovor koristeći naučene statističke veze
    odgovor = generisi_odgovor(unos)
    print(f"AI: {odgovor}\n")
