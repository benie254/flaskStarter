# Before working on your Flask project...
## You can always begin by installing the following:

    email-validator==1.2.1
    Flask==2.1.2
    Flask-Bootstrap==3.3.7.1
    Flask-Login==0.6.1
    Flask-Mail==0.9.1
    Flask-Migrate==2.6.0
    Flask-Reuploaded==1.2.0
    Flask-Script==2.0.5
    Flask-SQLAlchemy==2.5.1
    Flask-Uploads==0.2.1
    Flask-WTF==1.0.1
    gunicorn==20.1.0
    MarkupSafe==2.1.1
    psycopg2==2.9.3
    Werkzeug==2.0.0


### When you are done updating your app and feel ready to deploy...

#### You Can Avoid Some Miration Issues 

Here is how:

1. run `python manage.py shell`

        ◦ run db.drop_all()
        ◦ run db.create_all()


2. delete your `migrations` folder


3. run `python manage.py db init`


    • run python manage.py db migrate -m "initial migration"


4. in your `root` folder, open the `migrations` directory and navigate to `versions`; that is:


    • migrations/versions
    • create a file within the versions directory: name it .keep && leave it empty


5. close the terminal


6. reopen the terminal


7. run `heroku run bash` (opens the terminal for your deployed app on heroku)


    • run python manage.py db init
    • run python manage.py db migrate
    • run ls to check if you have the following folder structure:
    app config.py instance manage.py migrations Procfile ... among a few more

    • run cd migrations
    • run ls to check if you have or do not have the versions directory
    • if versions does not exist,
        ◦ run mkdir versions
    • run cd versions
    • run touch .keep
    • run cd .. to return to migrations
    • run cd .. to return to the root folder
    • run python manage.py db upgrade 

    • run exit to exit heroku bash


8. run `heroku restart`


9. run `heroku config:set MAIL_USERNAME=yourEmai@here.com`


10. run `heroku config:set MAIL_PASSWORD=yourPassHere`


11. run `heroku config:set SECRET_KEY=yourSecretKeyHere`


12. run `heroku addons:create heroku-postgresql`


14. delete `requirements.txt` if you have it


15. run `pip freeze > requirements.txt`


17. run `git add .`


18. run `git commit -m "fix deployment issues & redeploy"`


19. run `git push heroku master`



### It is a good idea to always check your `requirements.txt`

#### This package works:

    alembic==1.7.7
    blinker==1.4
    click==8.1.3
    dnspython==2.2.1
    dominate==2.6.0
    email-validator==1.2.1
    Flask==2.1.2
    Flask-Bootstrap==3.3.7.1
    Flask-Login==0.6.1
    Flask-Mail==0.9.1
    Flask-Migrate==2.6.0
    Flask-Reuploaded==1.2.0
    Flask-Script==2.0.5
    Flask-SQLAlchemy==2.5.1
    Flask-Uploads==0.2.1
    Flask-WTF==1.0.1
    greenlet==1.1.2
    gunicorn==20.1.0
    idna==3.3
    importlib-metadata==4.11.3
    importlib-resources==5.7.1
    itsdangerous==2.1.2
    Jinja2==3.1.2
    lark-parser==0.12.0
    Mako==1.2.0
    MarkupSafe==2.1.1
    psycopg2==2.9.3
    required==0.4.0
    six==1.16.0
    SQLAlchemy==1.4.36
    visitor==0.1.3
    Werkzeug==2.0.0
    WTForms==3.0.1
    zipp==3.8.0


### Common Flask & SQLALchemy Errors

#### .compat error... 

    • downgrade flask-script to v. 2.0.5 .. confirm that in your requirements.txt, it reads so. 
    • downgrade flask to v. 1.1.4


#### ImportError: cannot import name 'soft_unicode' from 'markupsafe'

    • pip install --user --upgrade aws-sam-cli
 

### Important things to do for a successful deployment:

    • downgrade your flask-script version to 2.0.5 by running the following command in your virtual environment:
      pip install flask-script==2.0.5
      
    • Downgrade flask to v 1.1.4 by running:
      pip install flask==1.1.4
      
    • To prevent a possible 'soft_unicode' import error, run this before deploying/redeploying:
      
          pip install --user --upgrade aws-sam-cli
          
    • restart heroku with the command: 
      
          heroku restart
          
    • export your configs afresh
      
    • I’m not sure if this has an effect, but after making any updates or installations, I like to delete my requirements.txt, and then create a new one with the command:

          pip freeze > requirements.txt 

    • now deploy/redeploy
 
 
### SQLALchemy
#### sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation does not exist

    • ensure that your config.py is in the root folder
      
    • DO NOT push your database upgrades from the local terminal. Before deploying, just clear everything in the database first

* In your ProdConfig(Config), our LMS suggested that we have this:
`SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")`
which is no longer correct, because SQLAlchemy made some changes. 

* Heroku tries to connect with postgres, which has since been modified to only work with postgresql. 

* To fix the error of `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres` 

simply replace this line:

    • SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") 

with this one:

    • SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)


* if you want to understand the logic in the new line, simply think of `postgres` and `postgresql`. 
* the difference in the two names are the letters `ql`. 
* So, our new line of code simply asks heroku to replace `postgres://` with `postgresql://` i.e, `.replace("://", "ql://", 1)`


* This line also does the same thing:
    
      • os.environ.get('DATABASE_URL?sslmode=require').replace('postgres://', 'postgresql://')



##### Now, you may experience errors when running your app between ProdConfig and DevConfig. Always remember this:

    • When working locally, you are in Development stage. 
    • When deploying, you are moving to Production stage. 

* Your manage.py can always have the following to save you the headache:

      • app = create_app('production')


* you do not have to change that at any stage of your app. 


* However, if you do not change it, you will have to tweak the settings in your `config.py ProdConfig` whenever you are working locally or deploying. 


* What I mean is... 
* Locally, your credentials will work better when hard coded, like this for example: 

`class ProdConfig(Config):`

    """
    production configuration child class
    for working locally
    """

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://yourusername:yourpass123word@localhost/yourdbname"


* However, when trying to deploy, you will have to replace your credentials with an environment variable, like this:


`class ProdConfig(Config):`

    """
    production configuration child class
    for deployment
    """

    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    





