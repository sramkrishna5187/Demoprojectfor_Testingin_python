# This is test_SignUp.py

import pytest

class TestSignUp():

    def test_SignUpByEmail(self,setup):
        print("This is signup by email method")
        assert True==True


    def test_SignUpByFacebook(self,setup):
        print("This is signup by facebook")
        assert True == True


    def test_SignUpByTwitter(self,setup):
        print("This is signup by Twitter")
        assert True==True
