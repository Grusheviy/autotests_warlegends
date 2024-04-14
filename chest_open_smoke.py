from testing.cases.common.one_time_set_up import one_time_set_up
from alt_tester_python.base_test_case import BaseTestCase
from testing.cases.chest_open.smoke.battery_chest_open import battery_chest_open_script


class ChestOpenTestCase(BaseTestCase):

    client_count = 1

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        one_time_set_up(cls.clients[0].wrapper, request_gold=1234)

    def setUp(self):
        super().setUp()
        self.clients[0].wrapper.set_up(is_active_skip=False)

    def test_01_battery_chest_open(self):
        battery_chest_open_script(self, self.clients[0].wrapper)

    def tearDown(self):
        super().tearDown()
        self.clients[0].wrapper.tear_down()
