# Vaatimusmäärittely

## Sovelluksen tarkoitus

_Finanssit_-sovellus mahdollistaa käyttäjän seurata tarkemmin omia tulo ja menovirtojaan. Sovelluksen käyttö pohjautuu käyttäjän luomiseen, johon kirjatut tulot ja menot yksilöidään. Näiden syötteiden perusteella muodostetusta raporttinäkymästä saa tarkemman kokonaiskuvan taloutensa tilasta, kuin pelkästään yksittäisiä tilitapahtumia katsomalla.

## Perusversion suunnitellut toiminnallisuudet

### Alkunäkymä

- Käyttäjä voi luoda itsellensä käyttäjätunnuksen, jos tällaista ei vielä hänellä ole.
    - Käyttäjätunnuksen on oltava uniikki ja salasanassa on oltava vähintään 8 merkkiä, 1 numero ja 1 erikoismerkki
- Käyttäjä voi kirjautua hänen luomillaan tunnuksilla omalle tililleen.

### Sovellusnäkymä

- Käyttäjän kirjauduttua sisään tulee vastaan _"at a glance"_-tyylinen näkymä mistä voi selkeästi havaita tiivistetysti käyttäjän talouden keskeisimmät tunnusluvut.
- Käyttäjä voi lisätä tapahtumia menoista tai tuloista sekä kirjata niiden yksityiskohtia
    - Tämä tapahtuu erillisessä näkymässä, jossa on myös mahdollisuus palata aiempiin tapahtumiin ja tutkia niiden lisätietoja.
- Käyttäjä voi myös tarvittaessa poistaa tapahtumia 

### Lisäkehitysideoita

- Sijoitustuottolaskuri, josta voi esimerkiksi havaita mitä ylimääräiset tulot tuottaisivat osakemarkkinoilla
- Tulo- ja menotapahtumien merkitseminen toistuvaksi, ja tämän informaation avulla hyödynnettävä ennakointi 
- Vienti esimerkiksi `.csv` ja/tai `.pdf` tiedostoihin
- Menokategoriat ja kuhunkin luokkaan kuuluvien tapahtumien tarkastelu erillisestä näkymästä
