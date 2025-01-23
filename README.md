# Catering Project

This project is a Django-based web application for managing catering services.

## **Prerequisites**

Ensure you have the following installed:

- [Python 3.12](https://www.python.org/downloads/release/python-312/)
- [Pipenv](https://pipenv.pypa.io/en/latest/) (for managing dependencies)

## **Installation Instructions**

Follow these steps to set up the project locally:

1. **Clone the repository via SSH:**
   ```bash
   git clone git@github.com:Thommy90/CATERING.git
   ```

   This command clones the repository using SSH authentication, ensuring a secure connection.

2. **Navigate to the project directory:**
   ```bash
   cd CATERING
   ```

   The `cd` command (change directory) is used to move into the cloned project folder.

3. **Set up the virtual environment:**
   ```bash
   pipenv install
   ```

4. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

5. **Apply database migrations:**
   ```bash
   python catering/manage.py migrate

   ```

6. **Create a superuser (optional for admin access):**
   ```bash
   python catering/manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python catering/manage.py runserver
   ```

Once the server is running, visit `http://127.0.0.1:8000/` in your browser.

---

## **Code Quality Tools**

The project includes the following development tools to ensure code quality:

- `flake8` - Linting and style checks
- `black` - Code formatting
- `isort` - Import sorting
- `mypy` - Type checking
- `pylint` - Code analysis
- `bandit` - Security analysis
- `coverage` - Test coverage reports

### Running code quality checks:

1. **Run all quality checks:**
   ```bash
   flake8 .
   black --check .
   isort --check-only .
   mypy .
   pylint catering
   bandit -r catering
   ```

2. **Run tests with coverage:**
   ```bash
   coverage run -m pytest
   coverage report
   ```
