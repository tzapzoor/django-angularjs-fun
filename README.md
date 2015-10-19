# baseApp1

## Installation

*Requirements*
* `$ sudo apt-get install python2.7 python-pip nodejs npm virtualenv virtualenvwrapper`
* `$ sudo ln -s /usr/bin/nodejs /usr/bin/node` (fix for bower)

After cloning the repo:
* `$ virtualenv baseAppEnv`
* `$ source baseAppEnv/bin/activate`
* `$ cd eestec-olympics/`
* `$ git checkout baseApp1-thinkster`
* `$ pip install -r requirements.txt`
* `$ sudo npm install -g bower`
* `$ bower install`
* `$ npm install`
* `$ python manage.py makemigrations`
* `$ python manage.py migrate`
* `$ python manage.py createsuperuser` (for the **[server-address]/admin/** panel)
* `$ python manage.py runserver`

## OOps! ##
Do not use the superuser created for the admin panel to login inside the application. (funny things will happen :P)
