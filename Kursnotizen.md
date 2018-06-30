# Fragen:
x init.py
Jupyter
Django
lint 
test
anaconda
aws lambda
buffer
events -> threads
Benachrichtigungen

# Python:
pip3 install verwenden
Datei-Struktur
Dateiendung .py
Packages von .py-Dateien
Bibliotheken sind py-Dateien = Module
Pakete: Standard, gehostet von Python (pypi) nachinstallierbar, nicht gehostet
Projekt
alles ist ein Objekt
Python enhancement protocol (PEP 8): Einrückungstiefe ist definiert
Tupelvergleich möglich (a, b) < (c, d), analog nacheinander sortieren in Excel
Declaration Rechtsklick-> Go to oder Strg+B
Informationen über Bibliotheken mit google suche „python bib“
List Comprehension (Ausdruck for if)
Zeichenketten sind unveränderlich, daher geben Methoden immer neue Zeichenketten zurück
input(„Wort“)
list oder * zum Auslesen von Objekten
lambda Funktionen wie Hilfsarbeiter
Filterobjekt wird konsumiert analog einer Pipe
Kommentare: ‘‘‘‘‘‘
Stringformatierung: „%02i.%02i.%04i, %s“ % (var1, var2, var3, var4)
2 verschiedene Stream: Standardausgabe und Fehlerausgabe
Modulcode, der als Modul nicht ausgeführt werden soll: if __name__==„__main__“
Vererbung zur Wiederverwendung von Modulen
Private Variable: _var (Konvention)
Globale Variablen, Modul-Variablen, Private Variablen
nicht das Tool für grafische Darstellung
Auf Server Modul ausführen durch Aufruf
Persiszenz: pickle
Fehler nicht mit if, sondern mit try except ERROR pass abfangen
magische Methoden: werden implizit von Python aufgerufen
Generatoren: Funktionen mit Schleifen, die über yield jeweils das nächste Element zurückgeben, „merken sich die vorige Zahl“
Iteratoren: Funktionen, die mit next jeweils ein weiteres Element ausgeben, „merken sich nicht die vorige Zahl“
Generator eher mit for-Schleife; while-Schleife mit Exception abfangen
Python kann mit großen Zahlen rechnen
genauer als Fliesskommazahlen: NumPy, Teil von SciPy-Package
def fkt(a, b, **kwargs): Keywordarguments = zusätzliche Argumente, die ich der Fkt übergeben kann und nutze kwargs[0]
Aufruf: fkt(a, b, c=x)

# Allgemein:
Syntaxfehler, Laufzeitfehler, Semantikfehler
Funktion wie Frage oder Aufforderung
Variablen wie Etiketten, Zuweisungen von rechts lesen
Listen mit Plural bezeichnen
Tupel ist Nur-Leseliste, unveränderbar
Hashtable, dictionary 
Boolean: True, False
Autovervollständigung mit Tab
Frage: Hat das vorher schon mal jemand entwickelt?ü
Möglichst auf bestehenden Ansatz zurückgreifen
Brüche im Binärsystem manchmal nicht abbrechend im Gegensatz zum Dezimalsystem
Fehler-Ansätze: 
1 = LBYL = Look Before You Leap, 
2 = EAFP = Easier Ask for Forgiveness than for Permission
Gute Verfahren kombinieren Algorithmen und Datenstruktukturen
Hashing bei Wörterbüchern: Aus Schlüsseln eine Zahl bilden (schnell, da konstante Zeit)
Datenbank: Baum entlanglaufen, daher logarithmische Zeit
Ablaufdiagramm: Start, Stop = Kreis, Operation im Rechteck, Frage oder Prüfung in Raute mit x Abzweigungen
Rekursive vs. iterative Ansätze
Reflection zur Laufzeit auf die Objekteigenschaften zugreifen, z.B. bei Implementierung von Serializierung
GUI: Steuerelemente zusammenstellen, benennen und Eigenschafte anpassen, Python TkInter (alt, aber Standard), PAGE, Gtk(Glade), PyQt (gut!), Alternative: ThinClient


# Tipps:
PyCharm 2017.3.4
Pythontutor.com: Quellcode visualisieren
python builtins = eingebaute Funktionen, oft für verschiedene Datentypen
Methoden: Objekt.Methode
__magischeMethoden__
codeacademy
Beim Lernen mit den Beispielen anfangen
Erst verwenden und dann importieren möglich
import name und dann unter name. schauen, welche Methoden es gibt
exercism.io: Übungen, mir Möglichkeit der Lösungsüberprüfung durch Test-Verifier (Unit-Test)
Bei Übernahme vorbereiteter Beispiele zunächst sicherstellen, dass auch die verwendete Python-Versione unterstützt wird
Bei guten Entwicklungsumgebungen initiiert das from lib import-Statement einen pip-Install
google fiance client
Excel-Dateien mit Bibliorhek pandas auslesen
Viele Ausgaben geben Objekte aus, von denen man noch die richtigen Attribute finden muss (z.B. value)
virtual environments zum parallelen Betreiben verschiedener Versionen
Für fast alles gibt es Funktionen, beachten, ob die Dinge geschickt, natürlich, intuitiv gelöst sind
Cross-Plattform für Python
Email: Mailinator, kinja, turboSMTP, temporäre Email-Adresse mit Google suchen
SMS: Relay-SMS
Zufall einsetzen, gibt manchmal falsches Ergebnis, oft nur in eine Richtung eindeutig
uploadfiles.io
https://ufile.io/4x58k

# Shortcuts:
Strg+Shift+F10 = Ausführen
Strg+Leerzeichen = Methodensignatur anzeigen
Universität von Paderborn
