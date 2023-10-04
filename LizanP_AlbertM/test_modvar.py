import modvar as mdv

def test_mod_myvar_condition_1():
    expected = 5
    var = 1
    actual = mdv.mod_myvar(var)
    assert expected == actual

def test_mod_myvar_condition_2():
    expected = 2
    var = 3
    actual = mdv.mod_myvar(var)
    assert expected == actual

def test_mod_myvar_condition_3():
    expected = 4
    var = 2
    actual = mdv.mod_myvar(var)
    assert expected == actual

def test_mod_myvar_condition_4():
    expected = 10
    var = 12
    actual = mdv.mod_myvar(var)
    assert expected == actual
