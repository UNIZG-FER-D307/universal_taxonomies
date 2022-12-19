class_to_index = {
    'unlabeled': 0,
    'ego vehicle': 1,
    'rectification border': 2,
    'out of roi': 3,
    'static': 4,
    'dynamic': 5,
    'ground': 6,
    'road': 7,
    'sidewalk': 8,
    'parking': 9,
    'rail track': 10,
    'building': 11,
    'wall': 12,
    'fence': 13,
    'guard rail': 14,
    'bridge': 15,
    'tunnel': 16,
    'pole': 17,
    'polegroup': 18,
    'traffic light': 19,
    'traffic sign': 20,
    'vegetation': 21,
    'terrain': 22,
    'sky': 23,
    'person': 24,
    'rider': 25,
    'car': 26,
    'truck': 27,
    'bus': 28,
    'caravan': 29,
    'trailer': 30,
    'train': 31,
    'motorcycle': 32,
    'bicycle': 33,
    # 'license plate': -1
}

mapping = {
    'unlabeled': [
        'ignore'
    ],
    'ego vehicle': [
        'ego_vehicle'
    ],
    'rectification border': [
        'ignore'
    ],
    'out of roi': [
        'ignore'
    ],
    'static': [
        'ignore'
    ],
    'dynamic': [
        'ignore'
    ],
    'ground': [
        'ground'
    ],
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
        'floor_stone',
        'pedestrian_area',
    ],
    'parking': [
        'parking'
    ],
    'rail track': [
        'rail_track'
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
    'guard rail': [
        'railing',
        'bannister'
    ],
    'bridge': [
        'bridge'
    ],
    'tunnel': [
        'tunnel'
    ],
    'pole': [
        'pole',
        'utility_pole',
        'pole_tl',
    ],
    'polegroup': [
        'polegroup'
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
    'caravan': [
        'caravan'
    ],
    'trailer': [
        'trailer'
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
    # 'license plate': [
    #     'ignore'
    # ]
}

class_to_eval = {
    'unlabeled': False,
    'ego vehicle': False,
    'rectification border': False,
    'out of roi': False,
    'static': False,
    'dynamic': False,
    'ground': False,
    'road': True,
    'sidewalk': True,
    'parking': False,
    'rail track': False,
    'building': True,
    'wall': True,
    'fence': True,
    'guard rail': False,
    'bridge': False,
    'tunnel': False,
    'pole': True,
    'polegroup': False,
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
    'caravan': False,
    'trailer': False,
    'train': True,
    'motorcycle': True,
    'bicycle': True
}
