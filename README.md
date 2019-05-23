## Starting app

    $ python manage.py runserver

The app will be served by django **runserver**

Access it through **http://localhost:8000**

## Setup of development environment with virtualenvwrapper

First install required dependencies:

    $ sudo apt install git virtualenvwrapper

Now, from your projects folder, clone this project:

    $ git clone https://github.com/atleyvarghese/slack-api.git

If this steps gives you an error, it means you add an SSH key to your user
you can get how [here](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

Set WORKON_HOME to your virtualenv dir

    $ export WORKON_HOME=~/.virtuals

Add this line to the end of ~/.bashrc so that the virtualenvwrapper commands are loaded.

    $ . /usr/share/virtualenvwrapper/virtualenvwrapper.sh

Exit and re-open your shell, or reload .bashrc with the command **source ~/.bashrc** and you’re ready to go.

After that, create your virtualenv:

    $ mkvirtualenv -p $(which python3.5) salck-api-env

Now, you can access it with:

    $ workon salck-api-env

And to start the django dev server:

    $ ./manage.py runserver


Install the package requirements form requirements file 

    $ pip install -r requirements.txt