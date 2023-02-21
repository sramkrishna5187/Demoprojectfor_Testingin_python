import pytest

class Testclass():
    @pytest.mark.third
    def test_methodC(self):
        print("This is test method c")
    @pytest.mark.fourth
    def test_methodD(self):
        print("this is test method D")
    @pytest.mark.first
    def test_methodA(self):
        print("This is test method A")
    @pytest.mark.second
    def test_methodB(self):
        print ("This is test method B")


    @pytest.mark.fifth
    def test_mehtodE(self):
        print("this is test method E")