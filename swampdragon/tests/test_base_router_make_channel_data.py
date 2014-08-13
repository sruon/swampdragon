from ..route_handler import BaseRouter
from .dragon_django_test_case import DragonDjangoTestCase


class FooRouter(BaseRouter):
    pass


class TestBaseRouter(DragonDjangoTestCase):
    def test_get_list(self):
        channel_data = FooRouter(self.connection).make_channel_data('client_chan', 'server_chan')
        expected = {'local_channel': 'client_chan', 'remote_channels': 'server_chan'}
        self.assertDictEqual(channel_data, expected)
