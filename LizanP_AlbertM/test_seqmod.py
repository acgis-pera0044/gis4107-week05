import seqmod as sqm

def test_mod_sequence_1():
    expected = "ABCD"
    actual = sqm.mod_sequence("ABCD")
    assert expected == actual

def test_mod_sequence_2():
    expected = "BCD"
    actual = sqm.mod_sequence("ABCD", 0)
    assert expected == actual

def test_mod_sequence_3():
    expected = "ACD"
    actual = sqm.mod_sequence("ABCD", 1)
    assert expected == actual

def test_mod_sequence_4():
    expected = "A"
    actual = sqm.mod_sequence("ABCD", 1, 2)
    assert expected == actual

def test_mod_sequence_5():
    expected = "AB"
    actual = sqm.mod_sequence("ABCD", 2, 2)
    assert expected == actual

def test_mod_sequence_6():
    expected = "AB"
    actual = sqm.mod_sequence("ABCD", 3, 2)
    assert expected == actual

def test_mod_sequence_7():
    expected = "ABCD"
    actual = sqm.mod_sequence("ABCD", 4)
    assert expected == actual

def test_mod_sequence_8():
    expected = "ABCD"
    actual = sqm.mod_sequence("ABCD", truncate_index=4)
    assert expected == actual

def test_mod_sequence_9():
    expected = "ACD"
    actual = sqm.mod_sequence("ABCD", 1, 4)
    assert expected == actual