# Django Project Setup Guide

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- virtualenv or venv (recommended)

## Installation

1. Clone the repository
```bash
git clone https://github.com/sanskarajput/Web-Chat.git
cd Web-Chat
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

5. Run the server
```bash
python manage.py runserver
```


6. Access the project:
- Main site: http://localhost:8000
- Admin interface: http://localhost:8000/admin


## Configuration

1. Create a `.env` file in the project root directory:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

2. Apply database migrations
```bash
python manage.py migrate
```

3. Create a superuser
```bash
python manage.py createsuperuser
```

## Running the Server

1. Start the development server
```bash
python manage.py runserver
```
