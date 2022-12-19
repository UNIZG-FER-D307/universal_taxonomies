class_to_index = {
    'animal--bird': 0,
    'animal--ground-animal': 1,
    'construction--barrier--curb': 2,
    'construction--barrier--fence': 3,
    'construction--barrier--guard-rail': 4,
    'construction--barrier--other-barrier': 5,
    'construction--barrier--wall': 6,
    'construction--flat--bike-lane': 7,
    'construction--flat--crosswalk-plain': 8,
    'construction--flat--curb-cut': 9,
    'construction--flat--parking': 10,
    'construction--flat--pedestrian-area': 11,
    'construction--flat--rail-track': 12,
    'construction--flat--road': 13,
    'construction--flat--service-lane': 14,
    'construction--flat--sidewalk': 15,
    'construction--structure--bridge': 16,
    'construction--structure--building': 17,
    'construction--structure--tunnel': 18,
    'human--person': 19,
    'human--rider--bicyclist': 20,
    'human--rider--motorcyclist': 21,
    'human--rider--other-rider': 22,
    'marking--crosswalk-zebra': 23,
    'marking--general': 24,
    'nature--mountain': 25,
    'nature--sand': 26,
    'nature--sky': 27,
    'nature--snow': 28,
    'nature--terrain': 29,
    'nature--vegetation': 30,
    'nature--water': 31,
    'object--banner': 32,
    'object--bench': 33,
    'object--bike-rack': 34,
    'object--billboard': 35,
    'object--catch-basin': 36,
    'object--cctv-camera': 37,
    'object--fire-hydrant': 38,
    'object--junction-box': 39,
    'object--mailbox': 40,
    'object--manhole': 41,
    'object--phone-booth': 42,
    'object--pothole': 43,
    'object--street-light': 44,
    'object--support--pole': 45,
    'object--support--traffic-sign-frame': 46,
    'object--support--utility-pole': 47,
    'object--traffic-light': 48,
    'object--traffic-sign--back': 49,
    'object--traffic-sign--front': 50,
    'object--trash-can': 51,
    'object--vehicle--bicycle': 52,
    'object--vehicle--boat': 53,
    'object--vehicle--bus': 54,
    'object--vehicle--car': 55,
    'object--vehicle--caravan': 56,
    'object--vehicle--motorcycle': 57,
    'object--vehicle--on-rails': 58,
    'object--vehicle--other-vehicle': 59,
    'object--vehicle--trailer': 60,
    'object--vehicle--truck': 61,
    'object--vehicle--wheeled-slow': 62,
    'void--car-mount': 63,
    'void--ego-vehicle': 64,
    'void--unlabeled': 65
}

class_to_eval = {
   'animal--bird': True,
   'animal--ground-animal': True,
   'construction--barrier--curb': True,
   'construction--barrier--fence': True,
   'construction--barrier--guard-rail': True,
   'construction--barrier--other-barrier': True,
   'construction--barrier--wall': True,
   'construction--flat--bike-lane': True,
   'construction--flat--crosswalk-plain': True,
   'construction--flat--curb-cut': True,
   'construction--flat--parking': True,
   'construction--flat--pedestrian-area': True,
   'construction--flat--rail-track': True,
   'construction--flat--road': True,
   'construction--flat--service-lane': True,
   'construction--flat--sidewalk': True,
   'construction--structure--bridge': True,
   'construction--structure--building': True,
   'construction--structure--tunnel': True,
   'human--person': True,
   'human--rider--bicyclist': True,
   'human--rider--motorcyclist': True,
   'human--rider--other-rider': True,
   'marking--crosswalk-zebra': True,
   'marking--general': True,
   'nature--mountain': True,
   'nature--sand': True,
   'nature--sky': True,
   'nature--snow': True,
   'nature--terrain': True,
   'nature--vegetation': True,
   'nature--water': True,
   'object--banner': True,
   'object--bench': True,
   'object--bike-rack': True,
   'object--billboard': True,
   'object--catch-basin': True,
   'object--cctv-camera': True,
   'object--fire-hydrant': True,
   'object--junction-box': True,
   'object--mailbox': True,
   'object--manhole': True,
   'object--phone-booth': True,
   'object--pothole': True,
   'object--street-light': True,
   'object--support--pole': True,
   'object--support--traffic-sign-frame': True,
   'object--support--utility-pole': True,
   'object--traffic-light': True,
   'object--traffic-sign--back': True,
   'object--traffic-sign--front': True,
   'object--trash-can': True,
   'object--vehicle--bicycle': True,
   'object--vehicle--boat': True,
   'object--vehicle--bus': True,
   'object--vehicle--car': True,
   'object--vehicle--caravan': True,
   'object--vehicle--motorcycle': True,
   'object--vehicle--on-rails': True,
   'object--vehicle--other-vehicle': True,
   'object--vehicle--trailer': True,
   'object--vehicle--truck': True,
   'object--vehicle--wheeled-slow': True,
   'void--car-mount': True,
   'void--ego-vehicle': True,
   'void--unlabeled': False
   }


