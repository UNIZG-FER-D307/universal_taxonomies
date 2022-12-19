class_to_index = {
    "person": 0,
    "bicycle": 1,
    "car": 2,
    "motorcycle": 3,
    "airplane": 4,
    "bus": 5,
    "train": 6,
    "truck": 7,
    "boat": 8,
    "traffic light": 9,
    "fire hydrant": 10,
    "stop sign": 11,
    "parking meter": 12,
    "bench": 13,
    "bird": 14,
    "cat": 15,
    "dog": 16,
    "horse": 17,
    "sheep": 18,
    "cow": 19,
    "elephant": 20,
    "bear": 21,
    "zebra": 22,
    "giraffe": 23,
    "backpack": 24,
    "umbrella": 25,
    "handbag": 26,
    "tie": 27,
    "suitcase": 28,
    "frisbee": 29,
    "skis": 30,
    "snowboard": 31,
    "sports ball": 32,
    "kite": 33,
    "baseball bat": 34,
    "baseball glove": 35,
    "skateboard": 36,
    "surfboard": 37,
    "tennis racket": 38,
    "bottle": 39,
    "wine glass": 40,
    "cup": 41,
    "fork": 42,
    "knife": 43,
    "spoon": 44,
    "bowl": 45,
    "banana": 46,
    "apple": 47,
    "sandwich": 48,
    "orange": 49,
    "broccoli": 50,
    "carrot": 51,
    "hot dog": 52,
    "pizza": 53,
    "donut": 54,
    "cake": 55,
    "chair": 56,
    "couch": 57,
    "potted plant": 58,
    "bed": 59,
    "dining table": 60,
    "toilet": 61,
    "tv": 62,
    "laptop": 63,
    "mouse": 64,
    "remote": 65,
    "keyboard": 66,
    "cell phone": 67,
    "microwave": 68,
    "oven": 69,
    "toaster": 70,
    "sink": 71,
    "refrigerator": 72,
    "book": 73,
    "clock": 74,
    "vase": 75,
    "scissors": 76,
    "teddy bear": 77,
    "hair drier": 78,
    "toothbrush": 79,
    "banner": 80,
    "blanket": 81,
    "bridge": 82,
    "cardboard": 83,
    "counter": 84,
    "curtain": 85,
    "door-stuff": 86,
    "floor-wood": 87,
    "flower": 88,
    "fruit": 89,
    "gravel": 90,
    "house": 91,
    "light": 92,
    "mirror-stuff": 93,
    "net": 94,
    "pillow": 95,
    "platform": 96,
    "playingfield": 97,
    "railroad": 98,
    "river": 99,
    "road": 100,
    "roof": 101,
    "sand": 102,
    "sea": 103,
    "shelf": 104,
    "snow": 105,
    "stairs": 106,
    "tent": 107,
    "towel": 108,
    "wall-brick": 109,
    "wall-stone": 110,
    "wall-tile": 111,
    "wall-wood": 112,
    "water-other": 113,
    "window-blind": 114,
    "window-other": 115,
    "tree-merged": 116,
    "fence-merged": 117,
    "ceiling-merged": 118,
    "sky-other-merged": 119,
    "cabinet-merged": 120,
    "table-merged": 121,
    "floor-other-merged": 122,
    "pavement-merged": 123,
    "mountain-merged": 124,
    "grass-merged": 125,
    "dirt-merged": 126,
    "paper-merged": 127,
    "food-other-merged": 128,
    "building-other-merged": 129,
    "rock-merged": 130,
    "wall-other-merged": 131,
    "rug-merged": 132,
    "ignore": 133
}
mapping = {
  "person" : [
    'pedestrian',
    'bicyclist',
    'motorcyclist',
    'rider_other'
  ],
  "bird" : [
    'bird'
  ],
  "cat" : [
    'cat'
  ],
  "dog" : [
    'dog'
  ],
  "horse" : [
    'horse'
  ],
  "sheep" : [
    'sheep'
  ],
  "cow" : [
    'cow'
  ],
  "elephant" : [
    'elephant'
  ],
  "bear" : [
    'bear'
  ],
  "zebra" : [
    'zebra_animal'
  ],
  "giraffe" : [
    'giraffe'
  ],
  "car" : [
    'car'
  ],
  "truck" : [
    'truck',
    'van',
    'trailer',
    'pickup'
  ],
  "bus" : [
    'bus'
  ],
  "train" : [
    'train'
  ],
  "motorcycle" : [
    'motorcycle'
  ],
  "bicycle" : [
    'bicycle'
  ],
  "boat" : [
    'boat',
    'ship'
  ],
  "airplane" : [
    'plane'
  ],
  "sky-other-merged" : [
    'sky_other'
  ],
  "dirt-merged" : [
    'dirt',
    'ground'
  ],
  "playingfield" : [
    'playing_field'
  ],
  "mountain-merged" : [
    'hill',
    'mountain'
  ],
  "sand" : [
    'sand'
  ],
  "grass-merged" : [
    'grass',
    'field'
  ],
  "gravel" : [
    'gravel'
  ],
  "rock-merged" : [
    'rock',
  ],
  "tree-merged" : [
    'tree',
    'palm',
  ],
  "flower" : [
    'flower'
  ],
  "potted plant" : [
    'potted_plant'
  ],
  "sea" : [
    'sea'
  ],
  "river" : [
    'river'
  ],
  "water-other" : [
    'lake',
    'water_other',
    'waterfall',
  ],
  "snow" : [
    'snow'
  ],
  "house" : [
    'house'
  ],
  "roof" : [
    'roof'
  ],
  "door-stuff" : [
    'door'
  ],
  "window-other" : [
    'window'
  ],
  "curtain" : [
    'curtain'
  ],
  "window-blind" : [
    'window_blind'
  ],
  "building-other-merged" : [
    'skyscraper',
    'hovel',
    'tower',
    'building'
  ],
  "bridge" : [
    'bridge'
  ],
  "tent" : [
    'tent'
  ],
  "stairs" : [
    'stair'
  ],
  "ceiling-merged" : [
    'ceiling_other'
  ],
  "wall-brick" : [
    'wall_brick'
  ],
  "wall-other-merged" : [
    'wall_other',
  ],
  "wall-stone" : [
    'wall_stone'
  ],
  "wall-tile" : [
    'wall_tile'
  ],
  "wall-wood" : [
    'wall_wood'
  ],
  "fence-merged" : [
    'fence',
    'railing',
    'bannister'
  ],
  "railroad" : [
    'rail_track'
  ],
  "road" : [
    'road'
  ],
  "floor-other-merged" : [
    'floor_other',
  ],
  "floor-wood" : [
    'wood_floor'
  ],
  "pavement-merged" : [
    'floor_stone',
    'pavement'
  ],
  "light" : [
    'street_light',
    'light_other',
    'lamp',
    'chandelier',
    'sconce'
  ],
  "traffic light" : [
    'traffic_light'
  ],
  "food-other-merged" : [
    'food_other',
  ],
  "broccoli" : [
    'broccoli'
  ],
  "carrot" : [
    'carrot'
  ],
  "fruit" : [
    'fruit'
  ],
  "banana" : [
    'banana'
  ],
  "apple" : [
    'apple'
  ],
  "orange" : [
    'orange'
  ],
  "sandwich" : [
    'sandwich'
  ],
  "hot dog" : [
    'hot_dog'
  ],
  "pizza" : [
    'pizza'
  ],
  "donut" : [
    'donut'
  ],
  "cake" : [
    'cake'
  ],
  "cabinet-merged" : [
    'cabinet',
  ],
  "bed" : [
    'bed'
  ],
  "table-merged" : [
    'desk_stuff',
    'table'
  ],
  "dining table" : [
    'dining_table'
  ],
  "chair" : [
    'chair',
    'swivel_chair'
  ],
  "couch" : [
    'sofa'
  ],
  "shelf" : [
    'shelf'
  ],
  "mirror-stuff" : [
    'mirror'
  ],
  "toilet" : [
    'toilet'
  ],
  "counter" : [
    'countertop',
    'buffet',
    'counter'
  ],
  "sink" : [
    'sink'
  ],
  "platform" : [
    'base'
  ],
  "bench" : [
    'bench'
  ],
  "fire hydrant" : [
    'fire_hydrant'
  ],
  "stop sign" : [
    'traffic_sign_front'
  ],
  "parking meter" : [
    'parking_meter'
  ],
  "banner" : [
    'banner'
  ],
  "snowboard" : [
    'snowboard'
  ],
  "kite" : [
    'kite'
  ],
  "baseball bat" : [
    'baseball_bat'
  ],
  "baseball glove" : [
    'baseball_glove'
  ],
  "skateboard" : [
    'skateboard'
  ],
  "surfboard" : [
    'surfboard'
  ],
  "tennis racket" : [
    'tennis_racket'
  ],
  "frisbee" : [
    'frisbee'
  ],
  "skis" : [
    'skis'
  ],
  "teddy bear" : [
    'teddy_bear'
  ],
  "sports ball" : [
    'ball'
  ],
  "refrigerator" : [
    'refridgerator'
  ],
  "oven" : [
    'oven'
  ],
  "microwave" : [
    'microvawe'
  ],
  "toaster" : [
    'toaster'
  ],
  "tie" : [
    'tie'
  ],
  "bottle" : [
    'bottle'
  ],
  "wine glass" : [
    'drinking_glass'
  ],
  "cup" : [
    'cup'
  ],
  "fork" : [
    'fork'
  ],
  "knife" : [
    'knife'
  ],
  "spoon" : [
    'spoon'
  ],
  "bowl" : [
    'bowl'
  ],
  "vase" : [
    'vase'
  ],
  "handbag" : [
    'handbag'
  ],
  "backpack" : [
    'backpack'
  ],
  "suitcase" : [
    'suitcase'
  ],
  "mouse" : [
    'mouse'
  ],
  "keyboard" : [
    'keyboard'
  ],
  "laptop" : [
    'laptop'
  ],
  "tv" : [
    'tv'
  ],
  "cardboard" : [
    'cardboard'
  ],
  "rug-merged" : [
    'rug',
    'carpet_floor'
  ],
  "paper-merged" : [
    'paper',
  ],
  "pillow" : [
    'pillow',
    'cushion'
  ],
  "towel" : [
    'towel'
  ],
  "book" : [
    'book'
  ],
  "scissors" : [
    'scissors'
  ],
  "toothbrush" : [
    'toothbrush'
  ],
  "remote" : [
    'remote'
  ],
  "cell phone" : [
    'cell_phone'
  ],
  "hair drier" : [
    'hair_drier'
  ],
  "net" : [
    'net'
  ],
  "umbrella" : [
    'umbrella'
  ],
  "clock" : [
    'clock'
  ],
  "blanket" : [
    'blanket'
  ],
  "ignore": [
    "ignore"
  ]
}
class_to_eval = {k: k != 'ignore' for k, v in class_to_index.items()}
