
import random

spelare_hp = 100
fiende_hp = 125

spelare_wins = 0
fiende_wins = 0
spelare_losses = 0
fiende_losses = 0

Name = input("vad är ditt namn? :")

print(f"Hej {Name}, du har blivt utmanad av Grinchen för att du också vill själa julen men han vill vara den ÄNDA.")

while True:
    print("\n1. Spela")
    print("2. Visa poäng")
    print("3. Avsluta")
    val = input("Välj: ")

    if val == "1":
        spelare_hp = 100
        fiende_hp = 125
        while fiende_hp > 0 and spelare_hp > 0:
            spelar_skada = random.randint(10, 25)
            fiende_skada = random.randint(10, 20)

            fiende_hp -= spelar_skada
            print(f"{Name} attackerar Grinchen med sina knytnävar som gör {spelar_skada}")
            print(f"Grinchens Hp {max(0, fiende_hp)}")

            if fiende_hp > 0:
                spelare_hp -= fiende_skada
                print(f"Grinchen attackerar {Name} med en attack som gör {fiende_skada}")
                print(f"{Name} {max(0, spelare_hp)}")

        if spelare_hp > 0:
            print(f"{Name} slår Grinchen en sista gång innan han tillslut ger upp")
            print("Okej då!, du får själa julen.. du är värdig. säger Grinchen")
            spelare_wins += 1
            fiende_losses += 1
        else:
            print(f"Grinchen sjuter {Name} en sista gång.")
            print("Jag sa ju att du inte var värdig säger Grinchen")
            fiende_wins += 1
            spelare_losses += 1

    elif val == "2":
        print(f"{Name} har vunnit: {spelare_wins} gånger och förlorat: {spelare_losses} gånger")
        print(f"Grinchen har vunnit: {fiende_wins} gånger och förlorat: {fiende_losses} gånger")

    elif val == "3":
        print("Asså du kan ju inte bara ge upp, men okej.")
        break

    else:
        print("Ogiltigt val.")


    

      
   




    



