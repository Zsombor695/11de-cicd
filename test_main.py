from main import divide

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
    assert divide(11, 2) == 5.5