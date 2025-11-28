import os

# --- A MÁGICA PARA A TELA APARECER ---
# Isso obriga o Django a servir o CSS e JS
DEBUG = True
# Permite acesso de qualquer lugar
ALLOWED_HOSTS = ['*']

# Configurações básicas
ADMINS = [('Admin', 'root@localhost')]
SECRET_KEY = 'tcc-fatec-segredo-2025'
AWX_PROJ_DIR = '/var/lib/awx/projects'

# Banco de Dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'awx',
        'USER': 'awx',
        'PASSWORD': 'awxpassword',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# Redis
BROKER_URL = 'redis://redis:6379/0'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

# Identificação do Cluster
CLUSTER_HOST_ID = "awx-docker"
SYSTEM_UUID = "00000000-0000-0000-0000-000000000000"
