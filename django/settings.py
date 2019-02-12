
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
    
    
BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    'formatters': {
        # 详细的日志格式
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },
    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        # 在终端打印
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'simple'
        },
        # 默认的
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 3,  # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 专门用来记错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 专门定义一个收集特定信息的日志
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {
       # 默认的logger应用如下配置
        '': {
            'handlers': ['default', 'console', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向更高级别的logger传递
        },
        # 名为 'collect'的logger还单独处理
        'collect': {
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        }
    },
}

views.py里使用

import logging
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")
 
def index(request):
    logger.debug("一个萌萌的请求过来了。。。。")
    logger.info("一个更萌的请求过来了。。。。")
    logger.debug("这是app01里面的index视图函数")
 
    collect_logger.info("用户1:河南")
 
    return HttpResponse("OK")







