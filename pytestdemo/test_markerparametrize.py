import pytest
import sys


@pytest.mark.parametrize("user,name",
                         [("nikita","yadav"),
                          ("nihal","yadav")])
def test_para(user,name):
    print(user)
    print(name)
