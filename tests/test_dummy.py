import pytest

@pytest.mark.usefixtures('init_driver')
class TestDummy():

    def test_dummy(self):
        # self.driver.get('')
        # import pdb; pdb.set_trace()
        pass
