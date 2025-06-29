# Project Setup Guide

## 💻 Quick Setup

Follow these steps to set up the project on your local machine.

### Prerequisites
- **Git**: Ensure Git is installed. Run `git --version` to verify. If not installed, download it from [https://git-scm.com/](https://git-scm.com/).
- **Python**: Ensure Python 3.8 or higher is installed. Run `python --version` (Windows) or `python3 --version` (Mac/Linux) to verify. Download from [https://www.python.org/](https://www.python.org/) if needed.
- **Repository URL**: Obtain the Git repository URL (e.g., `https://github.com/varshiii-th/SKYWAY.git`)

Copy the commands below into your terminal to get started!

<details>
<summary><strong>Windows Setup</strong></summary>

```cmd
:: Clone the repo 
git clone https://github.com/varshiii-th/SKYWAY.git

:: Create virtual environment
python -m venv venv

:: Activate virtual environment (CMD)
venv\Scripts\activate
:: For PowerShell, use:
:: .\venv\Scripts\activate

:: Verify activation (your prompt should show (venv))
:: Upgrade pip
pip install --upgrade pip

:: Install requirements (ensure requirements.txt exists in the project folder)
pip install -r requirements.txt

:: Run migrations to set up the database
python manage.py makemigrations
python manage.py migrate

:: Create superuser (follow prompts to enter username, email, and password)
python manage.py createsuperuser

:: Collect static files (only needed for production or if DEBUG=False in settings.py)
python manage.py collectstatic --noinput

:: Run the development server (use a different port if 8000 is in use, e.g., python manage.py runserver 8080)
python manage.py runserver
```

</details>

<details>
<summary><strong>Mac/Linux Setup</strong></summary>

```bash
# Clone the repo 
git clone https://github.com/varshiii-th/SKYWAY.git


# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify activation (your prompt should show (venv))
# Upgrade pip
pip install --upgrade pip

# Install requirements (ensure requirements.txt exists in the project folder)
pip install -r requirements.txt

# Run migrations to set up the database
python3 manage.py makemigrations
python3 manage.py migrate

# Create superuser (follow prompts to enter username, email, and password)
python3 manage.py createsuperuser

# Collect static files (only needed for production or if DEBUG=False in settings.py)
python3 manage.py collectstatic --noinput

# Run the development server (use a different port if 8000 is in use, e.g., python3 manage.py runserver 8080)
python3 manage.py runserver
```

</details>

### Troubleshooting
- **Git errors**: If `git clone` fails, ensure you have access to the repository and Git is configured. Check your credentials or SSH keys.
- **Requirements errors**: If `pip install -r requirements.txt` fails, verify that `requirements.txt` exists. If missing, install Django manually: `pip install django`.
- **Migration errors**: If migrations fail, check your database configuration in `settings.py`. Ensure the database is accessible and properly configured.
- **Port conflicts**: If port 8000 is in use, specify a different port, e.g., `python manage.py runserver 8080` (Windows) or `python3 manage.py runserver 8080` (Mac/Linux).
- **Virtual environment issues**: If activation fails, ensure the `venv` folder was created. Recreate it with `python -m venv venv` (Windows) or `python3 -m venv venv` (Mac/Linux).
