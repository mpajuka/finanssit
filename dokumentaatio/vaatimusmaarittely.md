# Vaatimusmäärittely

## Sovelluksen tarkoitus

_Finanssit_-sovellus mahdollistaa käyttäjän seurata tarkemmin omia tulo ja menovirtojaan. Sovelluksen käyttö pohjautuu käyttäjän luomiseen ja tämän lisäämiin profiileihin, johon kirjatut tulot ja menot yksilöidään. Tilitapahtumasyötteiden avulla on mahdollista tarkastella lisättyjä tilitapahtumia kokonaisvarojen osalta, sekä taulukosta joka sisältää yksityiskohdat lisätyistä tilitapahtumista.


## Toiminnallisuudet

### Alkunäkymä
Käyttäjä voi
- kirjautua hänen luomillaan tunnuksilla omalle tililleen.
- luoda itsellensä käyttäjätunnuksen, jos tällaista ei vielä hänellä ole.
    - Käyttäjätunnuksen on oltava uniikki ja salasanassa on oltava yhteensä vähintään 8 merkkiä, näistä ainakin 1 numero ja 1 erikoismerkki

### Profiilin valintanäkymä
- Käyttäjän kirjauduttua sisään voi valita tai lisätä uuden profiilin

### Profiilinäkymä
Käyttäjän valittua profiilin
-  on mahdollista tarkastella taulukkoa aiemmin lisätyistä tapahtumista ja lisäksi havaita sen hetkisen profiilin nettovarat, sekä lisäksi järjestämään taulukon sarakkeiden perusteella.  
- on mahdollista 
    - lisätä tapahtumia menoista tai tuloista sekä kirjata niiden yksityiskohtia
    - poistaa tai muokata tapahtumia
- on mahdollista hyödyntää sijoitustuottolaskuria, josta voi esimerkiksi havaita mitä ylimääräiset tulot tuottaisivat osakemarkkinoilla

## Lisäkehitysideoita

- Tulo- ja menotapahtumien merkitseminen toistuvaksi, ja tämän informaation avulla hyödynnettävä ennakointi 
- Vienti esimerkiksi `.csv` ja/tai `.pdf` tiedostoihin
- Menokategoriat ja kuhunkin luokkaan kuuluvien tapahtumien tarkastelu erillisestä näkymästä
