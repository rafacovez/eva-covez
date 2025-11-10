eva-covez
=========

A minimalist e-commerce blog on Project Management built with **Django**, **SQLite**, **TailwindCSS**, and **Docker**.

This is a personal project developed for my sister as a presentation website for her work. It is not meant to scale or be heavily trafficked, but to serve as a real-world reference for small-scale deployment and modern development practices.

⚠️ This project is **open source**, but **not open for contributions**. It's public for reference — for myself and for others who might benefit from studying or adapting it for their own ideas.

🧱 Tech Stack
-------------

*   **Backend**: Django
    
*   **Database**: SQLite
    
*   **Styling**: TailwindCSS
    
*   **Deployment**: Docker & Docker Compose
    
*   **Self-hosting**: Unraid (optional)
    

📄 License
----------

This project is licensed under the MIT License.

🛠 Setup Guide
--------------

### 1\. Clone the Repository

git clone cd eva-covez

### 2\. Create a Python Virtual Environment (Optional for Local Dev)

python3 -m venv .venvsource .venv/bin/activate # macOS/Linux.venv\\Scripts\\activate # Windows

### 3\. Install Dependencies

pip install -r requirements.txtpip install -r requirements-dev.txt # includes development tools

### 4\. Install Node.js Dependencies for Tailwind

cd theme/static\_srcnpm installcd ../.. # back to project root

### 5\. Environment Variables

Create either .env.dev or .env.prod depending on the environment.

Example .env.dev:

DJANGO\_DEBUG=TrueDJANGO\_SECRET\_KEY=dev-secret-keyDJANGO\_ALLOWED\_HOSTS=\*DJANGO\_DB\_ENGINE=django.db.backends.sqlite3DJANGO\_DB\_NAME=/app/db.sqlite3DJANGO\_STATIC\_ROOT=/app/staticfilesDJANGO\_MEDIA\_ROOT=/app/media

Security
========

DJANGO\_SECURE\_SSL\_REDIRECT=FalseDJANGO\_SESSION\_COOKIE\_SECURE=FalseDJANGO\_CSRF\_COOKIE\_SECURE=False

CSRF trusted origins
====================

DJANGO\_CSRF\_TRUSTED\_ORIGINS=[http://localhost,http://127.0.0.1](http://localhost,http//127.0.0.1)

Example .env.prod (for real deployment):

DJANGO\_DEBUG=FalseDJANGO\_SECRET\_KEY=prod-secret-keyDJANGO\_ALLOWED\_HOSTS=eva.covez.net,[www.eva.covez.net](http://www.eva.covez.net/)DJANGO\_DB\_ENGINE=django.db.backends.sqlite3DJANGO\_DB\_NAME=/app/db.sqlite3DJANGO\_STATIC\_ROOT=/app/staticfilesDJANGO\_MEDIA\_ROOT=/app/media

Security
========

DJANGO\_SECURE\_SSL\_REDIRECT=TrueDJANGO\_SESSION\_COOKIE\_SECURE=TrueDJANGO\_CSRF\_COOKIE\_SECURE=True

CSRF trusted origins
====================

DJANGO\_CSRF\_TRUSTED\_ORIGINS=[https://eva.covez.net,https://www.eva.covez.net](https://eva.covez.net,https//www.eva.covez.net)

> Note: When testing production locally, you can temporarily add localhost and 127.0.0.1 to DJANGO\_ALLOWED\_HOSTS and DJANGO\_CSRF\_TRUSTED\_ORIGINS.

### 6\. Apply Database Migrations

python manage.py migrate

### 7\. Running the Application

#### Development

docker compose --profile dev up -d --build

*   Access locally at [http://localhost:8000](http://localhost:8000/)
    
*   Uses Django’s runserver with live reloading.
    

#### Production (Local Test)

docker compose --profile prod up -d --build

*   Gunicorn runs on port 8000 inside the container.
    
*   Nginx serves traffic on port 80 and proxies to Gunicorn.
    
*   Access locally at [http://localhost:80](http://localhost/).
    
*   Real SSL handled externally by your reverse proxy (e.g., Nginx Proxy Manager on Unraid).
    

### 8\. Static & Media Files

*   Dev: served directly from the ./static and ./media folders.
    
*   Prod: collected into volumes static\_volume and media\_volume.
    

Run:

docker compose --profile prod exec web python manage.py collectstatic --noinput

### 9\. Notes & Tips

*   Local issues with Nginx: If accessing Nginx locally hangs, it is usually due to proxy\_pass http://web:8000; resolving only inside Docker. Access Django directly at localhost:8000 to test.
    
*   Debugging: Use docker compose logs -f  to see live logs.
    
*   Rebuilding images: Use --build to force Docker to rebuild images if dependencies change.
    

### 10\. Volumes

volumes:static\_volume:media\_volume:

*   Used to persist staticfiles and media across container restarts.
    

### 11\. Optional: Cleaning Up

docker compose down -v

*   Stops containers and removes associated volumes (useful for a fresh start).
    

### 12\. Quick Start (3 Commands)

For local dev with Docker:

docker compose --profile dev up -d --builddocker compose --profile dev exec web python manage.py migratedocker compose --profile dev logs -f web

Access your site at [http://localhost:8000](http://localhost:8000/).