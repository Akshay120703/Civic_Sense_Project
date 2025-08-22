# Deploying Civic Sense on Render

This guide walks you through deploying the Civic Sense PHP app to Render using Docker. The project uses SQLite by default, so no external database is required.

## Prerequisites
- GitHub repository with this project (Dockerfile and render.yaml included)
- Render account (`https://render.com`)

## One-time checks
1. Ensure `index.php` requires SQLite config:
```php
require_once 'config/database_sqlite.php';
```
2. Commit and push all changes to GitHub.

## Deploy Steps
1. Login to Render and click "New +" → "Web Service".
2. Connect your GitHub repo and select it.
3. Render detects `render.yaml` and Dockerfile. Confirm the service settings:
   - Type: Web Service
   - Runtime: Docker
   - Region: nearest to users
   - Plan: Free (for testing)
4. Click "Create Web Service" to start the first deploy.

## What Render does
- Builds Docker image using Dockerfile (installs `pdo` and `pdo_sqlite`).
- Runs Apache with PHP 8.3.
- Serves app at the generated Render URL.

## Post-deploy
- Visit your service URL.
- On first load, the app creates the SQLite database at `/var/www/html/database/civic_sense.db`.
- Register and test the app.

## Environment variables (optional)
Add variables in the Render dashboard if needed:
- `APP_ENV=production`

## Common issues
- 404 root path: Ensure `healthCheckPath: /` and index.php is at repo root.
- Permission denied on SQLite DB: We set directory perms in Dockerfile. If needed, run a Shell and `chown -R www-data:www-data /var/www/html`.
- Wrong DB driver: Confirm `index.php` includes `config/database_sqlite.php`.

## Redeploying
- Push changes to your repo; Render auto-deploys when `autoDeploy` is on.

## Switching to MySQL (optional)
- Provision a MySQL add-on or external DB.
- Change `index.php` to `require_once 'config/database.php';`
- Add env vars for credentials and update `config/database.php` to read them.
- Rebuild & deploy.
