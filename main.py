import random

spelare_hp = 100
fiende_hp = 200

Name = input("vad är ditt namn? :")

print (f"Hej {Name}, du har blivt utmanad av Grinchen för att du också vill själa julen men han vill vara den ÄNDA. ")

while fiende_hp > 0 or spelare_hp > 0:
    
    spelar_skada = random.randint(25,30)
    fiende_skada = random.randint(10,20)

    fiende_hp -= spelar_skada
    print(f"{Name} attackerar Grinchen med sina knytnävar som gör {spelar_skada}")
    print(f"Grinchens Hp {fiende_hp}")

    spelare_hp -= fiende_skada
    print(f"Grinchen attackerar {Name} med en AK-47 som gör {fiende_skada}")
    print(f"{Name} {spelare_hp}")
   
      
   


