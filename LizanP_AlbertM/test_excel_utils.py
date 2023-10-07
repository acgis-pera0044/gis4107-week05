import excel_utils as eu

def test_create_cell_refs1():
 columns = "A B"
 rows = "1 2"
 expection='A1,A2,B1,B2'
 actual = eu.create_cell_refs(columns, rows)
 assert expection==actual

def test_create_cell_refs2():
 columns = "A B C D"
 rows = "1 2 3"
 expection='A1,A2,A3,B1,B2,B3,C1,C2,C3,D1,D2,D3'
 actual = eu.create_cell_refs(columns, rows)
 assert expection==actual
