from os import getenv

import sys


class Config(object):
    """App base configuration"""

    # FLASK_ENV Configuration
    FLASK_ENV = getenv('FLASK_ENV')


class ProductionConfig(Config):
    """App production configuration."""


class DevelopmentConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    """App staging configuration."""


class TestingConfig(Config):
    """App testing configuration."""

    TESTING = True
    FLASK_ENV = 'testing'


config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

AppConfig = TestingConfig if 'pytest' in sys.modules else config.get(
    getenv('FLASK_ENV'), 'development')
