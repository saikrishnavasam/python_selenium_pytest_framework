import os


class Environment:
    DEV = 'dev'
    QA = 'qa'

    URLS = {
        DEV: 'https://your-app.dev:2858/webapp/services/rest/',
        QA: 'https://your-app.qa:2858/webapp/services/rest/'
    }

    def __init__(self):
        self.name = self._get_environment_variable()

    @classmethod
    def _get_environment_variable(cls):
        try:
            return os.environ['ENVIRONMENT']
        except:
            return cls.QA

    def base_url(self):
        return self.URLS[self.QA]


ENV = Environment()
