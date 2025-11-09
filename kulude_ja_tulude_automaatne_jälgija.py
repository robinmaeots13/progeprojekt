pank = input("Sisesta panga nimi: ")
csv_fail = input("Sisesta .csv faili nimi: ")

def kuva_kulud_tulud(pank, csv_fail):
    try:
        with open(csv_fail, 'r', encoding='utf-8') as fail:
            read_data = fail.readlines()
    except FileNotFoundError:
        print(f"Viga: Faili '{csv_fail}' ei leitud.")
        return

    if pank == "Luminor":
        kulud = 0.0
        tulud = 0.0

        for rida in read_data[1:]:  # Jäta vahele päis
            veerud = rida.strip().split(';')

            summa_str = veerud[6].replace('"', '').replace(',', '.').strip() # Teisenda koma punktiks ja eemalda jutumärgid

            try:
                summa = float(summa_str)
            except ValueError:
                print(f"Viga rea väärtuse teisendamisel: {veerud[6]}")
                continue  # jätab vahele rea, kui teisendamine ebaõnnestub

            if veerud[5] == 'D':
                kulud += abs(summa)
            else:
                tulud += summa

        print(f"Panga '{pank}' kulud: {kulud:.2f} EUR")
        print(f"Panga '{pank}' tulud: {tulud:.2f} EUR")

kuva_kulud_tulud(pank, csv_fail)