mapping = {
    'animal--bird': [
        'bird'
    ],
    'animal--ground-animal': [
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
    'construction--barrier--curb': [
        'curb'
    ],
    'construction--barrier--fence': [
        'fence'
    ],
    'construction--barrier--guard-rail': [
        'railing'
    ],
    'construction--barrier--other-barrier': [
        'bannister'
    ],
    'construction--barrier--wall': [
        'wall_brick',
        'wall_other',
        'wall_stone',
        'wall_tile',
        'wall_wood'
    ],
    'construction--flat--bike-lane': [
        'bike_lane'
    ],
    'construction--flat--crosswalk-plain': [
        'crosswalk_plain'
    ],
    'construction--flat--curb-cut': [
        'curb_cut'
    ],
    'construction--flat--parking': [
        'parking'
    ],
    'construction--flat--pedestrian-area': [
        'pedestrian_area'
    ],
    'construction--flat--rail-track': [
        'rail_track'
    ],
    'construction--flat--road': [
        'road'
    ],
    'construction--flat--service-lane': [
        'service_lane'
    ],
    'construction--flat--sidewalk': [
        'pavement'
    ],
    'construction--structure--bridge': [
        'bridge'
    ],
    'construction--structure--building': [
        'building',
        'skyscraper',
        'house',
        'roof',
        'hovel',
        'tower'
    ],
    'construction--structure--tunnel': [
        'tunnel'
    ],
    'human--person': [
        'pedestrian',
        'tie'
    ],
    'human--rider--bicyclist': [
        'bicyclist'
    ],
    'human--rider--motorcyclist': [
        'motorcyclist'
    ],
    'human--rider--other-rider': [
        'rider_other'
    ],
    'marking--crosswalk-zebra': [
        'zebra'
    ],
    'marking--general': [
        'marking_other'
    ],
    'nature--mountain': [
        'hill',
        'mountain'
    ],
    'nature--sand': [
        'sand'
    ],
    'nature--sky': [
        'sky_other'
    ],
    'nature--snow': [
        'snow'
    ],
    'nature--terrain': [
        'ground',
        'grass',
        'land',
        'dirt',
        'field',
        'playing_field',
        'gravel',
        'rock',
    ],
    'nature--vegetation': [
        'tree',
        'flower',
        'palm',
        'potted_plant'
    ],
    'nature--water': [
        'sea',
        'river',
        'lake',
        'water_other',
        'waterfall',
    ],
    'object--banner': [
        'banner'
    ],
    'object--bench': [
        'bench'
    ],
    'object--bike-rack': [
        'bike_rack'
    ],
    'object--billboard': [
        'billboard'
    ],
    'object--catch-basin': [
        'catch_basin'
    ],
    'object--cctv-camera': [
        'cctv_camera'
    ],
    'object--fire-hydrant': [
        'fire_hydrant'
    ],
    'object--junction-box': [
        'junction_box'
    ],
    'object--mailbox': [
        'mailbox'
    ],
    'object--manhole': [
        'manhole'
    ],
    'object--phone-booth': [
        'phone_booth'
    ],
    'object--pothole': [
        'pothole'
    ],
    'object--street-light': [
        'street_light'
    ],
    'object--support--pole': [
        'pole'
    ],
    'object--support--traffic-sign-frame': [
        'traffic_sign_frame'
    ],
    'object--support--utility-pole': [
        'utility_pole'
    ],
    'object--traffic-light': [
        'traffic_light'
    ],
    'object--traffic-sign--back': [
        'traffic_sign_back'
    ],
    'object--traffic-sign--front': [
        'traffic_sign_front'
    ],
    'object--trash-can': [
        'trashcan'
    ],
    'object--vehicle--bicycle': [
        'bicycle'
    ],
    'object--vehicle--boat': [
        'boat'
    ],
    'object--vehicle--bus': [
        'bus'
    ],
    'object--vehicle--car': [
        'car',
        'van',
        'pickup'
    ],
    'object--vehicle--caravan': [
        'caravan'
    ],
    'object--vehicle--motorcycle': [
        'motorcycle'
    ],
    'object--vehicle--on-rails': [
        'train',
    ],
    'object--vehicle--other-vehicle': [
        'vehicle_other'
    ],
    'object--vehicle--trailer': [
        'trailer'
    ],
    'object--vehicle--truck': [
        'truck'
    ],
    'object--vehicle--wheeled-slow': [
        'rickshaw',
        'wheeled_slow'
    ],
    'void--car-mount': [
        'car_mount'
    ],
    'void--ego-vehicle': [
        'ego_vehicle'
    ],
    'void--unlabeled': [
        'ignore'
    ]
}

