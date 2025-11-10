with open("tulud.txt", "w", encoding="UTF-8") as fail:
    while True:
        tulud = input("Sisesta sissetulekud (allikas - summa eurodes): ").strip().lower()
        if tulud == "":
            break
        fail.write(tulud + "\n")

with open("kulud.txt", "w", encoding="UTF-8") as fail:
    while True:
        kulud = input("Sisesta kulutused (kulu - summa eurodes): ").strip().lower()
        if kulud == "":
            break
        fail.write(kulud + "\n")
        
with open("tulud.txt") as fail:
    tulude_järjend = []
    for rida in fail:
        osad = rida.split(" - ")
        osad[1:] = list(map(int, osad[1:]))
        tulude_järjend.append(osad)
        tulud_kokku = 0
        for i in range(len(tulude_järjend)):
            tulud_kokku += tulude_järjend[i][1]
    print(f"Tulusid on kuu jooksul kokku {tulud_kokku} eurot.")

with open("kulud.txt") as fail:
    kulude_järjend = []
    for rida in fail:
        osad = rida.split(" - ")
        osad[1:] = list(map(int, osad[1:]))
        kulude_järjend.append(osad)
        kulud_kokku = 0
        for i in range(len(kulude_järjend)):
            kulud_kokku += kulude_järjend[i][1]
    print(f"Kulusid on kuu jooksul kokku {kulud_kokku} eurot.")

raha_üle = tulud_kokku - kulud_kokku
print(f"Raha jäi kuu jooksul üle {raha_üle} eurot.")
