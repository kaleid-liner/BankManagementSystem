import os

SECRET_KEY = '!yg7z%-#nzuu)crl#y0c+_4-pa0_5(rp3v0e*-*i%as2h+ph_^'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
