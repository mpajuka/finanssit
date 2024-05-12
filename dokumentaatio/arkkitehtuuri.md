# Arkkitehtuuri
## Luokkarakenne
```mermaid
classDiagram
    GUI --|> FinanceService
    FinanceService --|> ProfileRepository
    FinanceService --|> UserRepository
    FinanceService --|> TransactionRepository
    UserRepository --|> User
    ProfileRepository --|> Profile
    TransactionRepository --|> Transaction
    
    Profile -- FinanceService
    User "1" -- "*" Profile
    Profile "1" -- "*" Transaction
    FinanceService "0..1" -- "1..n" User

    class User {
        +String name
        -String password
    }
    class Profile {
        +String name
        +int username
        +int user_id
    }
    class Transaction {
        +String name
        +int amount
        +Profile profile
        +int id
    }
```
## Tietojen tallennus
Tiedot tallennetaan omiin tietokantatauluihin sqlite-tietokantaan.
Tilitapahtuman noudattaa rakennetta:
```
Tilitapahtuma:
    <tunniste>
    <nimi>
    <määrä>
    <tyyppi>
    <päivämäärä>
    <profiilitunniste>
```

## Pääasialliset toiminnallisuudet

### Käyttäjän luonti ja kirjautuminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Login
  participant Register
  participant FinanceService
  participant UserRepository
  UI->>Login: 
  User->>Login: click "Register view" 
  Login->>Register: 
  Register->>FinanceService: register("kayttaja", "salasana")
  FinanceService->>UserRepository: create_new_user("kayttaja", "salasana")
  UserRepository-->>FinanceService: User
  FinanceService-->>Register: User
  User->>Register: click "Return to login"
  UI->>Login: 
  User->>Login: click "Log in"
  Login->>FinanceService: login("kayttaja", "salasana")
  FinanceService->>UserRepository: find_username("kayttaja")
  UserRepository->>FinanceService: User
  UI->UI: _handle_account_view()
```
Käyttäjä syöttää haluamansa käyttäjänimi-salasana parin, jonka arvot välitetään FinanceService käsittelijälle joka välittää nämä eteenpäin UserRepository-luokkaan, joka suorittaa tarvittavat tietokantaoperaatiot.
Vastaavassa luokassa `login()`-funktio käsittelee käyttäjänimi-salasana parin ja palauttaa istunnolle `User`-instanssin.

### Profiilin avaus ja tilitapahtuman luonti
```mermaid
sequenceDiagram
actor User
  participant UI
  participant Account
  participant Profile
  participant FinanceService
  participant ProfileRepository
  participant TransactionRepository
UI->>Account: 
User->>Account: input profile name and click "create profile"
Account->>FinanceService: create_profile("profile", "kayttaja")
FinanceService->>ProfileRepository: create_new_profile(Profile("profile", "kayttaja"))
ProfileRepository->>Account: Profile
User->>Account: doubleclick the created profile 
UI->>Profile: 
User->>Profile: click "create new transaction", input name, amount, date and transaction type
Profile->>FinanceService: create_transaction("name", "amount", Profile("profile", "kayttaja"), "Expense", "yyyy-mm-dd")
FinanceService->>TransactionRepository: create_transaction(Transaction("name", "amount", Profile("profile", "kayttaja"), "Expense", "yyyy-mm-dd")): 
TransactionRepository->>Profile: new_transaction 
UI->>UI: refresh_transactions()
```
Käyttäjän syötettyä tarvittavat arvot välittää `FinanceService`-luokka ne eteenpäin `TransactionRepository`-luokalle joka suorittaa tilitapahtuman lisäykseen tietokantaoperaatiot, joka palauttaa tapahtuman. 
Palautetun tapahtuman tiedot päivitetään `refresh_transactions()`-funktion kautta graafiselle taulukko-komponentille.

### Muut toiminnot
Tapahtuman muokkaaminen etenee pääasiallisesti samantapaisesti tilitapahtuman lisäys, mutta annetuissa parametreissa välitetään olemassa olevan tilitapahtuman tunniste, tapahtuman poistaminen etenee myös välittämällä tämä tunniste.

Sijoitustuottolaskurin käyttö perustuu liukuvalitsimien arvoihin, jotka välitetään erilliselle `calculate_investments` funktiolle.