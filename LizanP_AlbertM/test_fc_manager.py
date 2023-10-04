import fc_manager as fm

def test_get_feature_type_1_is_point():
    expected = "POINT"
    feature_code = 1
    actual = fm.get_feature_type(feature_code)
    assert expected == actual

def test_get_feature_type_2_is_polyline():
    expected = "POLYLINE"
    feature_code = 2
    actual = fm.get_feature_type(feature_code)
    assert expected == actual

def test_get_feature_type_3_is_polygon():
    expected = "POLYGON"
    feature_code = 3
    actual = fm.get_feature_type(feature_code)
    assert expected == actual

def test_get_feature_type_4_is_others():
    expected = "None"
    feature_code = 4
    actual = fm.get_feature_type(feature_code)
    assert expected == actual