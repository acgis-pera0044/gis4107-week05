def create_cell_refs(columns, rows):
    index_rows = 0
    index_columns = 0
    length_rows = len(rows)
    length_columns = len(columns)
    final_result = ""
    for col in columns.split():
        for row in rows.split():
            if index_columns < length_columns:
                final_result += str(col)+str(row)+","
            elif index_columns >= length_columns and index_rows < length_rows:
                final_result += str(col)+str(row)+","
                index_rows += 3
            else:
                final_result += str(col)+str(row)
        index_columns += 3
             
    return final_result