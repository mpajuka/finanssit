```mermaid
sequenceDiagram
    

    main->>laitehallinto: HKLLaitehallinto()
    laitehallinto-->>main: 

    main->>rautatietori: Lataajalaite()
    rautatietori-->>main: 
    main->>ratikka6: Lukijalaite()
    ratikka6-->>main: 
    main->>bussi244: Lukijalaite()
    bussi244-->>main: 


    main->>laitehallinto: lisaa_lataaja(rautatietori)
    laitehallinto-->>main: 

    main->>laitehallinto: lisaa_lukija(ratikka6)
    laitehallinto-->>main: 

    main->>laitehallinto: lisaa_lukija(bussi244)
    laitehallinto-->>main: 
 
    main->>lippu_luukku: Kioski()
    lippu_luukku-->>main: 

    
    main->>lippu_luukku: osta_matkakortti("Kalle")

    lippu_luukku->>uusi_kortti: Matkakortti("Kalle")
    uusi_kortti-->>kallen_kortti: 
    kallen_kortti-->>main: Matkakortti("Kalle", 0, 0, 0)

  
    main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
    rautatietori->>kallen_kortti: kasvata_arvoa(3)
    kallen_kortti-->>main: 

    main->>ratikka6: osta_lippu(kallen_kortti, 0)
    ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
    kallen_kortti-->>ratikka6: 
    ratikka6-->>main: True 


    main->>bussi244: osta_lippu(kallen_kortti, 2)
    bussi244->>kallen_kortti: vahenna_arvoa(3.5)
    kallen_kortti-->>bussi244: 
    bussi244-->>main: True

    
```