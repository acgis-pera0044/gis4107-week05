def  is_point_in_box(x, y, xmin, ymin, xmax, ymax):
    if x>xmin and x<xmax:
        if y>ymin and y<ymax:
            return True
        else:
            False
    else:
        False
    