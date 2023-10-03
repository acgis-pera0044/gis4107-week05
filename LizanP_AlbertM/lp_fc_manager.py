def get_feature_type(feature_code):
    if feature_code == 1:
        return "POINT"
    elif feature_code == 2:
        return "POLYLINE"
    elif feature_code == 3:
        return "POLYGON"
    else:
        return "None"