# import files such as random, countries and capitals and ascii arts
import random
import json
from contry_and_capital_list import countries_and_capitals
from ascii import HANGMANPICS

# error counter méretének megadása
MAX_ERRORS = len(HANGMANPICS) - 1

import json

# scoreboard hozzáadása
def scoreboard(score):
    try:
        with open("scoreboard.json", "r") as f:
            list = json.load(f)
    except:
        list=[]
    print("\n" + "="*10 + "HIGH SCORE" + "="*10)
    print("="*30)
    print(f"{'Rank':<5} {'Name':<12} {'Score':<10}")
    print("-" * 30)
    for i in range(len(list[:10])):
        Name=list[i]["name"]
        Score=list[i]["score"]
        print(f"{i+1:<5} {Name:<12} {Score:<10}")
    print("="*30)
    if len(list)>=10 and score<list[9]["score"] or len(list)<10:
        print(f"Gratulálok! Csupán {score} tippre volt szükséged, amivel bebiztosítottad a helyed a Top 10-ben!")
        adat=str(input("Adj meg egy nevet vagy nyomj Entert:")).strip()
        if adat!="":
            list.append({"name":adat, "score":score})
            list.sort(key=lambda x: x["score"],)
            with open ("scoreboard.json","w") as f:
                json.dump(list, f, indent=4,)
    print(f"{score} tipp kellett, ezzel a neved maximum fejfára kerül")

# country and capital felbontása és random kiválasztása
def pick_random_pair():
    orszag = []
    capital = [] 
    for i in countries_and_capitals():
        x, y = i.strip().split("|")
        x=x.lstrip()
        y=y.lstrip()
        orszag.append(x)
        capital.append(y)
    ran_country= random.randint(0, (len(orszag)))
    ran_capital= random.randint(0, (len(capital)))
    return orszag[ran_country], capital[ran_capital]
# hiddenbe konvertálás
def mask_word(word, guessed):
    return "".join(ch if ch.lower() in guessed or ch == " " else "-" for ch in word)

# egy körnek a megfogalmazása
def play_one_round(secret_word, label): #secret word         
    guessed = set() # egy elem csak 1x szerepelhet benne, elmenti a már kérdezett betűket
    errors = 0
    score = 0

    while errors < MAX_ERRORS: # ha a hibák elérik a max errorst eltörik
        print("\n" + HANGMANPICS[errors])
        print(f"{label}: {mask_word(secret_word, guessed)}")
        print(f"Hibás betűk: {' '.join(sorted(guessed - set(secret_word.lower())))}")
        print(f"Maradt próbálkozás: {MAX_ERRORS - errors}")

        guess = input("Adj meg egy betűt: ").strip().lower() # több betűt nem fogad el
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Érvénytelen! - Csak egy betűt írj.")
            continue

        if guess in guessed:    # nem lehet egy betűt többször tippelni
            print("Már tippelted ezt a betűt.") 
            continue
        score=score+1
        guessed.add(guess)

        if guess in secret_word.lower():
            if all(ch.lower() in guessed or ch == " " for ch in secret_word):
                print(f"\nGratulálok! Kitaláltad a(z) {label.lower()}: {secret_word}")
                
                scoreboard(score)
                return True
        else:
            errors += 1
            print("Rossz betű!")
        

    print("\n" + HANGMANPICS[errors])
    print(f"Sajnos elvesztetted a játékot. A helyes {label.lower()}: {secret_word}")
    return False
 
 #a játék alapelvei
def main():
    print("Üdvözöllek a játékban!")
    while True:
        print("\nMit szeretnél kitalálni?") 
        print("[1] Ország")
        print("[2] Főváros")
        print("[Enter] Kilépés")
        choice = input().strip()

        if choice == "":
            break
        if choice not in {"1", "2"}:
            print("Érvénytelen választás.") # csak az 1-t és 2-t fogadja el válaszként
            continue

        ran_country, ran_capital = pick_random_pair()

        if choice == "1":
            play_one_round(ran_country, "Ország")
        else:
            play_one_round(ran_capital, "Főváros")

        again = input("\nJátszunk még egy körrel? (i/n): ").strip().lower()
        if again != "i":
            break

    print("\nKöszönjük a játékot!")

# replaying function
if __name__ == "__main__":
    main()                   