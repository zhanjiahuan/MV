import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-xk-mos#6=ybxlm#55w34fr#$3ieorh8#80_5fr2h2aze1k(tu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MY_APPS = [
    'apps.movies_api',
    'apps.common',
    'apps.account',
]

EXT_APPS = [
    'rest_framework',
    'corsheaders',
]

INSTALLED_APPS = SYSTEM_APPS + MY_APPS + EXT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movies.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'apps/account/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'movies.wsgi.application'

MYSQL_OPTIONS = {
    'sql_mode': 'TRADITIONAL',
    'charset': 'utf8',
    # 'init_command': 'SET default_storage_engine=INNODB',

}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'film',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '112.74.42.138',
        'PORT': '3306',
        'OPTION': MYSQL_OPTIONS,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 修改语言
LANGUAGE_CODE = 'zh-hans'
# 设置中国时区
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
# 是否使用django的时区
USE_TZ = False

STATIC_URL = '/static/'

# 当使用继承的方式重写auth模块的用户表的时候,
# 需要指定一下
# app的名字.用户类名
AUTH_USER_MODEL = 'account.User'

CORS_ORIGIN_ALLOW_ALL = True


# ===============发送邮箱配置==========
# 发送邮件的服务器地址
EMAIL_HOST = 'smtp.163.com'
# 发送邮件端口
EMAIL_PORT = 25
# 发送邮件默认的名称
EMAIL_HOST_USER = '15571383682@163.com'
# 授权码
EMAIL_HOST_PASSWORD = 'zhou123456'
# 是否启用tls安全协议
EMAIL_USE_TLS = True

# 是否启用SSL安全协议
# EMAIL_USE_SSL = True
# 发送超时时间
# EMAIL_TIMEOUT =

# ===============发送邮箱配置 end ==========
