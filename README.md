# Córdoba Sounds

A website for collecting sound samples from Córdoba, Argentina and other cities.


## Running

Install the system deps, you are going to need Python 3 and MongoDB.

Install requirements and the app as usual:

    $ pip -r requirements.txt
    $ pip install .

Configure your environment, you need to export some settings (check settings.py)

* MONGOLAB_URI: The URI for your mongo db instance
* MAIL_SERVER: Your mail server (The user system needs this)
* MAIL_PORT: The port your mail server is listening to
* MAIL_USERNAME: The username or your mail server
* MAIL_PASSWORD: The password for your mail server

Now you can run the development server:

    $ python3 cba_sounds/app.py


## Deploying

TBD


## Credits

* Rodrigo Bistolfi
* Sebastián Coca
* EF - Escuela de Fonoaudiología
* CIAL - Centro de Investigaciones Acústicas y Luminotécnicas
* UNC - Universidad Nacional de Córdoba
