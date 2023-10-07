
def get_countdown_as_text_using_for(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a for loop
    """
    countdown_string = ""
    for number in range(0, start_value+1):
        modified_value = start_value - number
        if modified_value > 0:
            countdown_string += str(modified_value) + " "
        else:
            countdown_string += str(modified_value)
    return countdown_string

def get_countdown_as_text_using_while(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a while loop
    """
    modified_value = start_value
    countdown_string = ""
    while modified_value >= 0:
        if modified_value > 0:
            countdown_string += str(modified_value) + " "
        else:
            countdown_string += str(modified_value)
        modified_value -= 1
    return countdown_string
