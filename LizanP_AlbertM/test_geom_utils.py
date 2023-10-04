import geom_utils as gu

def test_is_point_in_box_left_of_box():
    expected = False
    x = 2
    y = 7
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual


def test_is_point_in_box_on_left_edge():
    expected = False
    x = 5
    y = 8
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual


def test_is_point_in_box_above_box():
    expected = False
    x = 7
    y = 13
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual


def test_is_point_in_box_on_top_edge():
    expected = False
    x = 8
    y = 12
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual


def test_is_point_in_box_right_of_box():
    expected = False
    x = 11
    y = 11
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_on_right_edge():
    expected = False
    x = 10
    y = 8
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_below_box():
    expected = False
    x = 7
    y = 5
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_on_bottom_edeg():
    expected = False
    x = 7
    y = 6
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_in_box():
    expected = True
    x = 8
    y = 10
    xmin = 5
    xmax = 10
    ymin = 6
    ymax = 12
    actual = gu.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    assert expected == actual