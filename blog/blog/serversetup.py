DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '42.193.187.243',  # 数据库主机
        'PORT': 8306,  # 数据库端口
        'USER': 'blogdjango',  # 数据库用户名
        'PASSWORD': 'heimapeixun666',  # 数据库用户密码
        'NAME': 'blog'  # 数据库名字1
    },
}

CACHES = {
    "default": {  # 默认
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://42.193.187.243:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {  # session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://42.193.187.243:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

