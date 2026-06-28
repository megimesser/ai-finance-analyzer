### news - analyst

# requester.py
Ruft auf Basis des Systemprompts die aktuellen allgemeinen News aus den Finanzmätkten ab 

# sender.py
sendet die antwort.txt als Mail 


### portfolio - analyst 

# Importer.py 

Importiert die einzelnen Portfolio - Werte aus der finance.xlsx

# kurs.py

Ruft die Kursdaten für die Aktien und ETF´s auf Basis der Ticker aus der finance - Excel ab und speichert sie in finance.json

# merger.py

nimmt die Daten aus der finance.json und der finance.xlxs und verbindet sie 


# konverter.py 

verbindet Portfoliodaten mit dem vanilla-prompt für die weiterverarbeitung in einem Systemprompt

-> Hier müssen die Daten aus dem Request hinzugefügt werden !!!

# requester.py 

Sendet die verbundenen Prompts an die Claude - API 
und erstellt einen Report 



### conntroller - Multi-Agent-Review 

# requester.py

Einzelner Request welcher auf Basis des erhaltenen Prompts aus dem analyser die Antwort kritisch hinterfragt und eine zweite Risikoanalyse durchführt 
und anschließend einen Report mit Handlungsanweisungen erstellt 


### sender 

Sendet der Report per Mail heraus


----

# Daily Ticker 

überprüft auf Basis meines Portfolios die aktuellen Entwicklungen - in der Ausgabe wird als Json am Ende ein True für - wichtig oder ein False für - unwichtig mitgeliefert. 



# Twillio API 

Ein zweites Program filtert die Ausgabe und sendet die Daten als Mail und als Twillio - SMS falls wichtige Infos zu den Portfolios vorhanden sind 



# Fast API als Trigger für die Pipeline 



TODO : 

Fast API Trigger implementieren 

CI Pipeline Aufsetzen 

Komponenten fertig bauen 

Tests schreiben 
