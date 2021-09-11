import pytest
import sys

@pytest.mark.smile
def test_login():
    print("login done")

@pytest.mark.skipif(sys.version_info<(3,9), reason="python version not supported")
def test_add_prod():
    print("add products")

@pytest.mark.xfail
def test_logout():
    assert True # just put assert true /false for xpass and xfail results
    print("logout done")

