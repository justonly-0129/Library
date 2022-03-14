## Run project (2022/3/14)

```bash
$ # Download
$ git clone https://github.com/yaozeliang/Library.git
$ cd Library

$ # Install vierual environment
$ pip install virtualenv
$ virtualenv envname

$ # Activae virtual env
$ envname\scripts\activate

$cd ../..
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application 
$ python manage.py runserver 

```
