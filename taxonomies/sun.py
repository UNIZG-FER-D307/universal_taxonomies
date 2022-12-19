class_to_index = {
    'unlabeled':  0,
    'wall':  1,
    'floor':  2,
    'cabinet':  3,
    'bed':  4,
    'chair':  5,
    'sofa':  6,
    'table':  7,
    'door':  8,
    'window':  9,
    'bookshelf': 10,
    'picture': 11,
    'counter': 12,
    'blinds': 13,
    'desk': 14,
    'shelves': 15,
    'curtain': 16,
    'dresser': 17,
    'pillow': 18,
    'mirror': 19,
    'floor mat': 20,
    'clothes': 21,
    'ceiling': 22,
    'books': 23,
    'refridgerator': 24,
    'television': 25,
    'paper': 26,
    'towel': 27,
    'shower curtain': 28,
    'box': 29,
    'whiteboard': 30,
    'person': 31,
    'night stand': 32,
    'toilet': 33,
    'sink': 34,
    'lamp': 35,
    'bathtub': 36,
    'bag': 37
}

class_to_eval = {
    'unlabeled': False,
    'wall': True,
    'floor': True,
    'cabinet': True,
    'bed': True,
    'chair': True,
    'sofa': True,
    'table': True,
    'door': True,
    'window': True,
    'bookshelf': True,
    'picture': True,
    'counter': True,
    'blinds': True,
    'desk': True,
    'shelves': True,
    'curtain': True,
    'dresser': True,
    'pillow': True,
    'mirror': True,
    'floor mat': True,
    'clothes': True,
    'ceiling': True,
    'books': True,
    'refridgerator': True,
    'television': True,
    'paper': True,
    'towel': True,
    'shower curtain': True,
    'box': True,
    'whiteboard': True,
    'person': True,
    'night stand': True,
    'toilet': True,
    'sink': True,
    'lamp': True,
    'bathtub': True,
    'bag': True,
}

mapping = {
  'unlabeled'   : [
   'ignore'
    ],
  'person'   : [
   'pedestrian',
   'bicyclist',
   'motorcyclist',
   'rider_other'
    ],
  'door'   : [
   'door'
    ],
  'window'   : [
   'window'
    ],
  'curtain'   : [
   'curtain'
    ],
  'blinds'   : [
   'window_blind'
    ],
  'ceiling'   : [
   'ceiling_other'
    ],
  'wall'   : [
   'wall_brick',
   'wall_other',
   'wall_stone',
   'wall_tile',
   'wall_wood'
    ],
  'floor'   : [
   'floor_other',
   'wood_floor',
    'carpet_floor'
    ],
  'lamp'   : [
   'light_other',
   'lamp',
   'chandelier',
   'sconce'
    ],
  'cabinet'   : [
   'cabinet'
    ],
  'bed'   : [
   'bed'
    ],
  'desk'   : [
   'desk_stuff'
    ],
  'table'   : [
   'table',
   'dining_table',
   'snooker_table',
   'coffee_table'
    ],
  'chair'   : [
   'chair',
   'swivel_chair'
    ],
  'sofa'   : [
   'sofa'
    ],
  'shelves'   : [
   'shelf'
    ],
  'dresser'   : [
   'dresser'
    ],
  'bookshelf'   : [
   'bookcase'
    ],
  'mirror'   : [
   'mirror'
    ],
  'night stand'   : [
   'nightstand'
    ],
  #'otherfurniture'   : [
  # 'armchair',
  # 'ottoman',
  # 'stool',
  # 'seat',
  # 'cupboard',
  # 'vitrine',
  # 'cradle',
  # 'wardrobe',
  # 'furniture_other'
  #  ],
  'toilet'   : [
   'toilet'
    ],
  'bathtub'   : [
   'bath'
    ],
  'shower curtain'   : [
   'shower_curtain'
    ],
  'counter'   : [
   'countertop',
   'buffet',
   'bar',
   'counter'
    ],
  'sink'   : [
   'sink'
    ],
  'picture'   : [
   'picture'
    ],
  'refridgerator'   : [
   'refridgerator'
    ],
  'clothes'   : [
   'clothes',
   'tie'
    ],
  'bag'   : [
   'handbag',
   'backpack',
   'suitcase'
    ],
  'television'   : [
   'computer_screen',
   'monitor',
   'crt_screen',
   'tv',
   'screen'
    ],
  'floor mat'   : [
   'rug',
    ],
  'paper'   : [
   'paper'
    ],
  'pillow'   : [
   'pillow',
   'cushion'
    ],
  'towel'   : [
   'towel'
    ],
  'books'   : [
   'book'
    ],
  'box'   : [
   'box'
  ],
  'whiteboard': [
    'whiteboard'
  ]
}


