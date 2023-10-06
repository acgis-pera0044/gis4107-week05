import lp_countdown as ctd

def test_get_countdown_as_text_using_for():
    expected = "10 9 8 7 6 5 4 3 2 1 0"
    actual = ctd.get_countdown_as_text_using_for()
    assert expected == actual

def test_get_countdown_as_text_using_for_5():
    start_value = 5
    expected = "5 4 3 2 1 0"
    actual = ctd.get_countdown_as_text_using_for(start_value)
    assert expected == actual

def test_get_countdown_as_text_using_while():
    expected = "10 9 8 7 6 5 4 3 2 1 0"
    actual = ctd.get_countdown_as_text_using_while()
    assert expected == actual

def test_get_countdown_as_text_using_while_5():
    start_value = 5
    expected = "5 4 3 2 1 0"
    actual = ctd.get_countdown_as_text_using_while(start_value)
    assert expected == actual