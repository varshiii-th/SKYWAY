## 💻 Quick Setup

Copy these commands into your terminal to get started!

<details>
<summary><strong>Windows Setup</strong></summary>

```cmd
:: Clone the repo
git clone <your-repo-url>
cd <your-project-folder>

:: Create virtual environment
python -m venv venv

:: Activate virtual environment
venv\Scripts\activate

:: Upgrade pip
pip install --upgrade pip

:: Install requirements
pip install -r requirements.txt

:: Run migrations
python manage.py makemigrations
python manage.py migrate

:: Create superuser
python manage.py createsuperuser

:: Collect static files
python manage.py collectstatic

:: Run the development server
python manage.py runserver
</details> <details> <summary><strong>Mac/Linux Setup</strong></summary>
# Clone the repo
git clone <your-repo-url>
cd <your-project-folder>

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
</details> ```
