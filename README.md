# settings.py

# 1. create a database called staff using postgresql

# change it if you need

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'staff',

        'USER': 'postgres',

        'PASSWORD': '',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}

# 2. python3 manage.py migrate

# 3. python3 manage.py runserver