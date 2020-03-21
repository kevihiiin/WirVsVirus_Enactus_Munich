# Apps
## Was gehört hier rein?
Hier können verschiedene Anwendungen landen.
Z.B. Eine zum Abstimm-App, eine Admin Panel (wenn man die Django interne nicht benutzen möchte), eine Streaming App etc. 
Apps sind von Django Installation zu Django Installation übertragbar und meinstens sehr verschieden. Jede App kann (und hat im Normalfal)
mehrere Unterseiten. Unser Projekt wird vermutlich nur eine "App" haben.

## Wie erstelle ich eine neue App?
Dokumentation: https://docs.djangoproject.com/en/3.0/intro/tutorial01/#creating-the-polls-app

Oder kurz:
```shell script
# Erstelle neue App namens "polls"
# Kommandozeile (achte auf die geladene environment, am besten im PyCharm terminal laufen lassen)
python manage.py startapp polls

# Oder (bevorzugt) direkt über PyCharm: Tools -> Run manage.py Task... [Gibts nur in PyCharm Professional]
startapp poll
# Und dann noch in den apps Order verschieben
``` 
