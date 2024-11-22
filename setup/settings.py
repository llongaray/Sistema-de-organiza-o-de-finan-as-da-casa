"""
Configurações do Django para o projeto setup.

Este arquivo contém todas as configurações principais do Django para o projeto.
Inclui configurações de segurança, banco de dados, internacionalização,
arquivos estáticos e muito mais.

Gerado inicialmente por 'django-admin startproject' usando Django 5.1.3.

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/en/5.1/topics/settings/

Para a lista completa de configurações e seus valores, veja:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# BASE_DIR: Caminho base do projeto
# Usa Path para garantir compatibilidade entre diferentes sistemas operacionais
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações de Desenvolvimento
# Estas configurações são adequadas apenas para desenvolvimento
# Para ambiente de produção, consulte:
# https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# AVISO DE SEGURANÇA: Esta chave deve ser mantida em segredo e alterada em produção!
SECRET_KEY = os.getenv('SECRET_KEY')

# DEBUG: Controla o modo de depuração do Django
# Em produção, deve ser definido como False para evitar exposição de informações sensíveis
DEBUG = True

# ALLOWED_HOSTS: Lista de hosts/domínios permitidos para este site
# Lista vazia permite apenas localhost. Em produção, adicione seus domínios.
ALLOWED_HOSTS = ['127.0.0.1', '192.168.18.171', '0.0.0.0']


# Aplicações Instaladas
# Lista de todas as aplicações Django ativas neste projeto

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.financas.apps.FinancasConfig',
    'apps.users.apps.UsersConfig',
]

# Middleware
# Componentes que processam requisições/respostas globalmente
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # Segurança
    'django.contrib.sessions.middleware.SessionMiddleware',  # Gerenciamento de sessões
    'django.middleware.common.CommonMiddleware',            # Funcionalidades comuns
    'django.middleware.csrf.CsrfViewMiddleware',            # Proteção CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Sistema de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Proteção contra clickjacking
]

# Configuração principal de URLs
ROOT_URLCONF = 'setup.urls'

# Configurações de Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '.templates'),
            os.path.join(BASE_DIR, '.templates/apps'),
            os.path.join(BASE_DIR, '.templates/partials'),
        ],
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

# Configuração da aplicação WSGI
WSGI_APPLICATION = 'setup.wsgi.application'


# Configuração do Banco de Dados
# SQLite é usado por padrão. Para produção, considere PostgreSQL ou MySQL
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Arquivo do banco SQLite
    }
}


# Validadores de Senha
# Configurações para garantir senhas fortes e seguras
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Evita senhas similares aos dados do usuário
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Garante comprimento mínimo
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Evita senhas comuns
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Evita senhas apenas numéricas
    },
]


# Configurações de Internacionalização
# Define idioma, fuso horário e formatação local
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'    # Código do idioma padrão

TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário padrão

USE_I18N = True           # Ativa tradução de strings

USE_TZ = True            # Ativa suporte a fuso horário

# Configuração de Arquivos Estáticos
# Arquivos CSS, JavaScript, Imagens etc.
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'    # URL base para arquivos estáticos

# Diretório onde o comando collectstatic irá coletar os arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Diretórios adicionais onde o Django procurará arquivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/css'),
    os.path.join(BASE_DIR, 'static/js'),
    os.path.join(BASE_DIR, 'static/imgs'),
    os.path.join(BASE_DIR, 'static/files'),
]

# Configuração do Tipo de Campo Automático para Chaves Primárias
# Define BigAutoField como padrão para maior escalabilidade
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = 'users:login'  # Atualizar para usar o namespace do app users
LOGIN_REDIRECT_URL = 'financas:dashboard'
LOGOUT_REDIRECT_URL = 'users:login'
