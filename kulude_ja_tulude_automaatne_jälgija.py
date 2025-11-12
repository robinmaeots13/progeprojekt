# nimed ja mis teeb

from datetime import datetime

küsimus = input("Kas soovite oma kulud ja tulud kirjutada faili või pangast importida (kirjutada ise/importida)? ").strip().lower()

def kirjuta_ise(kirjuta_faili):
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
 
def kuva_kulud_tulud(pank, csv_fail):
    try:
        with open(csv_fail, 'r', encoding='utf-8') as fail:
            read_data = fail.readlines()
    except FileNotFoundError:
        print(f"Viga: Faili '{csv_fail}' ei leitud.")
        return

    if pank == "luminor": # Luminor CSV formaadi töötlemine
        kulud = 0.0
        tulud = 0.0
        sisend = []

        for rida in read_data[1:]:  # Jäta vahele päis
            veerud = rida.strip().split(';')

            if len(veerud) < 9: # Kontrolli, kas veerge on piisavalt. Kui ei, jätka järgmise reaga
                continue

            summa_str = veerud[6].replace('"', '').replace(',', '.').strip() # Teisenda koma punktiks ja eemalda jutumärgid

            try:
                summa = float(summa_str)
            except ValueError:
                print(f"Viga rea väärtuse teisendamisel: {veerud[6]}")
                continue  # jätab vahele rea, kui teisendamine ebaõnnestub
            
            kuupaev = datetime.strptime(veerud[2], "%d.%m.%Y").date() # Kuupäeva importimine csv failist
            sisend.append((kuupaev, summa, veerud[5])) # Lisa andmed sisendisse

            if veerud[5] == 'D':
                kulud += abs(summa)
            else:
                tulud += summa

        print(f"Panga '{pank}' kulud: {kulud:.2f} EUR")
        print(f"Panga '{pank}' tulud: {tulud:.2f} EUR")
        print(f"{sisend}")

    if pank == "lhv": # LHV panga CSV formaadi töötlemine
        kulud = 0.0
        tulud = 0.0

        for rida in read_data[1:]:  # Jäta vahele päis
            veerud = rida.strip().split(',')

            if len(veerud) < 9: # Kontrolli, kas veerge on piisavalt. Kui ei, jätka järgmise reaga
                continue

            summa = float(veerud[8])

            if veerud[7].strip('"') == "C":
                tulud += summa
            elif veerud[7].strip('"') == "D":
                kulud += abs(summa)

        print(f"Panga '{pank}' kulud: {kulud:.2f} EUR")
        print(f"Panga '{pank}' tulud: {tulud:.2f} EUR")

    if pank == "swedbank" or pank == 'swedpank' or pank == 'swed': # Swedbank panga CSV formaadi töötlemine
        kulud = 0.0
        tulud = 0.0

        for rida in read_data[1:-3]:  # Jäta vahele päis
            veerud = rida.strip().split(';')

            if len(veerud) < 9: # Kontrolli, kas veerge on piisavalt. Kui ei, jätka järgmise reaga
                continue

            summa_str = veerud[5].replace('"', '').replace(',', '.').strip() # Teisenda koma punktiks ja eemalda jutumärgid

            try:
                summa = float(summa_str)
            except ValueError:
                print(f"Viga rea väärtuse teisendamisel: {veerud[5]}")
                continue  # jätab vahele rea, kui teisendamine ebaõnnestub

            if veerud[7].strip('"') == "K":
                tulud += summa
            elif veerud[7].strip('"') == "D":
                kulud += abs(summa)

        print(f"Panga '{pank}' kulud: {kulud:.2f} EUR")
        print(f"Panga '{pank}' tulud: {tulud:.2f} EUR")

    if pank == "seb": # SEB CSV formaadi töötlemine
        kulud = 0.0
        tulud = 0.0

        for rida in read_data[1:]:  # Jäta vahele päis
            veerud = rida.strip().split(';')
            
            if len(veerud) < 9: # Kontrolli, kas veerge on piisavalt. Kui ei, jätka järgmise reaga
                continue

            summa_str = veerud[8].replace('"', '').replace(',', '.').strip() # Teisenda koma punktiks ja eemalda jutumärgid

            try:
                summa = float(summa_str)
            except ValueError:
                print(f"Viga rea väärtuse teisendamisel: {veerud[8]}")
                continue  # jätab vahele rea, kui teisendamine ebaõnnestub

            if veerud[7].strip('"') == "C":
                tulud += summa
            elif veerud[7].strip('"') == "D":
                kulud += abs(summa)

        print(f"Panga '{pank}' kulud: {kulud:.2f} EUR")
        print(f"Panga '{pank}' tulud: {tulud:.2f} EUR")
        
if küsimus == 'importida':
    pank = input("Sisesta panga nimi: ").strip().lower()
    csv_fail = input("Sisesta .csv faili nimi: ")
    kuva_kulud_tulud(pank, csv_fail)
else:
    kirjuta_ise(küsimus)