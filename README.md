# TestDRF 
## About

created for django test and DRF


## Install 

1. clone project and cd to project dir
1. clone DB from ./DB/bacup.buckup(postgresql)
1. create venv and activate it
    ```zsh
    #linux/mac
    python3 -m venv env
    source ./env/bin/activate
    ```
    ```bash
    #win cmd
    python -m venv env
    .\env\Scripts\activate
    ```
1. Install dependensies:
    ```zsh
    pip install -r requirements.txt
    ```

## Run it

1. cd to `src` directory
1. run
    ```zsh
    #linux/mac
    python3 manage.py runserver
    ```
    ```bash
    #win cmd
    python manage.py runserver
    ```
##URL
1. admin/ -admin panel
1. api-oauth/ - authorization
1. DepList/ - list of departments
1. Employee/ - router link for employee data
    1. Employee/ - list of all employees 
    1. Employee?username= - search by full name
    1. Employee?depid= - search by department
    1. Employee/<int:id> - output by employee id
    1. You can combine the search
 

