# fashion-revolution
## Install instructions:


1. Get the code: `git clone https://github.com/womenhackfornonprofits/fashion-revolution-django`
2. Get [Virtual Env](https://virtualenv.pypa.io/en/latest/installation.html) 
2. Get [virtualend wrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
3. Create a new virtual enviroment for the project `mkvirtualenv fashrevwall`
4. Use the enviroment: `workon fashrevwall`
2. Go to project folder: `pip install -r requirements.txt`
3. Create empty db for now locally, `createdb fashrevwall`
4. Start the server: `python manage.py runserver`

## Deploy to Heroku
1. Create a [Heroku](https://www.heroku.com/) account and get added to the app
2. Download [Heroku Toolbeit](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
3. Login: `heroku login`
4. Add a new remote to push to Heroku: `git remote add heroku-remote git@heroku.com:fashion-revolution-wall.git`
5. You may need to add ssh keys `heroku keys:add` if this is a machine that has not had heroku setup before
6. When you have changed ready to push, your working directory must be clean then do `git push heroku master`
7. See the pushed changes: `heroku open`
8. If any issues, view the logs: `heroku logs`
