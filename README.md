# Schedular
TWA-Project

### WIP Team ####

### Schedular Prototype Design ###
 https://invis.io/KFHPP263PN9#/294229274_LoginForm
*^Click/hover over clickable elements to see the application workflow.^

### How do I get set up? ###
* First of all please install git, and clone this project If you don't know how please give up! Kaufland hires all the time.

* Install python3
```
$ sudo apt-get update
$ sudo apt-get install python3.6
  python3 -V (It say Python 3.5.1+ I have no Idea what it means... )
```
* Install pipe3 (for python3)

```
sudo apt-get -y install python3-pip
```

* Then install virtualenv using pip3

```
pip3 install virtualenv (if not working try with sudo)
```

* Now create a virtual environment

```
virtualenv env (can be used any name instead of env)
```

* Active your virtual environment (in root directory)

```
source env/bin/activate
```

* Install mysql
```
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04/
```

* Should be created a dabates that is configured in schedularApp/settings.py
    Install mysql and bla bla bla... else will get crapau "mysqlclient"
    Instead of
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'schedular',
        'USER': 'root',
        'PASSWORD': 'daniel',
        'HOST': '',
        'PORT': '',
    }
}
```
Please use your crdential and database!!!

cd schedularApp/ and run:
```
python3 manage.py migrate
```

* Install requirements

```
pip install -r requirments.txt  # to install requrements (some of them might not be required)
```

* Run Server
```
python3 manage.py runserver
```
If in your console doesn't appear:
```
Django version 2.0.4, using settings 'schedularApp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
Please try to install more times ... or ask someone else or me (hope not)

* Front End side

cd team/
you must have npm install or please install it...
run:
```
npm install
```
wait few second and all the setup is done! :D
Should install package.json requirements

### After you installed the project please use below link You should see me and my Awesome team: ###
    http://127.0.0.1:8000/team/





