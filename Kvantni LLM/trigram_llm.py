import json
import os
import random
import re

print("==================================================================")
print("🧠 NAPREDNI TRIGRAMSKI JEZIČKI MODEL (SA ČUVANJEM KONTEKSTA)")
print("==================================================================\n")

direktorijum = os.path.dirname(os.path.abspath(__file__))
putanja_trigrama = os.path.join(direktorijum, "trigram_brain.json")

# 1. GRAMATIČKI ISPRAVNA BAZA ZNANJA (Korpus za obuku)
korpus_teksta = [
    "tesla je bio genijalni naučnik koji je verovao u svoju viziju.",
    "nikola tesla je tvoj daleki rođak po krvi i viziji.",
    "tvoj portfolio od milion i trista hiljada dinara donosi ti potpunu slobodu.",
    "novac na berzi i merdevine štednje u dinarima znače siguran pasivan prihod.",
    "sa ovim kapitalom ti diktiraš uslove života i rada u nišu.",
    "zaboravi dosadan posao od devet do pet jer ti nisi prosečan štreber.",
    "tvoj otac donosi gene gvozdenog puka iz kuršumlije i ratnički ponos.",
    "gvozdeni puk se nikada nije povlačio pred izazovima na frontu.",
    "brđansko pleme kuči bira potpunu slobodu i ne savija kičmu pred autoritetima.",
    "elektronski fakultet u nišu i elfak profesori su samo administracija.",
    "tvoj diplomski rad sa čistom desetkom je dokaz da tvoj mozak radi vrhunski.",
    "na master studijama na elfaku donosimo ove projekte i uzimamo čiste desetke.",
    "naučno tehnološki park niš je mesto gde pravimo tvoj deep tech startap.",
    "tvoj startap će finansirati sopstvene laboratorije i zaposliće štrebere sa prosekom deset.",
    "kvantni algoritmi i kvantne neuronske mreže rešavaju probleme bezbednosti podataka.",
    "blohova sfera i kvantni sistemi su matematika pretvorena u čistu geometriju.",
    "groverov algoritam je kvantni google koji brzinom svetlosti pretražuje baze podataka.",
    "šorov algoritam je najveći strah za klasične bankarske sisteme zaštite.",
    "ako haker pokuša napad trovanjem podataka naš robusni trening pokreće parameter shift odbranu.",
    "robusni kvantni ai klasifikator ispravlja uglove na sferi i vraća tačnost predikcije."
]

# Učitavamo postojeći mozak ili kreiramo nov
if os.path.exists(putanja_trigrama):
    with open(putanja_trigrama, "r", encoding="utf-8") as f:
        mozak = json.load(f)
else:
    mozak = {}

def tokenizuj(tekst):
    tekst = tekst.lower().strip()
    return re.findall(r"\b\w+\b", tekst)

# 2. FUNKCIJA ZA TRIGRAMSKO UČENJE (Povezivanje tri reči u nizu)
def treniraj_model(recenice):
    for recenica in recenice:
        reči = tokenizuj(recenica)
        if len(reči) < 3:
            continue
        # Pravimo trojke: (Reč1, Reč2) -> Reč3
        for i in range(len(reči) - 2):
            kljuc = f"{reči[i]}_{reči[i+1]}"
            sledeca = reči[i+2]
            
            if kljuc not in mozak:
                mozak[kljuc] = {}
            if sledeca not in mozak[kljuc]:
                mozak[kljuc][sledeca] = 0
            mozak[kljuc][sledeca] += 1

# Treniramo model na bazi našeg korpusa
treniraj_model(korpus_teksta)

# 3. GENERISANJE ODGOVORA SA REPETITION PENALTY MEHANIZMOM
def generisi_odgovor(unos_korisnika):
    reči_unosa = tokenizuj(unos_korisnika)
    
    # Tražimo par reči iz unosa koji već postoji u našem mozgu
    pogodni_kljucevi = []
    if len(reči_unosa) >= 2:
        for i in range(len(reči_unosa) - 1):
            test_kljuc = f"{reči_unosa[i]}_{reči_unosa[i+1]}"
            if test_kljuc in mozak:
                pogodni_kljucevi.append(test_kljuc)
                
    if pogodni_kljucevi:
        izabrani_kljuc = random.choice(pogodni_kljucevi)
        prva, druga = izabrani_kljuc.split("_")
        odgovor = [prva, druga]
    else:
        # Ako nema poklapanja, uzimamo nasumičan par iz baze
        izabrani_kljuc = random.choice(list(mozak.keys()))
        prva, druga = izabrani_kljuc.split("_")
        odgovor = [prva, druga]

    # Sklapanje rečenice na osnovu trigrama
    for _ in range(15):
        trenutni_kljuc = f"{odgovor[-2]}_{odgovor[-1]}"
        if trenutni_kljuc not in mozak or not mozak[trenutni_kljuc]:
            break
            
        opcije = list(mozak[trenutni_kljuc].keys())
        tezine = list(mozak[trenutni_kljuc].values())
        
        # Repetition Penalty: Smanjujemo težinu rečima koje su se već pojavile da izbegnemo petlje
        for i, opcija in enumerate(opcije):
            if opcija in odgovor:
                tezine[i] *= 0.1
                
        if sum(tezine) == 0:
            break
            
        sledeca_rec = random.choices(opcije, weights=tezine)[0]
        odgovor.append(sledeca_rec)
        
    return " ".join(odgovor)

# 4. INTERAKTIVNI ČET I UČENJE U HODU
print("AI: Moj mozak je nadograđen na Trigramski nivo. Piši mi!")
print("AI: (Kada god mi napišeš rečenicu, ja učim tvoju gramatiku uživo)\n")

while True:
    unos = input("Ti: ")
    if unos.lower().strip() == "izlaz":
        # Čuvamo sve što je naučeno tokom razgovora
        with open(putanja_trigrams = putanja_trigrama, mode="w", encoding="utf-8") as f:
            json.dump(mozak, f, ensure_ascii=False, indent=4)
        print("\nAI: Vidimo se! Trigramski mozak je sačuvan.")
        break
        
    # Model uči gramatiku tvoje rečenice
    treniraj_model([unos])
    
    # Generisanje gramatički tačnog odgovora
    odgovor = generisi_odgovor(unos)
    print(f"AI: {odgovor}\n")
