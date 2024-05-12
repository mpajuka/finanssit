# Käyttöohje

Lataa viimeisin [release](https://github.com/mpjk/finanssit/releases) projektista.

## Tietokantatallennus
Ohjelman alustessa määritetään automaattisesti tietokanta nimellä `db.sqlite`.
Voit kuitenkin halutessasi asettaa tietokannalle itsemääritetyn osoitteen projektin juureen tiedostoon `.env`, 
jonka sisältö tulisi olla seuraavanlainen:

```env
DB=<syötä tietokannan nimi>.sqlite
```

## Asennus
> [!IMPORTANT]
> Ohjelman suoritus vaatii vähintään Python 3.10 tai uudemman
> sekä riippuvuuksienhallinta ohjelman nimeltä `poetry`
> ([asennusohje](https://python-poetry.org/docs/#installation))
- Ympäristön riippuvuudet
```bash
poetry install
```
- Tietokannan alustaminen
```bash
poetry run invoke build
```
- Ohjelman käynnistäminen
```bash
poetry run invoke start
```

## Alkunäkymä

### Kirjautumisnäkymä
<img width="335" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/c7a1f230-6e3c-459c-a835-e1258915b8f8">

Vaihda alkunäkymä rekisteröintilomakkeeseen painikkeella `Register view`.

### Rekisteröintinäkymä
<img width="335" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/3957d817-4844-463f-b66f-a07b3377acad">

Syötettyäsi haluamasi käyttäjätunnus ja salasana, voit siirtyä takaisin
edelliselle kirjautumislomakkeelle painikkeella `Return to login`

### Profiilin luonti ja avaus

#### Alku

<img width="335" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/6f87a4c8-e596-4336-875f-2fb0493774af">

Syötä haluamasi profiilin nimi ja valitse `Create profile`

#### Profiilin luonti

<img width="335" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/805a643a-45ce-4d18-859f-4bf47f0a30dc">

Kirjauduttuasi sisään voit siirtyä eteenpäin luomalla itsellesi profiilin,
joka vastaa yksittäistä "tiliä", mihin lisäämäsi tilitapahtumat yksilöidään.

<img width="334" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/643f528c-d77f-4f7d-893a-f27378e2e5d0">

Profiiliin seuraavasta näkymästä siirrytään tuplaklikkaamalla lisätyn profiilin nimeä

## Profiilinäkymä

<img width="435" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/fc196af1-5962-4973-b979-dda504372add">

### Tilitapahtuman luominen

<img width="601" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/bcc8c3bf-f4c3-4723-8165-005fa0fd3513">

Painikkeella `add transaction` saat luotua tapahtuman lisäämistä varten tarvittavan
näkymän. Syötä tarvittavat arvot tilitapahtumalle. Tilitapahtuman nimi, sen euroarvoinen
suuruus, päivämäärä ja tyyppi. __Huomaathan että menotapahtuma kirjataan samalla tavalla kuin tulo.__
`Income` tai `Expense`-valitsin määrää etumerkin, joten menotapahtumalle ei ole tarpeellista lisätä `-` merkkiä

<img width="662" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/0a17fba4-de34-415a-95ae-be0c36659e71">

Lisättyäsi tapahtuman voit havaita sen päivittyneen profiilinäkymän taulukkoon.
> [!TIP]
> Kun tapahtumia on riittävän paljon, voit järjestää taulukon sarakkeen sisällön
> mukaisesti painamalla sarakkeen otsikkoa


### Tilitapahtuman poistaminen ja muokkaus

<img width="374" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/68d5b3b8-ede0-433a-b49d-607a9ad5f5fc">

Kaksoisklikkauksella voit avata tiedot tapahtumasta ja halutessasi muokata tapahtumaa

#### Muokkaus

<img width="298" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/965fcf6b-d0c3-49e0-a879-e6e44fe95417">

Tapahtuman muokkaaminen avaa samantapaisen näkymän kun luomisessa, tässä voit syöttää uudet tiedot
lisäämällesi tapahtumalle ilman että joudut erikseen poistamaan sitä ja luomaan uutta.
Syötä siis aiemman luonnin tapaisesti uudet tiedot.

#### Poisto

<img width="298" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/1abac09c-aed6-419e-8783-a4109a3f60aa">

Tilitapahtuman poistaminen tapahtuu hyvin suoraviivaisesti, valitessa `Remove transaction` avautuu
vahvistusikkuna josta voit halutessasi vahvistaa tai vielä perua poiston.
__Huomaathan että tilitapahtuman poisto on lopullinen eikä vahvistuksen jälkeen sitä voi enää perua.__


### Sijoitustuottolaskuri

<img width="836" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/4cd0d049-c8de-4608-ac4b-6dc89186004e">

Alkunäkymässä painikkeella  `Compound Interest Calculator` käynnistää sijoitustuottolaskurin.
Laskurissa pyydetään seuraavat tiedot:
1. Aloitussumma, jolla viitataan kertaluontoisesti sijotettavaan summaan.
2. Kuukausisäästösumma, eli kuukausittain sijoitettava summa
3. Odotettu tuotto, eli vuotuisella tasolla odotettu keskimääräinen tuottoprosentti
4. Aika jona varat ovat sijoitettuna alusta lukien.

Annetujen tietojen perusteella ohjelma muodostaa havainnollistavan kaavion

<img width="693" alt="image" src="https://github.com/mpjk/finanssit/assets/56785774/1f67f1a4-37b0-4e8f-88e1-f016d0a1f2a8">

Lisätietoja korkoa korolle-ilmiöstä ja sen laskemisesta esimerkiksi [täältä](https://fi.wikipedia.org/wiki/Korko#Korkoa_korolle)

#### Tärkeä huomio sijoitustuottolaskurin tuloksista
_Huomaathan että laskuri on puhtaasti viitteellinen, 
eikä ohjelman luoja vastaa tietojen oikeellisuudesta, eikä niistä mahdollisesti seuraavista vahingoista.
Muodostettu kaavio kuvastaa sijoitettavien varojen teoreettista kehitystä, eikä tätä voida käyttää sijoitusohjeena._

## Lopuksi
Kun olet suorittanut haluamiesi tapahtumien lisäyksen ovat ne tällöin tallentuneet tietokantaan, eikä erillistä tallennustoimenpidettä tarvita.
Voit palata myöhemmin profiiliisi kirjautumalla käyttämällesi tilille.

