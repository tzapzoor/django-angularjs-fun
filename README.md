# baseApp1

## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) and
[Node.js](http://nodejs.org/).*

After cloning the repo:
* `$ virtualenv baseAppEnv`
* '$ source baseAppEnv/bin/activate'
* `$ cd eestec-olympics/`
* '$ git checkout baseApp1-thinkster'
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ python manage.py makemigrations`
* `$ python manage.py migrate`
* `$ python manage.py runserver`
