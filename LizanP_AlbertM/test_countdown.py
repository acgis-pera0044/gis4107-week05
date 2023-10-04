def get_countdown_as_text_using_for(start_value=10):
    """
       Using for loop to countdwon number from start_value to 0    
       start_value (int, optional): mark the start point of the number, default value is 10
    """
    for i in range(start_value,-1,-1):
      print("\ncountdown using for :",i)

get_countdown_as_text_using_for()
#using default value 10

get_countdown_as_text_using_for(5)
#using argument value

def get_countdown_as_text_using_while(start_value=10):
    """
       Using while loop to countdwon number from start_value to 0    
       start_value (int, optional): mark the start point of the number, default value is 10
    """

    while(start_value>=0):
       print("\ncountdown using while :",start_value)
       start_value-=1

get_countdown_as_text_using_while()
#using default value 10

get_countdown_as_text_using_while(5)
#using argument value




