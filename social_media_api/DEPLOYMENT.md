# Deployment Guide

This guide describes how to deploy the `social_media_api` to a platform like Heroku.

## Prerequisites
- A Heroku account (or similar PaaS).
- Heroku CLI installed.
- Git installed and initialized in this repository.

## Configuration
The `settings.py` has been configured to read from environment variables:
- `SECRET_KEY`: Your Django secret key.
- `DEBUG`: Set to `False` in production.
- `ALLOWED_HOSTS`: A comma-separated list of your app's domains (e.g., `your-app-name.herokuapp.com`).
- `DATABASE_URL`: Automatically handled by Heroku for PostgreSQL.

## Deployment Steps (Heroku Example)

1.  **Login to Heroku**:
    ```bash
    heroku login
    ```

2.  **Create an App**:
    ```bash
    heroku create your-unique-app-name
    ```

3.  **Add PostgreSQL Database**:
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

4.  **Set Environment Variables**:
    ```bash
    heroku config:set SECRET_KEY='your-generated-secret-key'
    heroku config:set DEBUG=False
    heroku config:set ALLOWED_HOSTS='your-unique-app-name.herokuapp.com'
    # SECURE_SSL_REDIRECT is optional, set to True if you have SSL setup (Heroku provides this by default)
    heroku config:set SECURE_SSL_REDIRECT=True
    ```

5.  **Push Code**:
    ```bash
    git push heroku main
    ```

6.  **Run Migrations**:
    ```bash
    heroku run python manage.py migrate
    ```

7.  **Create Superuser**:
    ```bash
    heroku run python manage.py createsuperuser
    ```

8.  **Open App**:
    ```bash
    heroku open
    ```

## Maintenance
- Monitor logs using `heroku logs --tail`.
- Run updates by pushing new code to the `main` branch.
