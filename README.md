# Merchex

If you want start this project in your computer, follow these steps : 

1. Create a virtual environment 

First of all, you must create a virtual environment at the root of project

```
python -m venv ENV
```

Then, you must activate this environment 

```
source ENV/Scripts/activate
```

2. Run the server

You must to go in the folder `merchex` for run the server with `manage.py` and go at this address : [127.0.0.1:8000/](http://127.0.0.1:8000/)

```
cd merchex

python manage.py runserver
```

If you have an error message, install django and then, retry to run the server

```
pip install django
```

3. Shell django

If you want add some informations in the database, you must have to acces at the django's shell. 

```
python manage.py shell
```

To quit this interface, use the function `exit()` or use the combinaison of <kbd>CTRL</kbd>+<kbd>D</kbd>


## Admin interface 

If you want to have an access to the administration, please contact me or create an issues!
