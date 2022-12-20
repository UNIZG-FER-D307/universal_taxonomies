class_to_index = {
    'building': 0,
    'tree': 1,
    'sky': 2,
    'car': 3,
    'sign': 4,
    'road': 5,
    'pedestrian': 6,
    'fence': 7,
    'column pole': 8,
    'sidewalk': 9,
    'bicyclist': 10,
    'ignore': 11
}

class_to_eval = {
    'building': True,
    'tree': True,
    'sky': True,
    'car': True,
    'sign': True,
    'road': True,
    'pedestrian': True,
    'fence': True,
    'column pole': True,
    'sidewalk': True,
    'bicyclist': True,
    'ignore': False,
}



mapping = {
    'road': [
        'bike_lane',
        'crosswalk_plain',
        'road',
        'service_lane',
        'zebra',
        'marking_other',
        'manhole',
        'pothole',
    ],
    'sidewalk': [
        'curb',
        'curb_cut',
        'pedestrian_area',
        'pavement',
    ],
    'building': [
        'building',
        'skyscraper',
        'house',
        'roof',
        'hovel',
        'tower',
        'trade_name',
        'door',
        'window',
        'banner',
        'phone_booth',
        'billboard',
        'bulletin_board',
        'potted_plant'
    ],
    'fence': [
        'fence',
    ],
    'column pole': [
        'pole',
        'utility_pole',
    ],
    'sign': [
        'traffic_sign_frame',
        'traffic_sign_back',
        'traffic_sign_front',
    ],
    'tree': [
        'tree',
    ],
    'sky': [
        'sky_other'
    ],
    'pedestrian': [
        'pedestrian',
    ],
    'bicyclist': [
        'bicyclist',
        'motorcyclist',
        'rider_other',
        'bicycle'
    ],
    'car': [
        'car',
        'pickup',
        'van',
        'bus',
        'truck',
        'train',
        'trailer',
        'caravan',
        'wheeled_slow',
        'vehicle_other'
    ],
    'ignore': [
        'ignore'
    ]
}
