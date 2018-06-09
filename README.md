# Schedular
(All rights are reserved by WIP TEAM)

### WIP Team ####

### Schedular Prototype Design (invision)###
 https://invis.io/KFHPP263PN9#/294229274_LoginForm
*^Click/hover over clickable elements to see the application workflow.^

### Schedular Final Design (invision)###
```
https://projects.invisionapp.com/share/QHKKKY0634P#/screens/302145854_LoginWithoutCredentials
```

### How do I get set up? ###
* First of all please install git, and clone this project If you don't know how please give up! Kaufland hires all the time.

* Install python and pip
```
$ sudo apt-get update
$ sudo apt upgrade
$ sudo apt install python2.7 python-pip
```
* Check if above was installed (if returns that it's not found try again maybe with root access)
```
python -V
pip -V
```

* Install virtualenv

```
pip install virtualenv (if not working try with sudo)
```

* Install mysql

```
sudo apt-get install mysql-client
sudo apt-get install mysql-server
mysql_secure_installation
or follow this steps:
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04/
```

* Now create a virtual environment

```
virtualenv env (can be used any name instead of env)
```

* Active your virtual environment (in root directory)

```
source env/bin/activate

deactivate  //(to deactivate your environment)
```
*  In your environment now you should install the requirements for our awesome project following the next command
please in project root directory

```
 cd schedular/
 pip install -r requirments.txt

```
* If something went wrong please follow the next commands (If all good you can skip this step)

```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
pip install mysqlclient
```
* Please create a mysql database, can be any name but it's recommended to use "scheduler" because next steps are involving this

```
mysql -u root -p
CREATE DATABASE scheduler;
show databases; // for showing your new database
exit;

```
* Now you can set database connection in settings.py but it's not recomanded, so please create a local_settings.py file in schedular child directory

```
cd schedular
```

local_settings.py should look like:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'schedular',
        'USER': 'root',
        'PASSWORD': 'Your_Password_for_abowe_user',
        'HOST': '',
        'PORT': '',
    }
}

```
Important note!: Please use your crdential and database!!!


* Now you should migrate the application structure in your database (o back to your root directory, where it's manage.py file) and run the following:

```
./manage.py makemigrations
./manage.py migrate
```

* If you want to have acces to our application please create an Super user using the following and complete the steps:

```
./manage.py createsuperuser
```

* Run the Server

If in your console doesn't appear:
```
Django version 1.11 , using settings 'schedular.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
Please try to install more times ... or ask someone else or me (hope not)

* Front End side
you must have npm install or please install it...
run:
```
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm

npm install
```
wait few second and all the setup is done! :D
Should install package.json requirements

### After you installed the project please use below link You should see me and my Awesome team: ###
    http://127.0.0.1:8000/team/





