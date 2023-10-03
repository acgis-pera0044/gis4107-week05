import lp_fc_manager as lfm

def test_get_feature_type_fc_1_is_point():
    expected = "POINT"
    feature_code = 1
    actual = lfm.get_feature_type(1)
    assert expected == actual


def test_get_feature_type_fc_2_is_polyline():
    expected = "POLYLINE"
    feature_code = 2
    actual = lfm.get_feature_type(2)
    assert expected == actual


def test_get_feature_type_fc_3_is_polygon():
    expected = "POLYGON"
    feature_code = 3
    actual = lfm.get_feature_type(feature_code)
    assert expected == actual 


def test_get_feature_type_fc_another_is_none():
    expected = "None"
    feature_code = 4
    actual = lfm.get_feature_type(feature_code)
    assert expected == actual 

test_get_feature_type_fc_1_is_point()