from falcon import testing

import src.app as myapp
import src.conf as settings


class BaseTest(testing.TestCase):
    def setUp(self):
        super(BaseTest, self).setUp()

        self.headers = {'TOKEN': settings.SECRET_KEY}
        self.app = myapp.create_app()