class_to_index = {
    'unlabeled': 0,
    'ambiguous': 1,
    'sky': 2,
    'road': 3,
    'sidewalk': 4,
    'railtrack': 5,
    'terrain': 6,
    'tree': 7,
    'vegetation': 8,
    'building': 9,
    'infrastructure': 10,
    'fence': 11,
    'billboard': 12,
    'trafficlight': 13,
    'trafficsign': 14,
    'mobilebarrier': 15,
    'firehydrant': 16,
    'chair': 17,
    'trash': 18,
    'trashcan': 19,
    'person': 20,
    'animal': 21,
    'bicycle': 22,
    'motorcycle': 23,
    'car': 24,
    'van': 25,
    'bus': 26,
    'truck': 27,
    'trailer': 28,
    'train': 29,
    'plane': 30,
    'boat': 31,
}

mapping = {
    'unlabeled': [
        'ignore'
    ],
    'ambiguous': [
        'ignore'
    ],
    'sky': [
        'sky_other',
    ],
    'road': [
        'road',
        'bike_lane',
        'crosswalk_plain',
        'parking',
        'manhole',
        'pothole',
        'service_lane',
        'zebra',
        'marking_other',
    ],
    'sidewalk': [
        'pavement',
        'curb_cut',
        'curb',
        'pedestrian_area',
    ],
    'railtrack': [
        'rail_track'
    ],
    'terrain': [
        'ground',
        'grass',
        'land',
        'field',
        'hill',
        'mountain',
    ],
    'tree': [
        'tree'
    ],
    'vegetation': [
        'flower',
        'palm',
        'potted_plant',
    ],
    'building': [
        'building',
        'skyscraper',
        'house',
        'roof',
        'hovel',
        'tower',
    ],
    'infrastructure': [
        'bridge',
        'tunnel',
        'tent',
        'pier',
        'column',
        'phone_booth',
        'stairway',
        'steps',
        'stair',
        'escalator',
        'fountain',
        'swimming pool',
        'wall_brick',
        'wall_other',
        'wall_stone',
        'wall_tile',
        'wall_wood'
    ],
    'fence': [
        'fence',
        'railing',
        'bannister',
    ],
    'billboard': [
        'billboard'
    ],
    'trafficlight': [
        'traffic_light'
    ],
    'trafficsign': [
        'traffic_sign_front',
        'traffic_sign_back',
        'traffic_sign_frame',
    ],
    'mobilebarrier': [
        'mobilebarrier'
    ],
    'firehydrant': [
        'fire_hydrant'
    ],
    'chair': [
        'chair',
        'swivel_chair',
        'bench'
    ],
    'trash': [
        'trash'
    ],
    'trashcan': [
        'trashcan'
    ],
    'person': [
        'pedestrian',
        'bicyclist',
        'motorcyclist',
        'rider_other',
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
    'bicycle': [
        'bicycle'
    ],
    'motorcycle': [
        'motorcycle'
    ],
    'car': [
        'car',
        'ego_vehicle'
    ],
    'van': [
        'van',
        'caravan'
    ],
    'bus': [
        'bus'
    ],
    'truck': [
        'truck',
        'pickup'
    ],
    'trailer': [
        'trailer'
    ],
    'train': [
        'train'
    ],
    'plane': [
        'plane'
    ],
    'boat': [
        'boat',
        'ship'
    ],
}

class_to_eval = {
    'unlabeled': False,
    'ambiguous': False,
    'sky': True,
    'road': True,
    'sidewalk': True,
    'railtrack': True,
    'terrain': True,
    'tree': True,
    'vegetation': True,
    'building': True,
    'infrastructure': True,
    'fence': True,
    'billboard': True,
    'trafficlight': True,
    'trafficsign': True,
    'mobilebarrier': True,
    'firehydrant': True,
    'chair': True,
    'trash': True,
    'trashcan': True,
    'person': True,
    'animal': True,
    'bicycle': True,
    'motorcycle': True,
    'car': True,
    'van': True,
    'bus': True,
    'truck': True,
    'trailer': True,
    'train': True,
    'plane': True,
    'boat': True
}
