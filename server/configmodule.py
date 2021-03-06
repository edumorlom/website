"""Module contains Flask config for production and dev environment.
"""

import os
import datetime


class Config:
    TEST = False
    WEBDRIVER = False
    DEVELOPMENT = False
    CACHE_TYPE = 'simple'  # Flask-Caching related configs
    GAE_VERSION = (os.environ.get('GAE_VERSION') or
                   datetime.datetime.today().strftime("%m-%d-%H-%M"))
    API_PROJECT = ''
    GA_ACCOUNT = ''
    MAPS_API_KEY = ''


class ProductionConfig(Config):
    SECRET_PROJECT = 'factcheck-sandbox'
    API_PROJECT = 'datcom-mixer'
    API_ROOT = 'https://api.datacommons.org'
    GCS_BUCKET = 'datcom-browser-prod.appspot.com'
    GA_ACCOUNT = 'UA-117119267-1'


class StagingConfig(Config):
    SECRET_PROJECT = 'datcom-browser-staging'
    API_PROJECT = 'datcom-mixer-staging'
    API_ROOT = 'https://datacommons.endpoints.datcom-mixer-staging.cloud.goog'
    GCS_BUCKET = 'datcom-browser-staging.appspot.com'
    GA_ACCOUNT = 'UA-117119267-2'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SECRET_PROJECT = 'datcom-website-dev'
    API_PROJECT = 'datcom-mixer-staging'
    API_ROOT = 'https://datacommons.endpoints.datcom-mixer-staging.cloud.goog'
    GCS_BUCKET = 'datcom-browser-staging.appspot.com'


class MinikubeConfig(Config):
    DEVELOPMENT = True
    API_ROOT = 'http://127.0.0.1:8081'  # Port for Kubernetes ESP.


class GKEConfig(Config):
    API_ROOT = 'http://127.0.0.1:8081'  # Port for Kubernetes ESP.


class WebdriverConfig(Config):
    WEBDRIVER = True
    SECRET_PROJECT = 'datcom-website-dev'
    API_PROJECT = 'datcom-mixer-staging'
    API_ROOT = 'https://datacommons.endpoints.datcom-mixer-staging.cloud.goog'
    GCS_BUCKET = ''


class TestConfig(Config):
    TEST = True
    API_PROJECT = 'api-project'
    API_ROOT = 'api-root'
    GCS_BUCKET = 'gcs-bucket'
