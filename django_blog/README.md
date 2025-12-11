# Django Blog - Authentication System

## Overview

This document describes the authentication system implemented in the Django Blog project. The system provides functionalities for user registration, login, logout, and profile management.

## Features

-   **User Registration**: New users can create an account by providing a username, email, and password.
-   **User Login**: Registered users can log in to the application.
-   **User Logout**: Logged-in users can log out of the application.
-   **Profile Management**: Logged-in users can view and update their profile information, including their username, email, and profile picture.

## Implementation Details

### Models

-   **User**: Django's built-in `User` model is used for authentication.
-   **Profile**: A `Profile` model is created to store additional user information, such as a profile picture. It has a one-to-one relationship with the `User` model. A signal is used to automatically create a `Profile` instance when a new `User` is created.

### Forms

-   **UserRegisterForm**: A custom form that extends Django's `UserCreationForm` to include an email field.
-   **UserUpdateForm**: A form to update the user's username and email.
-   **ProfileUpdateForm**: A form to update the user's profile picture.

### Views

-   **register**: A view to handle user registration.
-   **login**: Uses Django's built-in `LoginView`.
-   **logout**: Uses Django's built-in `LogoutView`.
-   **profile**: A view that allows users to view and update their profile information. It is protected by the `@login_required` decorator.

### Templates

-   **register.html**: Template for the registration page.
-   **login.html**: Template for the login page.
-   **logout.html**: Template for the logout page.
-   **profile.html**: Template for the user profile page.
-   **base.html**: A base template that is extended by all other templates.

### URLs

The following URL patterns are defined in `blog/urls.py`:

-   `/register/`: Registration page.
-   `/login/`: Login page.
-   `/logout/`: Logout page.
-   `/profile/`: User profile page.

## Testing

To test the authentication system:

1.  **Run the development server**: `python manage.py runserver`
2.  **Register a new user**: Navigate to `http://127.0.0.1:8000/register/` and create a new account.
3.  **Login**: Navigate to `http://127.0.0.1:8000/login/` and log in with the newly created user.
4.  **View and update profile**: Navigate to `http://127.0.0.1:8000/profile/` to view and update your profile.
5.  **Logout**: Click the "Logout" link in the navigation bar.

## Security

-   **CSRF Protection**: All forms use Django's CSRF protection.
-   **Password Hashing**: Passwords are automatically hashed and salted by Django's authentication system.
-   **Protected Views**: The profile page is protected from unauthenticated access using the `@login_required` decorator.
