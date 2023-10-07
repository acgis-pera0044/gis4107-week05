import countdown as cd
 
def test_countdown_using_for_default():
    expection='10 9 8 7 6 5 4 3 2 1 0'
    actual=cd.get_countdown_as_text_using_for()
    assert expection==actual

def test_countdown_using_for_value():
    expection='5 4 3 2 1 0'
    actual=cd.get_countdown_as_text_using_for(5)
    assert expection==actual
    

def test_countdown_using_while_default():
    expection='10 9 8 7 6 5 4 3 2 1 0'
    actual=cd.get_countdown_as_text_using_while()
    assert expection==actual

def test_countdown_using_while_value():
    expection='5 4 3 2 1 0'
    actual=cd.get_countdown_as_text_using_while(5)
    assert expection==actual



