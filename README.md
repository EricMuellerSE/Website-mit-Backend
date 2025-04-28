<h1 align="center" id="title">Website ASJ</h1>

<p id="description">Website für die Airsoft Scorpions Jena e.V.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Kommentare
*   Admin-View

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone Gitrepo</p>

```
$ git clone
```

<p>2. Install Requirements</p>

```
$ pip install -r ./Website/requirements.txt
```

<p>3. goto Website</p>

```
$ cd Website
```

<p>4. Make Migrations</p>

```
$ py manage.py makemigrations
```

<p>5. Migrate</p>

```
py manage.py migrate
```

<p>6. Runseerver for everywone</p>

```
$ daphne -b 0.0.0.0 -p 80 Website.asgi:application
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Django
*   HTML
*   CSS
*   SCSS
*   Bootstrap
*   Python
*   JavaScript

<h2>Suport</h2>

Ansprechparthner: Eric Müller<p>TEL.: +49 1575 2047095</p>

<h2>Deployment</h2>

Natürlich! Hier ist die Zusammenfassung erneut – diesmal ohne den Punkt "Endergebnis":

—

# Zusammenfassung – Schritt für Schritt

🔹 1. Notwendige Pakete installiert

Damit Nginx und Certbot funktionieren, haben wir folgende Pakete installiert:

```bash
sudo apt update
sudo apt install nginx
sudo apt install certbot python3-certbot-nginx
```

—

🔹 2. Nginx Serverblöcke für HTTPS und HTTP-Weiterleitung erstellt

**Kompletter Server-Block-Code:**

```nginx
server {
    listen 80;
    server_name example.com;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

—

🔹 3. Neues SSL-Zertifikat erstellt

Ein neues Zertifikat für `example.com` erstellt und automatisch in Nginx eingebunden:

```bash
sudo certbot --nginx -d example.com
```

—

🔹 4. Nginx-Konfiguration geprüft

Die Konfiguration auf Fehler geprüft:

```bash
sudo nginx -t
```

—

🔹 5. Nginx neu geladen

Damit die Änderungen aktiv werden:

```bash
sudo systemctl reload nginx
```

—

🔹 6. Browser-Cache und Cookies geleert

- Cache und Cookies für `example.com` gelöscht
- Seite neu geladen oder im Inkognito-Modus getestet

—

Willst du jetzt noch, dass ich daraus ein fertiges Bash-Skript erstelle, das den gesamten Ablauf automatisch ausführt? 🚀  
(Wäre super praktisch für spätere Setups.)