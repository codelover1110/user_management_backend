# Django and React Profile App

This project demonstrates a simple Django backend with a React frontend to manage user profiles.

## Backend Setup:

1. **Navigate to the `user_management_backend` directory:**

    ```bash
    cd user_management_backend
    ```

2. **Install backend dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the Django development server:**

    ```bash
    python manage.py runserver
    ```

    The backend server will be running at `http://127.0.0.1:8000/`.

## Frontend Setup:

1. **Navigate to the `frontend` directory:**

    ```bash
    cd frontend
    ```

2. **Install frontend dependencies:**

    ```bash
    npm install
    ```

3. **Run the frontend development server:**

    ```bash
    npm start
    ```

    The frontend server will be running at `http://localhost:3000/`.

4. **Access User Management:**

    Open your web browser and go to `http://localhost:3000/users` to access the user management section.

    The user management section allows you to perform various actions such as creating, updating, and removing user profiles.
