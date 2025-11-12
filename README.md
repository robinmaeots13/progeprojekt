# progeprojekt
Autorid: Robin Mäeots ja Eduard Pavlov

Koostame programmi, mis võtab sisendiks kulud ja tulud, mille inimene on sisestanud ning see salvestatakse faili. Selle illustreerimiseks kasutame graafikuid, kuidas kulud ja tulud jaotuvad. Projekt aitab inimesel automatiseerida kulude ja sissetulekute jälgimist ning aru saada, mille peale raha peamiselt kulub. Valisime selle projekti, sest saame seda kasutada abivahendina tulevikus.

## Alfaversioon - 12.11.2025 seisuga

Programm võimaldab kasutajal sisestada oma kulud ja tulud ning salvestab need eraldi .txt-failidesse. Lisaks suudab programm importida konto väljavõtteid neljast Eestis levinud pangast .csv-vormingus. .csv failist lugemine annab kolm väljundit:
- valitud ajavahemiku **kulude summa**,
- **tulude summa**,
- **nimekiri ennikutest** kujul (kuupäev, absoluutne summa, C/D), kus C/D näitab, kas kanne on kreedit või deebet.

**Järgmised sammud:**

- Ühtlustada käsitsi sisestatud ja .csv-dest imporditud kanded ning kirjutada need ühtsesse faili ühetaolises formaadis (nt üks rida = üks kanne).
- Kasutada seda ühtlustatud faili edasistes tööetappides sisendina.
- Lisada visualiseeringud matplotlibiga:
  - Tulpdiagramm (bar chart) kulude ja tulude võrdlemiseks valitud perioodis.
  - Joondiagramm (line chart) saldo muutuse kuvamiseks kuu jooksul.
