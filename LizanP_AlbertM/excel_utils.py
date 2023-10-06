def create_cell_refs(columns,rows):

    column_list = columns.split() 
    row_list = rows.split()  

    cell_refs = []

    for column in column_list:
        for row in row_list:
            cell_refs_element = f"{column}{row}"  

            #To use append, the array need to be a list format
            cell_refs.append(cell_refs_element)

    #function join will destroy the format of a list, the returning value will be transferred into a string linking with ','
    return ','.join(cell_refs)
    

