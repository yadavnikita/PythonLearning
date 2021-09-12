"""
preconditions
        login, signup,etc
test
test
assertion
postcondition
        logout, teardown

run - pytest test_fixtures.py -s

after yield write teardown condition


"""




import pytest

@pytest.fixture
def setup():
    print("test started")
    yield
    print("ended")

def test_1(setup):
    print("test1 executed")

def test_2(setup):
    print("test 2 executed")
