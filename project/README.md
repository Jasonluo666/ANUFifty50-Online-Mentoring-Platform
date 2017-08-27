# ANU Fifty50 Website

ANU Fifty50 mentoring project.


## Quick Start


#### TL&DR: Quick Quickstart

You *must* be in the directory that contains `requirements.txt`.

The set of commands in a perfect world:

    # Windows start:
    pip install virtualenvwrapper-win

    # Linux/OSX start:
    pip install virtualenvwrapper

    mkvirtualenv Fifty50
    workon Fifty50
    pip install -r requirements.txt
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser

    ./manage.py runserver


Navigate to: [http:/127.0.0.1:8000](http:/127.0.0.1:8000)

### Install VirtualEnv/VirtualEnvWrapper

#### Windows

Install `virtualenvwrapper-win` using pip:

https://pypi.python.org/pypi/virtualenvwrapper-win

    # using pip
    pip install virtualenvwrapper-win

    # using easy_install
    easy_install virtualenvwrapper-win

    # from source
    git clone git://github.com/davidmarble/virtualenvwrapper-win.git
    cd virtualenvwrapper-win
    python setup.py install


#### OSX/Linux

Install `virtualenvwrapper`

    pip install virtualenvwrapper


### Create Virtual Environment

This is to make sure the project stays isolated and clean.

    mkvirtualenv Fifty50
    workon Fifty50



    virtualenv Fifty50


### Install Website Requirements

    pip install -r requirements.txt

It should take a minute or two to install all the necessary project requirements.


### Setup Django Website

Once-off create toy database to use for the purposes of development dummy data
and an admin login for yourself:

    ./manage.py migrate
    ./manage.py createsuperuser
    # ... Follow prompts to create user

*Note: If this doesn't work the permission on the project might be not-quite-right:*

    # If that doesn't work and permissions need fixing on manage.py
    chmod u+rwx manage.py

### Start Development Webserver

    ./manage.py runserver

From here you can navigate to [http:/127.0.0.1:8000](http:/127.0.0.1:8000) to view project.

To log in to site admin using credentials created above navigate to:
[http:/127.0.0.1:8000/admin/](http:/127.0.0.1:8000/admin/)

or specify URI and port to host publicly for other on your network.

    ./manage.py runserver 0.0.0.0:8000
    
### Login or Other Issues - Try this!
If you are having issues with logging in as a mentor/mentee/admin or with signing up, please
try this to fix the issue.
    
    1. Stop running the server
        CTRL + C (Windows)
        Control + C (Mac)
    2. Make Migrations
        ./manage.py makemigrations
        ./manage.py migrate
    3. Run the Server
        ./manage.py runserver
        
 ### CONTACT
 If you are having issues running the site, please log an issue with Github Issues OR
 contact: Nikita (u5830260@anu.edu.au) or Tyrus (u5800279@anu.edu.au)
