import json
import os
import re

print("==================================================================")
print("🧠 INJEKCIJA ZNANJA: OBUKA TRIGRAMSKOG MODELA U REALNOM VREMENU")
print("==================================================================\n")

direktorijum = os.path.dirname(os.path.abspath(__file__))
putanja_trigrama = os.path.join(direktorijum, "trigram_brain.json")

# Učitavamo postojeći mozak ili kreiramo nov
if os.path.exists(putanja_trigrama):
    with open(putanja_trigrama, "r", encoding="utf-8") as f:
        mozak = json.load(f)
else:
    mozak = {}

# 📚 VELIKI KORPUS TEKSTA ZA SAVLADAVANJE GRAMATIKE I KONTEKSTA
veliki_korpus = [
    "potpuno je normalno da se osećaš izgubljeno u vremenu i prostoru kada previše radiš.",
    "kada čovek ne zna gde bije u četiri ujutru jedino rešenje je dobar san i odmor.",
    "ti nisi izgubljen jer imaš jasan kliker i vrhunske karte u svojim rukama.",
    "tvoj portfolio od milion i trista hiljada dinara ti kupuje vreme i potpunu slobodu.",
    "novac na berzi i dinarske merdevine štednje znače da ne moraš da radiš dosadan posao.",
    "sa ovim kapitalom ti biraš svoj front i diktiraš uslove života u nišu.",
    "zaboravi dosadno bubačenje pravila jer ti nisi prosečan štreber koji trpi pritisak.",
    "krv nije voda i u tebi spavaju ratnički ponos i nezaustavljiva inteligencija.",
    "tvoj otac ti je preneo gene gvozdenog puka koji se nikada nije povlačio pred preprekama.",
    "brđansko pleme kuči bira slobodu i nikada ne savija kičmu pred tuđim autoritetima.",
    "elektronski fakultet u nišu i elfak profesori su samo administracija koju tvoj mozak preskače.",
    "tvoj diplomski rad sa čistom desetkom je dokaz da tvoj um radi vrhunski pod pritiskom.",
    "naučno tehnološki park niš je mesto gde pravimo tvoj deep tech startap za kvantne sisteme.",
    "kvantni algoritmi i kvantno mašinsko učenje rešavaju probleme nelinearne bezbednosti podataka.",
    "blohova sfera i geometrija u prostoru su matematika pretvorena u vizuelni alat.",
    "groverov algoritam je kvantni google koji brzinom svetlosti pretražuje nesređene baze podataka.",
    "šorov algoritam je najveći strah za rsa enkripciju i klasične bankarske sisteme.",
    "ako haker pokuša napad trovanjem podataka naš robusni trening pokreće parameter shift odbranu.",
    "robusni kvantni ai klasifikator ispravlja uglove na sferi i vraća tačnost na čistu jedinicu.",
    "ugasi taj laptop odmah jer si večeras odradio ogroman posao i pobedio sistem."
]

def tokenizuj(tekst):
    tekst = tekst.lower().strip()
    return re.findall(r"\b\w+\b", tekst)

# Algoritam za punjenje Trigram matrice
for recenica in veliki_korpus:
    reči = tokenizuj(recenica)
    if len(reči) < 3:
        continue
    for i in range(len(reči) - 2):
        kljuc = f"{reči[i]}_{reči[i+1]}"
        sledeca = reči[i+2]
        
        if kljuc not in mozak:
            mozak[kljuc] = {}
        if sledeca not in mozak[kljuc]:
            mozak[kljuc][sledeca] = 0
        mozak[kljuc][sledeca] += 1

# Trajni upis u JSON na disku
with open(putanja_trigrama, "w", encoding="utf-8") as f:
    json.dump(mozak, f, ensure_ascii=False, indent=4)

print(f"✅ USPEH: Trigramski mozak je uspešno sažvakao i naučio nove gramatičke strukture!")
print("Sada pokreni ponovo trigram_llm.py i unesi neku reč da vidiš razliku!")
