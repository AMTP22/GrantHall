### Operation Guide

*This is a guide exist to walk users how thorugh how
to add and remove administrative users, backup and restore
database files, as well as start and stop the application.*


#### To Start the application locally
1. ./manage.py runserver


#### Adding Admin Users
1. Go to http://127.0.0.1:8000/admin/ on local web browser
2. Under Group click the *Add* button to only add one Admin
3. Next to *Name* title the name of the admin group
4. Select the appropriate admin permissions 
5. Select *SAVE*
6. Go to Users and select *Add*
7. Create a username and password and set it to the group


#### Update Database Files
1. manage.py makemigrations
2. manage.py migrate
