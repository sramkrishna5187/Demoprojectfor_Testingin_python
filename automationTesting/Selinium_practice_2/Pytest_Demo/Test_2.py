import pytest

class TestClass:
    @pytest.fixture()   #Decorator
    def setup(self):
        print("Laucnching browser...")
        print("Opening the application")

    def test_login(self,setup):
        print("login was completed")

    def test_search(self,setup):
        print("The task is search")

    def test_advsearch(self,setup):
        print("The task advsearch completed")