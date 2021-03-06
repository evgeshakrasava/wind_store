import os
from .auth_vk import SOCIAL_AUTH_VK_OAUTH2_KEY,SOCIAL_AUTH_VK_OAUTH2_SECRET
from .auth_facebook import SOCIAL_AUTH_FACEBOOK_OAUTH2_KEY,SOCIAL_AUTH_FACEBOOK_OAUTH2_SECRET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'r=nrc5s9mg8mnz-3l2sz9s=4010uyv_h$w-(&6e7t%26izqpo*'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'wind_cart.apps.WindCartConfig',
    'crispy_forms',
    'user.apps.UserConfig',
    'shop',
    'products.apps.ProductsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'social_django',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'
#TEMPLATE_DIR =  os.path.join(os.path.dirname(__file__) ,'../templates').replace('\\','/')
AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',          # бекенд авторизации через ВКонтакте
    'django.contrib.auth.backends.ModelBackend', # бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
)



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'



# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_PATH='/static/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL='home'
LOGIN_URL = 'login'
CART_PRODUCT_MODEL = 'products.models.Product'
CART_SESSION_ID = 'cart'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_VK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}
