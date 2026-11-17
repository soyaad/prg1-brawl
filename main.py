import random

spelare_hp = 100
fiende_hp = 200

Name = input("vad är ditt namn? :")

print (f"Hej {Name}, du har blivt utmanad av Grinchen för att du också vill själa julen men han vill vara den ÄNDA. ")


while True:
    print("\n1. Visa spel")
    print("2. Visa poäng")
    print("3. Avsluta")
    val = input("Välj: ")

    if val == "1" : 
        while fiende_hp > 0 and spelare_hp > 0:
            spelar_skada = random.randint(20, 25)
            fiende_skada = random.randint(10, 20)

            fiende_hp -= spelar_skada
            print(f"{Name} attackerar Grinchen med sina knytnävar som gör {spelar_skada}")
            print(f"Grinchens Hp {fiende_hp}")

            spelare_hp -= fiende_skada
            print(f"Grinchen attackerar {Name} med en AK-47 som gör {fiende_skada}")
            print(f"{Name} {spelare_hp}")

    if spelare_hp > 0:
        print(f" {Name} slår Grinchen en sista gång innan han tillslut ger upp")
        print(f"Okej då! du får själa julen.. du är värdig. säger Grinchen med en irriterad röst")
    else:
        print(f" Grinchen sjuter {Name} rakt igenom huvudet med sin AK-47")
        print(f"jag sa ju att du inte var värdig säger Grinchen")

    

      
   




    



