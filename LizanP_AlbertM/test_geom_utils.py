import geom_utils as gu

def test_is_point_in_box_left_of_box():
    expected=False
    x=2
    y=7
    xmin=5
    xmax=10
    ymin=6
    ymax=12
    actual=gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected==actual