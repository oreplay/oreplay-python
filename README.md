# Oreplay-python
A REST api written in DjangoRestFramework

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have `python 3.11` globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed `pipenv` globally as well. If not, run this:
    ```bash
        $ pip install pipenv
    ```

* #### Dependencies
    1. Install the dependencies needed to run the app:
        ```bash
            $ pipenv install
        ```
    2. Load the virtualenv:
        ```bash
            $ pipenv shell
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```