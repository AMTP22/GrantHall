*This file is a guide that walks the user through how to 
take the application from the git repository here on github
and deploy it to Heroku. This is intended for users using a 
linux OS.*

1. First, enter into a virtual envrionment

2. To get the application from github you must clone the git repo
- git clone https://<username>@github.com/apearson22/grantHallRepo
*Or if you have already cloned the repo*
- git pull origin master

3. Next,ensure that everything is updated for the files we need
 - pip install django
 - pip install heroku
 - pip install --upgrade pip
 - pip install gunicorn
 - pip install whitenoise
 - pip freeze >requirements.txt

4. Once those are up to date, login to heroku
- heroku login
- **enter username and password

5. ensure settings.py has the following lines at the end
- STATIC_URL = '/static/'
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
- STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

6. Also make sure this is in the MIDDLEWARE section of setting.py
- 'whitenoise.middleware.WhiteNoiseMiddleware',

7. Create Procfile
- vim Procfile

8. add in Procfile
- web: gunicorn it394.wsgi --log-file 

9. Establish the connection to Heroku
- heroku git: remote -a rocky-everglades-63868

10. commit files from the local repo
- git add .
- git commit -a -m "purpose of commit"

11. Push local repository to Herkou
- git push heroku master


This should allow you to have your application deployed
to heroku. You can visit the site to see view logs of
successful and unsuccessful builds or you can use:
- heroku logs

The site to upload the git repository to establish the 
heroku connection is https://git.heroku.com/rocky-everglades-63868.git
