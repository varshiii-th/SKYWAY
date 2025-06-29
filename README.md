## 💻 Quick Setup

Copy these commands into your terminal to get started!

<details>
<summary>Windows Setup</summary>

```cmd
::[
# First clone the repo

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run the development server
python manage.py runserver]
</details> <details> <summary>Mac/Linux Setup</summary>
```cmd
::[
# First clone the repo

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run the development server
python manage.py runserver
]
</details>

