def test_1():
    x=10
    y=10
    assert x==y

def test_2():
    name = "selenium"
    title = "selenium is for web automation"
    assert name in title

def test_3():
    name = "jenkis"
    title = "jenkis is ci server"
    assert name is title , "title does not match"