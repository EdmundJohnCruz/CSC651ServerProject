# CSC 651 - Server Project
A project based on what is being taught in System Administrations.

<br>

## Meet Our Team
| Student Name          |        Student Email        |
|    :---:              |            :---:            |
| Begum Sakin           | bsakin@mail.sfsu.edu        |
| Mantasha Khan         | mkhan8@mail.sfsu.edu        |
| John Cruz             | ecruz13@mail.sfsu.edu       |
| Franklin Arevalo      | jarevaloruiz@mail.sfsu.edu  |

<br>

## Getting Started
After cloning the repo, and opening the project in vscode, make sure to install the python environment if you haven't already. You will be in the outer app root folder.

install python virtual environment (if you don't have it already)
```
pip install pipenv
```

then run the shell command to get started while inside the root project folder
```
pipenv shell
```

then cd into the folder web_server_project from the root folder to access manage.py
```
cd web_server_project
```

then start the server
```
python manage.py runserver
```

<br>

## Folders
path: web_server_project/application/ ( Frontend ) <br>
- In the /static folder you can store images, css and other static files.
- In the /templates folder you can store html files for the different pages.

Adding new pages
- Make a new html file in the templates folder
- Open views.py and add the path 
- Open urls.py and added the component

path: /web_server_project/web_server_project/ ( Backend ) <br>
- settings.py stores all of the main core components.

path: /web_server_project/web_server_project/ ( DB ) <br>
- models.py to create models and tables.

## Additional libraries
These were some additional libraries we used.

For a better form view
```
pip install django-crispy-forms
```


