liste =["istanbul","Ankara","Sivas"]
for sehirler in liste:
    print(sehirler)


for sekıl in range(2,7):
    print("*"*sekıl)

for rakam in range(4):
    print("rakam:" + str(rakam))

for rakam in range(20):
    if rakam == 5:
         break
    print("rakam:" + str(rakam))



sayi = 1
sayac = 10
while sayi <6:
    if sayac == 3:
        break
    print(sayi)
    sayi += 1
