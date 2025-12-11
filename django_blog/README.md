# Django Blog - Authentication and Blog Post Management

## Overview

This document describes the authentication and blog post management systems implemented in the Django Blog project. The system provides functionalities for user registration, login, logout, profile management, and complete CRUD operations for blog posts.

## Features

### Authentication

-   **User Registration**: New users can create an account by providing a username, email, and password.
-   **User Login**: Registered users can log in to the application.
-   **User Logout**: Logged-in users can log out of the application.
-   **Profile Management**: Logged-in users can view and update their profile information, including their username, email, and profile picture.

### Blog Post Management

-   **Create Posts**: Authenticated users can create new blog posts.
-   **Read Posts**: All users can view a list of all blog posts and view the details of a single post.
-   **Update Posts**: The author of a post can edit their own posts.
-   **Delete Posts**: The author of a post can delete their own posts.

## Implementation Details

### Models

-   **User**: Django's built-in `User` model is used for authentication.
-   **Profile**: A `Profile` model is created to store additional user information, such as a profile picture. It has a one-to-one relationship with the `User` model. A signal is used to automatically create a `Profile` instance when a new `User` is created.
-   **Post**: The `Post` model stores the blog post data, including the title, content, published date, and author.

### Forms

-   **UserRegisterForm**: A custom form that extends Django's `UserCreationForm` to include an email field.
-   **UserUpdateForm**: A form to update the user's username and email.
-   **ProfileUpdateForm**: A form to update the user's profile picture.
-   **PostForm**: A `ModelForm` for creating and updating blog posts.

### Views

-   **register**: A view to handle user registration.
-   **login**: Uses Django's built-in `LoginView`.
-   **logout**: Uses Django's built-in `LogoutView`.
-   **profile**: A view that allows users to view and update their profile information. It is protected by the `@login_required` decorator.
-   **PostListView**: A class-based view to display a list of all blog posts.
-   **PostDetailView**: A class-based view to display the details of a single blog post.
-   **PostCreateView**: A class-based view to create a new blog post. Requires user to be logged in.
-   **PostUpdateView**: A class-based view to update a blog post. Requires user to be the author of the post.
-   **PostDeleteView**: A class-based view to delete a blog post. Requires user to be the author of the post.

### Templates

-   **register.html**: Template for the registration page.
-   **login.html**: Template for the login page.
-   **logout.html**: Template for the logout page.
-   **profile.html**: Template for the user profile page.
-   **base.html**: A base template that is extended by all other templates.
-   **home.html**: The main page, which lists all blog posts.
-   **post_detail.html**: Template to display a single blog post.
-   **post_form.html**: Template for creating and updating blog posts.
-   **post_confirm_delete.html**: Template to confirm the deletion of a blog post.

### URLs

The following URL patterns are defined in `blog/urls.py`:

-   `/register/`: Registration page.
-   `/login/`: Login page.
-   `/logout/`: Logout page.
-   `/profile/`: User profile page.
-   `/`: The home page, which lists all blog posts.
-   `/post/<int:pk>/`: The detail page for a single blog post.
-   `/post/new/`: The page to create a new blog post.
-   `/post/<int:pk>/update/`: The page to update a blog post.
-   `/post/<int:pk>/delete/`: The page to delete a blog post.

## Testing

To test the system:

1.  **Run the development server**: `python manage.py runserver`
2.  **Register a new user**: Navigate to `http://127.0.0.1:8000/register/` and create a new account.
3.  **Login**: Navigate to `http://127.0.0.1:8000/login/` and log in with the newly created user.
4.  **Create a post**: Navigate to `http://127.0.0.1:8000/post/new/` and create a new blog post.
5.  **View and update profile**: Navigate to `http://127.0.0.1:8000/profile/` to view and update your profile.
6.  **Update and delete post**: Navigate to the detail page of the post you created and use the "Update" and "Delete" buttons.
7.  **Logout**: Click the "Logout" link in the navigation bar.

## Security

-   **CSRF Protection**: All forms use Django's CSRF protection.
-   **Password Hashing**: Passwords are automatically hashed and salted by Django's authentication system.
-   **Protected Views**: The profile page and post creation, update, and deletion views are protected from unauthenticated access using the `@login_required` decorator and `LoginRequiredMixin`.
-   **Object-level permissions**: The `UserPassesTestMixin` is used to ensure that only the author of a post can edit or delete it.
