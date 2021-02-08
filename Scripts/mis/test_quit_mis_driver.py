from Base.driver import Driver
import pytest


@pytest.mark.run(order=200)
class TestQuitMisDriver:

    def test_quit_mis(self):
        """退出mis驱动driver"""
        Driver.quit_mis_driver()
