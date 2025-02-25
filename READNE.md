1. **Clone the repository:**
    ```bash
    git clone git@github.com:Thommy90/CATERING.git
    cd <repository-directory>
    ```

2. **Install dependencies with Pipenv::**
    ```bash
    pipenv install
    ```

3. **Activate the virtual environment:**
    ```bash
    pipenv shell
    ```
   
4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```
   
6. **Load test data:**
    ```bash
    python manage.py loaddata Data/auth/fixtures/auth_users.json
    python manage.py loaddata Data/food/fixtures/food_data.json
    python manage.py loaddata Data/logistic/fixtures/logistic_data.json
    ```

7. **Run the server:**
    ```bash
    python manage.py runserver
    ```

8. **Access Django Admin Panel:**
    Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## 📂 Test Data Format

**Why JSON?**

- I use JSON because it’s just easier to work with when I have models that are linked together or have nested data. 
- It’s simple to read, easy to edit, and works right out of the box with Django fixtures. 
- CSV is great for flat data, but it struggles when models have relationships or nested fields.