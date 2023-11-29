# A Python backend for the Unicorn database

## About this project

This project is a simple example of a Python application accessing a SQLite
database. There is ABSOLUTELY NO WAY you should run this in a real project, as
it is really, really insecure. Just don't do it. Learn from it, but that's all.

## How do I run this project?

Create a virtual environment, install the requirements and run the application by typing:

### Unix-like operating systems

```bash
$ python -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ python src/test.py
(venv) $ flask --app src/app run
```

### Windows

```
C:\> python -m venv venv
C:\> venv\Scripts\activate.bat
(venv) C:\> pip install -r requirements.txt
(venv) C:\> python src\test.py
(venv) C:\> flask --app src\app run
```