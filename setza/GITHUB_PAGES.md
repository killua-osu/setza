# GitHub Pages

This repository includes a static export for the Setza Django demo. GitHub Pages serves only static files, so the workflow renders the Django templates into HTML and publishes those files with CSS and JavaScript.

## Deploy

1. Push the repository to GitHub.
2. In the repository settings, open **Pages**.
3. Set **Source** to **GitHub Actions**.
4. Push to `main` or run the **Deploy GitHub Pages** workflow manually.

The exported site is a browsable demo. Django-only features such as sign-in POSTs, sessions, API endpoints, and database writes do not run on GitHub Pages.

## Build Locally

```bash
python manage.py migrate --noinput --settings=config.settings.pages
python manage.py export_pages --settings=config.settings.pages
```

The static output is written to `dist/`.
