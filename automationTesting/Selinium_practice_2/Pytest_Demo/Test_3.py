import pytest

class TestClass:
    @pytest.fixture() #decorate
    def setup(self):
        print("Lauching the browser")
        print("Invoking the application")
        yield
        print("closing the browser completed sucessfully")

    def test_login(self,setup):
        print("Login task completed sucessfully")

    def test_search(self,setup):
        print("search task completed successfully")

    def test_advsearch(self,setup):
        print ("The advanced serach task completed sucessfully")
