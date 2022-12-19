class_to_index = {
    'road':  0,
    'parking':  1,
    'drivable fallback':  2,
    'sidewalk':  3,
    'rail track':  4,
    'non-drivable fallback':  5,
    'person':  6,
    'animal':  7,
    'rider':  8,
    'motorcycle':  9,
    'bicycle': 10,
    'autorickshaw': 11,
    'car': 12,
    'truck': 13,
    'bus': 14,
    'caravan': 15,
    'trailer': 16,
    'train': 17,
    'vehicle fallback': 18,
    'curb': 19,
    'wall': 20,
    'fence': 21,
    'guard rail': 22,
    'billboard': 23,
    'traffic sign': 24,
    'traffic light': 25,
    'pole': 26,
    'polegroup': 27,
    'obs-str-bar-fallback': 28,
    'building': 29,
    'bridge': 30,
    'tunnel': 31,
    'vegetation': 32,
    'sky': 33,
    'fallback background': 34,
    'unlabeled': 35,
    'ego vehicle': 36,
    'rectification border': 37,
    'out of roi': 38,
    'license plate': 39,
    'ignore': 40
}

class_to_eval = {
    'road': True,
    'parking': True,
    'drivable fallback': True,
    'sidewalk': True,
    'rail track': True,
    'non-drivable fallback': True,
    'person': True,
    'animal': False,
    'rider': True,
    'motorcycle': True,
    'bicycle': True,
    'autorickshaw': True,
    'car': True,
    'truck': True,
    'bus': True,
    'caravan': False,
    'trailer': False,
    'train': False,
    'vehicle fallback': True,
    'curb': True,
    'wall': True,
    'fence': True,
    'guard rail': True,
    'billboard': True,
    'traffic sign': True,
    'traffic light': True,
    'pole': True,
    'polegroup':True,
    'obs-str-bar-fallback': True,
    'building': True,
    'bridge': True,
    'tunnel': True,
    'vegetation': True,
    'sky': True,
    'fallback background': True,
    'unlabeled': False,
    'ego vehicle': False,
    'rectification border': False,
    'out of roi': False,
    'license plate': False,
    'ignore': False
   }

mapping = {
    'ego vehicle': [
        'ego_vehicle'
    ],
    'rectification border': [
        'ignore'
    ],
    'out of roi': [
        'ignore'
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
        'floor_stone',
        'pedestrian_area',
    ],
    'curb': [
        'curb',
        'curb_cut'
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
    ],
    'bridge': [
        'bridge'
    ],
    'tunnel': [
        'tunnel'
    ],
    'pole': [
        'pole',
        'utility_pole'
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
    'sky': [
        'sky_other',
    ],
    'person': [
        'pedestrian'
    ],
    'animal': [
        'bird',
        'cat',
        'dog',
        'horse',
        'sheep',
        'cow',
        'elephant',
        'bear',
        'zebra_animal',
        'giraffe'
    ],
    'rider': [
        'bicyclist',
        'motorcyclist',
        'rider_other',
    ],
    'car': [
        'car',
        'van',
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
    'billboard': [
        'billboard'
    ],
    'unlabeled': [
        'ignore'
    ],
    'license plate': [
        'ignore'
    ],
    'autorickshaw': [
        'autorickshaw'
    ],
    'vehicle fallback': [
        'vehicle_other',
        'wheeled_slow'
    ],
    'obs-str-bar-fallback': [
        'bannister'
    ],
    'drivable fallback': [
        'drivable_fallback'
    ],
    'non-drivable fallback': [
        'grass',
        'moss',
        'land',
        'dirt',
        'mud',
        'field',
        'playing_field',
        'straw',
        'hill',
        'mountain',
        'ground'
    ],
    'polegroup': [
        'polegroup'
    ],
    'fallback background': [
        'fallback_background'
    ],
    'ignore': [
        'ignore'
    ]
}

