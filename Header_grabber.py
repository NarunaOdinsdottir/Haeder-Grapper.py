#!/usr/bin/env python3
# header_grabber.py
import requests
import random
import datetime

vault_quotes = [
    "🛠️ Nachtatem scannt die Leitungen der Vault…",
    "⚡ Sicherheitsprotokolle prüfen…",
    "💀 Alte Server-Geister werden geweckt…",
    "🔥 Ein digitales Geheimnis wird gelüftet…",
    "🦖 Selbst ein Raider hätte Respekt vor diesen Headern!"
]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "curl/7.88.1"
]

# Welche Header zählen wir als "Sicherheitsheader"
highlight_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "Server",
    "Set-Cookie",
]

def format_line(key, value, highlight=False):
    if highlight:
        return f"{key}: {value} "
    return f"{key}: {value}"

def run_scan(url, save_report=False):
    print(random.choice(vault_quotes))
    headers = {"User-Agent": random.choice(user_agents)}
    start = datetime.datetime.now()
    try:
        resp = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
    except requests.exceptions.RequestException as e:
        print(f"💀 Fehler beim Abrufen der URL: {e}")
        return

    print(f"\n🔍 HTTP-Header für {url} (Status: {resp.status_code})")
    print("="*60)

    found_security_headers = 0
    for key, value in resp.headers.items():
        if key in highlight_headers:
            print(format_line(key, value, highlight=True))
            found_security_headers += 1
        else:
            print(format_line(key, value))

    # Security-Report
    print("\n Vault-Sicherheitsreport:")
    print(f"Gefundene Sicherheitsheader: {found_security_headers} / {len(highlight_headers)}")
    if found_security_headers == len(highlight_headers):
        print("✅ Vault gut gesichert! Keine offensichtlichen Header-Lücken.")
    elif found_security_headers >= len(highlight_headers) // 2:
        print("⚠️ Vault teilweise gesichert. Einige Header fehlen.")
    else:
        print("💀 Warnung: Sicherheitslücken möglich! Vault-Verteidigung schwach.")

    # zusätzliche Infos
    print(f"\n⏱️ Scan-Dauer: {(datetime.datetime.now() - start).total_seconds():.2f}s")
    if save_report:
        filename = f"header_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as fh:
            fh.write(f"URL: {url}\nStatus: {resp.status_code}\n\nHeaders:\n")
            for k, v in resp.headers.items():
                fh.write(f"{k}: {v}\n")
            fh.write(f"\nSecurity headers found: {found_security_headers}/{len(highlight_headers)}\n")
        print(f"💾 Report gespeichert: {filename}")

if __name__ == "__main__":
    url = input("Gib die URL ein (z.B. http://example.com): ").strip()
    if not url:
        print("Keine URL eingegeben. Abbruch.")
    else:
        # kleine Normalisierung
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        save = input("Report speichern? (y/n): ").lower() == "y"
        run_scan(url, save_report=save)
