
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

STATICFILES_DIRS=[
  os.path.join(BASE_DIR,'static')
]
#新建static目录和manage.py平级

python manage.py startapp booktest
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py sqlmigrate polls 0001


#django 使用pymysql 
import pymysql
pymysql.install_as_MySQLdb()

#sqlmigrate的命令可以展示SQL语句
python manage.py sqlmigrate polls 0001

主键 (IDs) 是自动添加的 你也可以重写此行为
Django 会在外键字段名上附加 "_id" 。 (你仍然可以重写此行为。)

# 创建一个新的question对象
    # Django推荐使用timezone.now()代替python内置的datetime.datetime.now()
    # 这个timezone就来自于Django唯一的依赖库pytz
    from django.utils import timezone
    >>> q = Question(question_text="What's new?", pub_date=timezone.now())
    
    








