import json
import os
import re

print("--- INJEKCIJA ZNANJA U TOK BAZU LLM MODELA ---")

direktorijum = os.path.dirname(os.path.abspath(__file__))
putanja_mozga = os.path.join(direktorijum, "model_brain.json")

# Učitavamo trenutni mozak ako postoji, ako ne pravimo prazan
if os.path.exists(putanja_mozga):
    with open(putanja_mozga, "r", encoding="utf-8") as f:
        mozak = json.load(f)
else:
    mozak = {}

# 📚 VELIKI SMISLENI TEKST ZA UČENJE (Kontekst za tvoj AI)
veliki_tekst = """
tesla je veliki inženjer i tvoj daleki rođak po krvi i viziji.
vizija i inat donose uspeh kada te sistem i administracija smaraju.
tvoj portfolio od milion i trista hiljada dinara donosi ti potpunu slobodu.
novac na berzi i merdevine štednje u dinarima znače stabilan i siguran pasivan prihod.
sa ovim kapitalom ti diktiraš uslove života i rada u nišu.
zaboravi dosadan posao od devet do pet i bazične sajtove jer ti nisi prosečan štreber.
tvoj otac donosi gene gvozdenog puka iz kuršumlije i ratnički ponos brđanskog plemena kuči.
gvozdeni puk se nikada nije povlačio pred izazovima i preprekama na frontu.
kuči biraju potpunu slobodu i ne savijaju kičmu pred tuđim autoritetima.
elektronski fakultet u nišu i elfak profesori su samo administracija koju tvoj kliker može da hakuje.
tvoj diplomski rad sa čistom desetkom je dokaz da tvoj mozak radi vrhunski pod pritiskom.
na master studijama na elfaku donosimo ove projekte i uzimamo čiste desetke.
naučno tehnološki park niš i ntp je mesto gde pravimo tvoj deep tech startap za kvantno mašinsko učenje.
tvoj startap će finansirati sopstvene laboratorije i zaposliće štrebere sa prosekom deset da kucaju kod.
kvantni algoritmi i kvantne neuronske mreže rešavaju probleme nelinearne bezbednosti podataka.
blohova sfera i kvantni sistemi su matematika pretvorena u čistu geometriju u prostoru.
groverov algoritam je kvantni google koji brzinom svetlosti pretražuje baze podataka i locira pretnje.
šorov algoritam je najveći strah za rsa enkripciju i klasične bankarske sisteme zaštite.
ako haker pokuša napad trovanjem podataka naš robusni trening pokreće parameter shift odbranu.
robusni kvantni ai klasifikator ispravlja uglove na sferi i vraća tačnost predikcije na čistu jedinicu.
krv nije voda i biologija ne laže jer u tebi spavaju i naučnik i vojnik.
"""

def očisti_i_tokenizuj(tekst):
    tekst = tekst.lower().strip()
    reči = re.findall(r"\b\w+\b", tekst)
    return reči

# Algoritam za masovno učenje veza između reči
reči = očisti_i_tokenizuj(veliki_tekst)
for i in range(len(reči) - 1):
    trenutna_reč = reči[i]
    sledeća_reč = reči[i+1]
    
    if trenutna_reč not in mozak:
        mozak[trenutna_reč] = {}
    if sledeća_reč not in mozak[trenutna_reč]:
        mozak[trenutna_reč][sledeća_reč] = 0
    mozak[trenutna_reč][sledeća_reč] += 1

# Čuvanje proširenog mozga u JSON
with open(putanja_mozga, "w", encoding="utf-8") as f:
    json.dump(mozak, f, ensure_ascii=False, indent=4)

print(f"✅ USPEH: Tvoj AI je upravo progutao i naučio {len(reči)} reči i smislenih veza!")
print("Sada pokreni ponovo mini_llm.py (ili real_learning_llm.py) i testiraj ga!")
