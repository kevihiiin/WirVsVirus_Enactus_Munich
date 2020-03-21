 # WirVsVirus

Github Repo für die Winner?;)



## Setup

Am besten PyCharm *Professional* benutzen, das hat besseren Django support und hat ein eigenes Django tools um die Funktionen zu managen

Repository Clonen (SSH oder HTTPS)

```bash
git clone git@github.com:manoletre99/WirVsVirus_Enactus_Munich.git
cd WirVsVirus_Enactus_Munich
```

Virtual environment erstellen (bitte genau so nennen, sonnst wird das mit hochgeladen)
Alternativ kann das auch in PyCharm erstellt werden, so isses aber einfacher:P

```bash
python3 -m venv env  
# Activate environment
source env/bin/activate
# Install all requirements
pip install -r requirements/development.txt
```

PyCharm 

1. Projekt importieren -> Projekt importieren

2. Datenbank migrieren (ist eine lokale SQLite für development, in production automatisch MariaDB oder MySQL oder PostgreSQL, etc)

   ```bash
   # Kommandozeile (achte auf die geladene environment, am besten im PyCharm terminal laufen lassen)
   python manage.py migrate
   
   # Oder (bevorzugt) direkt über PyCharm: Tools -> Run manage.py Task... [Gibts nur in PyCharm Professional]
   migrate
   ```

3. Django Server laufen lassen (in PyCharm oben rechts auf run), Website besuchen unter http://127.0.0.1:8000/

4. Sollte keine Fehlermeldung anzeigen

## Projektstruktur

Am besten hier nachlesen: https://django-project-skeleton.readthedocs.io/en/latest/index.html

Kommentare zu Django:

**Datenbank**

+ Wenn wir eine Datenbank ansprechen um etwa Sachen zu speichern, machen wir das in Django nicht direkt über SQL, sondern über eigene sogenannte "models". Das sind Objekte in Python (Klassen) mit Attribute. Heißt eine Klasse entspricht einer Tabelle in der Datenbank und eine Instanz, ein Objekt konkret enspricht einer Zeile. Die Attribute des Objekts / der Instanz sind die Spalten in der Tabelle. Dadurch können wir das Backend der Datenbank ganz easy austauschen. 
  Die Models beschreiben also die Datenbank, wir müssen nie eine Zeile SQL schreiben
+ Jeden mal wenn wir eine Änderung an der DB Struktur vornehmen, also wenn wir das "models.py" File ändern, müssen wir die Datenbankstruktur ändern. Das muss manuell angestoßen werden. Zuerst "migrationen erstellen [makemigrations]" und dann anwenden [migrate]
+ Wir könnnen auch in Django Filtern und Queries erstellen

**Templates**

+ Django benutzt standartmäßig die "Jinja2" Templating Sprache. Was heißt das? Die Templates sind im Prinzip ganz normaler HTML Code, jedoch erweitert mit Platzhaltern, die Django für uns füllt. Diese Werden Signalisiert mit {% %} oder { }. Damit können wir if/else statements einbauen oder Variablen dynmaisch ausfüllen lassen, sehr praktisch
+ Alle Templates zu einer Seite befinden sich im Template Ordner
+ Wir können aber auch ganz auf die Templates pfeifen und nur Django als Backend verwenden, und z.B. React als Frontend. Dann Django und React über die REST Api kommunizieren lassen.

