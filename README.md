## Nachtatem’s Recon Vault 🐉🏜️

Willkommen, Wanderer der Ödnis.
Dies ist dein kleines Toolkit von Nachtatem — dem alten Drachen, der die Datenruinen durchforstet.
Hier findest du eine Sammlung handlicher Python-Skripte für Recon-Aufgaben: Header-Grabber, Wordlist-Generator, Hash-Cracker, Passwort-Checks und weitere Tools. Alle Tools sind lern- und test-orientiert — nur gegen Systeme einsetzen, für die du eine Erlaubnis hast (z. B. HTB/THM-Labs oder eigene Testumgebungen).

## 🔧 Enthaltene Tools (Kurzüberblick)

Wordlist Generator (Wordlist-Generator/)
Generiert praxisnahe Passwortlisten (Zahlen, Sonderzeichen, Leetspeak, Case-Varianten).

Hash Cracker (Hash-Cracker/)
Dictionary-Attacke für MD5 / SHA1 / SHA256-Hashes.

Passwort-Prüfer (Passwort-Pruefer/)
Prüft Passwörter gegen lokale leaked.txt Dateien. (Bulk-Modus & Report)

HTTP Header Grabber (HTTP-Header-Grabber/)
Holt HTTP-Header einer Ziel-URL, markiert Sicherheitsheader und erstellt optional einen Report.

(geplant) Directory Brute Forcer, Login Simulation, Logfile Parser, Ping-Sweeper, CLI-Toolkit — Ausbau folgt.

## 🚀 Schnellstart

1.Repository klonen
git clone https://github.com/NarunaOdinsdottir/Recon-Mini-Toolkit.git
cd Recon-Mini-Toolkit

2.Virtuelle Umgebung (optional, empfohlen)
python3 -m venv .venv
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows
pip install -r requirements.txt   # falls vorhanden

3.Beispiel: Header Grabber
cd HTTP-Header-Grabber
python header_grabber.py
# URL eingeben (z.B. http://10.10.10.10)
# Optional Report speichern -> y/n

## 🧾 Anforderungen

Minimal (je nach Tool):

Python 3.8+

requests (für Web-Requests)

Optional: pynput (Keylogger, nur lokal zu Lernzwecken), pyautogui (Screenshots)

## ⚠️ Regeln & Ethik (WICHTIG)

Nachtatem ist weise — und streng:

Verwende diese Werkzeuge nur in genehmigten Testumgebungen (eigene Server, HTB/THM-Labs, CTFs).

Scans oder Brute-Force auf fremde Websites / Systeme ohne Erlaubnis sind illegal.

Diese Tools sind zu Lernzwecken gedacht. Verantwortung liegt bei dir.

## ✨ Stil & Flavor (Nachtatem-Hinweis)

Die Konsolen-Ausgaben sind bewusst thematisch (Fallout/Wasteland).

Du kannst Sprüche in den Skripts leicht erweitern — die Stimmung macht das Üben leichter.

Achtung: Humor ist stark — aber die Technik bleibt ernst.



Install:
