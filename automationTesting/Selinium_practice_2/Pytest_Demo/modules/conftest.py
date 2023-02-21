import pytest

@pytest.fixture()  #Decorator
def setup():
    print("Lauching the browser ")
    print("Launching the application")
    yield
    print("\nClosing the Application and Browser")