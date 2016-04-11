# Fashion Revolution Wall

## Description
Live wall/ photo feed of clothing labels for Fashion Revolution Day for [Fashion Revolution](http://fashionrevolution.org/). People will be taking photos of their clothing labels, we would like them to all upload onto a live feed.

##Team
###Backend
* Raquel
* Mariza

###Front-End
* Lili
* Karen

##Project Setup
1. Get the code: `git clone https://github.com/womenhackfornonprofits/fashion-revolution-django`
2. Get [Virtual Env](https://virtualenv.pypa.io/en/latest/installation.html) 
2. Get [virtualend wrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
3. Create a new virtual enviroment for the project `mkvirtualenv fashrevwall`
4. Use this enviroment or change to this from another by using: `workon fashrevwall`
2. Go to project folder: `pip install -r requirements.txt`
3. Get [Postgres]: (http://www.postgresql.org/)
3. Create empty db for now locally, `createdb fashrevwall`
4. Start the server: `python manage.py runserver`

### Front End Instuctrions
1. First you will need to install [NPM](https://nodejs.org/) to manage packages 
2. Install [Grunt](http://gruntjs.com/getting-started)
3. Go to `static-src` folder and run `npm install` to install all the front end dependencies.

## Deploy to Heroku
1. Create a [Heroku](https://www.heroku.com/) account and get added to the app
2. Download [Heroku Toolbeit](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
3. Login: `heroku login`
4. Add a new remote to push to Heroku: `git remote add heroku-remote git@heroku.com:fashion-revolution-wall.git`
5. You may need to add ssh keys `heroku keys:add` if this is a machine that has not had heroku setup before
6. When you have changed ready to push, your working directory must be clean then do `git push heroku master`
7. See the pushed changes: `heroku open`
8. If any issues, view the logs: `heroku logs`
