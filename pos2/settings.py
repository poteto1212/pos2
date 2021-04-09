import os
from django.contrib.messages import constants as messages
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vwf^#7wqy7ygytg@t$qvi)q!a8z&9a!$z2bfzt)-f%xv3#ybrr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'timeline.apps.TimelineConfig',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    #'allauth.socialaccount',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pos2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'pos2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#staticを取り扱う際のURL
STATIC_URL = '/static/'
#静的コンテンツの読み取り場所を指定(BASE_DIRとstaticを同一パスとして扱う)
#複数形にし忘れるとstaticが全て適用されなくなる。
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
    )

#アップロードファイルの保存先を指定(BASE_DIRとmediaを同一パスとして扱う)
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
#mediaを取り扱う際のurl
MEDIA_URL='/media/'

MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


AUTH_USER_MODEL='accounts.CustomUser'

#メールアドレスでのユーザー認証システム
SITE_ID=1
AUTHENTICATION_BACKENDS=(
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
    )
#メールアドレスとパスワードでの認証　アカウント認証時の自動承認
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = 'timeline:index'#ログイン時のリダイレクトURL設定
ACCOUNT_LOGOUT_REDIRECT_URL='account_login'#ログアウト時のリダイレクトURL設定
ACCOUNT_EMAIL_SUBJECT_PREFIX=''#メールタイトルの接頭辞を指定
ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'
DEFAULT_FROM_EMAIL='admin@example.com'
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'#コンソールでの試験的なメールを確認にする










