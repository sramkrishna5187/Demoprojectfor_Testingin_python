import pytest


class TestClass:
    @pytest.mark.dependency()
    def test_openApp(self):
        print("This is open application module")
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_openApp'])
    def test_Login(self):
        print("This is login method")

    @pytest.mark.dependency(depends=['TestClass::test_openApp'])
    def test_Search(self):
        print("This is method Search")

    @pytest.mark.dependency(depends=['TestClass::test_openApp'])
    def test_advsearch(self):
        print("This is method Advanced search")

    @pytest.mark.dependency(depends=['TestClass::test_advsearch'])
    def test_updatevalues(self):
        print("This is method To update new values")

