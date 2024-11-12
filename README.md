# Blog Post Documentation

## Development

### Project Requirements

- Python 3.11+
- Virtualenv 20.24

### IDE

I recommend you use Visual Studio Code and set it up using the ff. extensions and settings below.

##### Extensions

Install these extensions in VS Code:

- Python
- Django
- Pylint
- Flake8
- MyPy Type Checker

### Django Admin Endpoint
http://127.0.0.1:8000/admin

### Project Setup (Without using Docker)

1. Clone the project

```bash
  git clone https://github.com/ooplaza/Blogs.git
```

2. Create a virtual environment using virtualenv running on Python 3.11+

```bash
  virtualenv <env_name>
```

3. Activate the virtual environment

```bash
  <env_name>/Scripts/activate
```

4. Run the command to install local environment dependencies.

```bash
  pip install -r requirements.txt
```

5. Perform a migrate by running this command

```bash
   python manage.py migrate
```

### Running and shutting down the development server
1. Run the command `python manage.py runserver` to start the development server. Server is available at http://127.0.0.1:8000/
