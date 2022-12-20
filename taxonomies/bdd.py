class_to_index = {
    'road': 0,
    'sidewalk': 1,
    'building': 2,
    'wall': 3,
    'fence': 4,
    'pole': 5,
    'traffic light': 6,
    'traffic sign': 7,
    'vegetation': 8,
    'terrain': 9,
    'sky': 10,
    'person': 11,
    'rider': 12,
    'car': 13,
    'truck': 14,
    'bus': 15,
    'train': 16,
    'motorcycle': 17,
    'bicycle': 18,
    'ignore': 19,
}

class_to_eval = {
    'road': True,
    'sidewalk': True,
    'building': True,
    'wall': True,
    'fence': True,
    'pole': True,
    'traffic light': True,
    'traffic sign': True,
    'vegetation': True,
    'terrain': True,
    'sky': True,
    'person': True,
    'rider': True,
    'car': True,
    'truck': True,
    'bus': True,
    'train': True,
    'motorcycle': True,
    'bicycle': True,
    'ignore': False,
}

mapping = {
    'road': [
        'road',
        'bike_lane',
        'crosswalk_plain',
        'zebra',
        'marking_other',
        'manhole',
        'pothole',
        'service_lane',
    ],
    'sidewalk': [
        'pavement',
        'curb_cut',
        'curb',
        'pedestrian_area',
    ],
    'building': [
        'building',
        'skyscraper',
        'house',
        'roof',
        'hovel',
        'tower',
    ],
    'wall': [
        'wall_brick',
        'wall_other',
        'wall_stone',
        'wall_tile',
        'wall_wood',
    ],
    'fence': [
        'fence'
    ],
    'pole': [
        'pole',
        'utility_pole',
        'pole_tl',
    ],
    'traffic light': [
        'traffic_light'
    ],
    'traffic sign': [
        'traffic_sign_front',
        'traffic_sign_back',
        'traffic_sign_frame',
    ],
    'vegetation': [
        'tree',
        'flower',
        'palm',
        'potted_plant',
    ],
    'terrain': [
        'grass',
        'land',
        'dirt',
        'field',
        'playing_field',
        'hill',
        'mountain',
    ],
    'sky': [
        'sky_other',
    ],
    'person': [
        'pedestrian',
        'tie'
    ],
    'rider': [
        'bicyclist',
        'motorcyclist',
        'rider_other',
    ],
    'car': [
        'car',
        'van',
        'pickup'
    ],
    'truck': [
        'truck'
    ],
    'bus': [
        'bus'
    ],
    'train': [
        'train',
    ],
    'motorcycle': [
        'motorcycle'
    ],
    'bicycle': [
        'bicycle'
    ],
    'ignore': [
        'ignore'
    ]
}
