Coffee Shop
===================

Welcome to the Cofee Shop project! This Django application is designed to
manage the products and orders of a coffee shop. It is a simple project

Requirements
------------

* **PostgreSQL** (Make sure you have a PostgreSQL server running)
* **Python 3.11** or higher

Installation Guide
------------------

Follow these steps to get the project up and running on your local machine:

### 1\. Clone the repository

```bash
git clone https://github.com/MiguelAngelGutierrezMaya/coffee_shop.git
cd coffee_shop
```

### 2\. Create a virtual environment

Create and activate a virtual environment to install the project dependencies:
```bash
python3.12 -m venv venv
source venv/bin/activate
```

### 3\. Install the dependencies

Install the required Python packages using pip:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4\. Set up the database

Create a new PostgreSQL database and user for the project. Then, update the

```bash
psql -U postgres
CREATE DATABASE coffee_shop;
CREATE USER coffee_shop_user WITH PASSWORD 'password';
ALTER ROLE coffee_shop_user SET client_encoding TO 'utf8';
ALTER ROLE coffee_shop_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE coffee_shop_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE coffee_shop TO coffee_shop_user;
\q
```

### 5\. Set up the environment variables

Create a new `.env` file in the project root directory and add the following

```bash
DATABASE_URL=postgres://coffee_shop_user:password@localhost/coffee_shop
```

### 6\. Run the migrations

Run the Django migrations to create the database tables:
```bash
python manage.py migrate
```

### 7\. Create a superuser

Create a superuser to access the Django admin interface:
```bash
python manage.py createsuperuser
```

### 8\. Run the development server

Run the Django development server to start the application:
```bash
python manage.py runserver
```

### 9\. Access the application

Open your web browser and go to `http://localhost:8000` to access the Coffee

Contributing
------------

We welcome contributions! Please fork the repository and submit a pull request
for any features, improvements, or bug fixes