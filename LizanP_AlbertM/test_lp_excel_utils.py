import lp_excel_utils as eu

def test_create_cell_refs_1():
    columns = "A B"
    rows= "1 2"
    expected = "A1,A2,B1,B2"
    actual = eu.create_cell_refs(columns, rows)
    assert expected == actual

def test_create_cell_refs_2():
    columns = "A B C"
    rows= "1 2"
    expected = "A1,A2,B1,B2,C1,C2"
    actual = eu.create_cell_refs(columns, rows)
    assert expected == actual

def test_create_cell_refs_3():
    columns = "A B"
    rows= "1 2 3"
    expected = "A1,A2,A3,B1,B2,B3"
    actual = eu.create_cell_refs(columns, rows)
    assert expected == actual