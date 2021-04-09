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

then run the shell command to get started
```
pipenv shell
```

then cd into the folder webApp from the root app to access manage.py
```
cd webApp
```

then start the server
```
python manage.py runserver
```

<br>

## Folders
path: app/webApp/application ( Frontend ) <br>
- In the /static folder you can store images, css and other static files.
- In the /templates folder you can store html files for the different pages.

Adding new pages
- Make a new html file in the templates folder
- Open views.py and add the path 
- Open urls.py and added the component

path: app/webApp/webApp ( Backend ) <br>
- settings.py stores all of the main core components.

path: app/webApp/webApp ( DB ) <br>
- models.py to create models and tables.


