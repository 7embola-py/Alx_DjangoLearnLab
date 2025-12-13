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

### Posts

*   **List Posts:** `GET /api/posts/`
*   **Create Post:** `POST /api/posts/`
    *   **Authentication:** Requires Token Authentication.
    *   **Body:**
        ```json
        {
            "title": "My First Post",
            "content": "This is the content of my first post."
        }
        ```
*   **Retrieve Post:** `GET /api/posts/{id}/`
*   **Update Post:** `PUT /api/posts/{id}/`, `PATCH /api/posts/{id}/`
    *   **Authentication:** Requires Token Authentication. Only the author can update.
*   **Delete Post:** `DELETE /api/posts/{id}/`
    *   **Authentication:** Requires Token Authentication. Only the author can delete.

### Comments

*   **List Comments for a Post:** `GET /api/posts/{post_id}/comments/`
*   **Create Comment on a Post:** `POST /api/posts/{post_id}/comments/`
    *   **Authentication:** Requires Token Authentication.
    *   **Body:**
        ```json
        {
            "content": "This is a comment on the post."
        }
        ```
*   **Retrieve Comment:** `GET /api/posts/{post_id}/comments/{id}/`
*   **Update Comment:** `PUT /api/posts/{post_id}/comments/{id}/`, `PATCH /api/posts/{post_id}/comments/{id}/`
    *   **Authentication:** Requires Token Authentication. Only the author can update.
*   **Delete Comment:** `DELETE /api/posts/{post_id}/comments/{id}/`
    *   **Authentication:** Requires Token Authentication. Only the author can delete.

### Social

*   **Follow User:** `POST /api/accounts/follow/{user_id}/`
    *   **Authentication:** Requires Token Authentication.
*   **Unfollow User:** `POST /api/accounts/unfollow/{user_id}/`
    *   **Authentication:** Requires Token Authentication.

### Feed

*   **Get Feed:** `GET /api/feed/`
    *   **Authentication:** Requires Token Authentication.
    *   **Response:** A paginated list of posts from users the current user follows.
