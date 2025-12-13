# Social Media API

This is a Django-based Social Media API that allows users to register, log in, and manage their profiles.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Alx_DjangoLearnLab.git
    cd Alx_DjangoLearnLab/social_media_api
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file is not yet created, but will be added in a future step.)*

3.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

*   **Register:** `POST /api/accounts/register/`
    *   **Body:**
        ```json
        {
            "username": "yourusername",
            "password": "yourpassword",
            "email": "youremail@example.com",
            "first_name": "Your",
            "last_name": "Name"
        }
        ```
    *   **Response:**
        ```json
        {
            "user": {
                "id": 1,
                "username": "yourusername",
                "email": "youremail@example.com",
                "bio": null,
                "profile_picture": null
            },
            "token": "your-auth-token"
        }
        ```

*   **Login:** `POST /api/accounts/login/`
    *   **Body:**
        ```json
        {
            "username": "yourusername",
            "password": "yourpassword"
        }
        ```
    *   **Response:**
        ```json
        {
            "token": "your-auth-token",
            "user_id": 1,
            "email": "youremail@example.com"
        }
        ```

### Profile

*   **View/Update Profile:** `GET /api/accounts/profile/`, `PUT /api/accounts/profile/`, `PATCH /api/accounts/profile/`
    *   **Authentication:** Requires Token Authentication.
        *   Header: `Authorization: Token your-auth-token`
    *   **GET Response:**
        ```json
        {
            "id": 1,
            "username": "yourusername",
            "email": "youremail@example.com",
            "bio": "This is my bio.",
            "profile_picture": null
        }
        ```
    *   **PUT/PATCH Body:**
        ```json
        {
            "bio": "This is my updated bio."
        }
        ```
