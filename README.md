# Series Cleaner

## installation

`git clone git@github.com:hadzne/series_cleaner  `
`cd series_cleaner  `

in your virtual environment

`pip3 install -r requirements.txt`

## running
tested on linux only
`python3 series_cleaner.py -n 'YOUR PATH TO FOLDER CONTAINING FILMS'`

## wstępna instrukcja
Zakładam, że mamy przerobić katalog pliki do testowania
mamy przerobić każdy z plików .tx, który ma w nazwie wzorzec SXEY (X i Y to jedna lub dwie cyfry) pod warunkiem, że istnieje odpowiedni plik multimedialny (.avi, .mkv,.ts) ale nie istnieje odpowiedni plik .txt
odpowiedni oznacza, że ma w nazwie taki sam wzorzec SXEY

S01E01.Poldové a nemluvně1_13 - Malorážka.tx  - tak i wynik zapisać do S01E01.Poldové a nemluvně1_13 - Malorážka.txt
S01E02.Poldové a nemluvně2_13 - Chrastítko.tx	- tak i wynik zapisać do S01E02.Poldové a nemluvně2_13 - Chrastítko.txt
S01E03.Poldové a nemluvně3_13 - Miláček.tx 	- nie bo nie ma pliku z filmem
S01E04.Poldové a nemluvně4_13 - Dort.tx		- nie bo nie ma pliku z filmem
S01E04.Poldové a nemluvně4_13 - Dort.txt	- nie bo nie ma pliku z filmem
S01E05.Poldové a nemluvně5_13 - Michalova smrt.tx	- nie bo nie ma pliku z filmem
S01E06.Poldové a nemluvně6_13 - Svatopluk Ocásek.tx - nie bo istnieje juz Poldové a nemluvně6_13 S01E06- Svatopluk Ocásek.txt
S01E07.Poldové a nemluvně7_13 - Ema.tx	- tak i wynik zapisać do Poldové a nemluvně7_13 - EmaS01E07.txt
S01E08.Poldové a nemluvně8_13 - Vdovská metoda.tx	- nie
S01E09.Poldové a nemluvně9_13 - Noc s háčkem.tx		 - nie
S01E10.Poldové a nemluvně10_13 - Únos jako řemen.tx	- nie
S01E11.Poldové a nemluvně11_13 - Čumáček to zařídí.tx 	- nie
S01E12.tx - tak tak i wynik zapisać do S01E12.Poldové a nemluvně12_13 - Evina nevina.txt
S01E13.Poldové a nemluvně.tx  - tak tak i wynik zapisać do Poldové a nemluvně13_13 - Tři královéS01E13.txt


jak przerabiamy .tx ?
Zaczynamy od pierwszej linijki zawierajkącej znacznik czasowy np. 00:00:47
i cały tekst nastepujący po tej linijce idzie za tym znacznikiem aż do następnego znacznika 
Na przykładL
    Titulky

Poldové a nemluvně - Tři králové

    00:00:45
    PLÁČ DÍTĚTE
    -A nakonec, nakonec...
    00:00:49
    Ale, Eli, nakonec Ježíšek
    přiletí dovnitř oknem, hm?
    00:00:54
    Čímž se překvapivě
    nedopustí ani trestného činu

Przerabiamy na 
00:00:45  PLÁČ DÍTĚTE -A nakonec, nakonec...
00:00:49  Ale, Eli, nakonec Ježíšek přiletí dovnitř oknem, hm?
00:00:54  Čímž se překvapivě nedopustí ani trestného činu

Wojciech Stanek