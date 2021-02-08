from Base.driver import Driver
import pytest


@pytest.mark.run(order=100)
class TestQuitMp:

    def test_quit_mp(self):
        Driver.quit_mp_driver()
