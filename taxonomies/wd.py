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
    'pickup': 34,
    'van': 35,
    'billboard': 36,
    'street-light': 37,
    'road-marking': 38
}

mapping = {
    "person": [
        'pedestrian',
        'tie'
    ],
    "rider": [
        'bicyclist',
        'motorcyclist',
        'rider_other'
    ],
    "car": [
        'car'
    ],
    "truck": [
        'truck'
    ],
    "trailer": [
        'trailer'
    ],
    "bus": [
        'bus'
    ],
    "train": [
        'train'
    ],
    "motorcycle": [
        'motorcycle'
    ],
    "bicycle": [
        'bicycle'
    ],
    "pickup": [
        'pickup'
    ],
    "van": [
        'van'
    ],
    "caravan": [
        'caravan'
    ],
    "ego vehicle": [
        'ego_vehicle'
    ],
    "sky": [
        'sky'
    ],
    "ground": [
        'ground'
    ],
    "terrain": [
        'grass',
        'land',
        'field',
        'hill',
        'mountain'
        'dirt',
        'field',
        'playing_field',
        'gravel',
        'rock',
    ],
    "vegetation": [
        'tree',
        'flower',
        'palm',
        'potted_plant',
    ],
    "building": [
        'building',
        'skyscraper',
        'house',
        'roof',
        'hovel',
        'tower'
    ],
    "bridge": [
        'bridge'
    ],
    "tunnel": [
        'tunnel'
    ],
    "wall": [
        'wall',
    ],
    "fence": [
        'fence'
    ],
    "guard rail": [
        'railing',
        'bannister'
    ],
    "parking": [
        'parking'
    ],
    "rail track": [
        'rail_track'
    ],
    "road": [
        'road',
        'bike_lane',
        'crosswalk_plain',
        'manhole',
        'pothole',
        'service_lane'
    ],
    "road-marking": [
        'zebra',
        'marking_other'
    ],
    "sidewalk": [
        'pavement',
        'curb_cut',
        'curb',
        'pedestrian_area'
    ],
    "pole": [
        'pole',
        'utility_pole',
        'pole_tl'
    ],
    "street-light": [
        'street_light'
    ],
    "traffic light": [
        'traffic_light'
    ],
    "billboard": [
        'billboard'
    ],
    "traffic sign": [
        'traffic_sign_front',
        'traffic_sign_back',
        'traffic_sign_frame'
    ],
    "unlabeled": [
        "ignore"
    ],
    "rectification border": [
        "ignore"
    ],
    "out of roi": [
        "ignore"
    ],
    "static": [
        "ignore"
    ],
    "dynamic": [
        "ignore"
    ],
    "polegroup": [
        "ignore"
    ]
}

class_to_eval = {
    'unlabeled': False,
    'ego vehicle': True,
    'rectification border': False,
    'out of roi': False,
    'static': False,
    'dynamic': False,
    'ground': False,
    'road': True,
    'sidewalk': True,
    'parking': True,
    'rail track': True,
    'building': True,
    'wall': True,
    'fence': True,
    'guard rail': True,
    'bridge': True,
    'tunnel': True,
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
    'caravan': True,
    'trailer': True,
    'train': True,
    'motorcycle': True,
    'bicycle': True,
    'pickup': True,
    'van': True,
    'billboard': True,
    'street-light': True,
    'road-marking': True
}
