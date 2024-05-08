# Arkkitehtuuri

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
        +int owner_id
    }
    class Transaction {
        +String name
        +int amount
        +Profile profile
        +int id
    }
```
