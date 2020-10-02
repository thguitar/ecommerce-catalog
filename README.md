# Ecommerce Catalog

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.1.1-brightgreen.svg)](https://djangoproject.com)

Project to Controller a Ecommerce Product Catalog.

## Running the Project Locally

1. Download or clone the repository to your local machine:
```bash 
    git clone https://github.com/thguitar/ecommerce-catalog.git
```

2. Create the ``virtualenv`` :

```bash
    virtualenv venv
```
    
3. Activate the ``virtualenv``:
    
```bash
    venv/bin/activate
```

4. Install the requirements:

```bash
     pip install -r requirements.txt
```

5. Generate the migrations:
    
```bash
    python manage.py makemigrations
```

5. Apply the migrations:
 
```bash 
    python manage.py migrate
 ```
    
6. Finally, run the development server:

```bash 
    python manage.py runserver
```
