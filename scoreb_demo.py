import json

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
scoreboard(int(input()))