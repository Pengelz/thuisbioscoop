# thuisbioscoop
Hoe gaat de app eruit zien?

Aanbieders en gebruiker moeten gescheiden zijn. Dit gebeurd door aanbieders een aparte inlognaam en wachtwoord te geven.
Begint met een inlogscherm. Bezoekers kunnen registreren met hun naam en emailadres. Dit wordt opgeslagen in een csv.bestand. 
Deze gebruiker krijgt dan de films te zien van vandaag en morgen met alle informatie erbij. Gebruiker selecteert de film en krijgt hierbij een unieke code (ticket) Extra opdracht dit koppelen aan een QR-Code.
Aanbieders toewijzen aan de film. Een aanbieder per film. Als er een aanbieder inlogt moet deze alle gasten van de dag zien. Ook kan hij alle films vertonen en sorteren. Aanbieders mogen alleen hun eigen gasten zien. 

Gebruikers oogpunt:

1.	Programma weergeeft inlog scherm van thuisbioscoop. Hierin kan email + wachtwoord worden ingevoerd om in te loggen.
2.	Gebruiker kan registeren. Naam en emailadres word in de csv database geplaatst.
3.	Gebruikers logt in met email en password en word doorverwezen naar film pagina.
4.	Gebruiker ziet alle films vandaag morgen. Elke film heeft een titel en een aanbieder. Een aanbieder kan meerdere films vertonen. Een film kan alleen op een locatie tegelijk worden vertoond.
5.	Gebruiker kan op een film naam klikken en daarbij word informatie per film weergegeven. Filmrating, duur en korte beschrijving word weergegeven.
6.	Gebruiker besteld een film en krijgt hierbij een unieke gegenereerde code
7.	Unieke code wordt opgeslagen in de database bij de gebruiker.
8.	Unieke code word omgezet in een qr code in python.
9.	Gebruiker kan zien welke film hij of zij heeft uitgekozen en de qr code word erbij weergegeven.



Aanbieders oogpunt:
1.	Programma weergeeft inlog scherm van thuisbioscoop. Hierin kan email + wachtwoord worden ingevoerd om in te loggen.
2.	Aanbieder logt in met zijn eigen email en wachtwoord. 
3.	Aanbieder ziet zijn films met alle informatie. 
4.	Aanbieder ziet per film ook al zijn eigen gebruikers van die dag. 
5.	Alle bezoekers worden gesorteerd op begintijd van de film en daarna op achternaam.  
