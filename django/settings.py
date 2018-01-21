
DEBUG = True
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lv',
)

ROOT_URLCONF = 'gzw.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'blog',
        'USER':'django',
        'PASSWORD':'123456',
        'HOST':'192.168.10.200',
        'PORT':'3306',
        'OPTIONS':{
                   'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
                   'charset':'utf8',
                   }
    }
}

LANGUAGE_CODE = 'zh-hans'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug':DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',  
            ],
        },
    },
]



python manage.py startapp booktest
python manage.py makemigrations
python manage.py migrate
python manage.py shell
