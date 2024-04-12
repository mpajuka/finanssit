# Ohjelmistotekniikka, harjoitustyö

__Finanssit__, on _henkilökohtaisen talouden seurantasovellus_, missä voit seurata oman talouden kehitystä ja rakennetta.

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/mpajuka/finanssit/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/mpajuka/finanssit/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/mpajuka/finanssit/blob/main/dokumentaatio/changelog.md)

## Ohjelman käyttö
### Asennus
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

### Testien suorittaminen
```bash
poetry run invoke test
```

### Laatutarkistusten suorittaminen
```bash
poetry run invoke lint
```
