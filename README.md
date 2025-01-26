<!-- #### To use the app click [here](http://43.204.215.250:8000/) -->


<div align="center">

## Chit Chat Website Setup Guide
</div>

Before you begin, ensure you have the following installed:
- Python 3.10
- pip (Python package manager)
- virtualenv or venv (recommended)

## Installation

1. Clone the repository
```bash
git clone https://github.com/sanskarajput/Chit-Chat.git
cd Chit-Chat
```

2. Create and activate a virtual environment
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required dependencies
```bash
pip install -r requirements.txt
```

4. Navigate to Application folder
```bash
cd Application
```

5. Prepares migration files if applicable
```bash
python manage.py makemigrations
```

6. Applies the prepared migrations to the database.
```bash
python manage.py migrate
```

7. Create a superuser
```bash
python manage.py createsuperuser
#- Enter username
#- Enter Email Address
#- Enter Password
#- Enter Confirm Password
```

8. Run the server
```bash
python manage.py runserver
```


## Access the project :

* Main site: http://localhost:8000
* Admin interface: http://localhost:8000/admin


---

<div align="center">

## AWS Lambda Functions
</div>

#### To use the Lambda Functions [here](https://sanskarajput.github.io/Chit-Chat/)


<div align="center">
Thank you :heart:
</div>

