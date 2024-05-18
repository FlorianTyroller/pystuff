import random

standard_board_config = {
    'playercount':4,
    'points_to_win':12,
    'thief':False,
    'resource_types': ['lumber', 'grain', 'ore', 'wool', 'brick'],
    'buildings': {
        'road': {
            'recipe': {
                'resources': {
                    'lumber': 1,
                    'brick': 1,
                },
                'buildings': {},
            },
            'placement': 'edge',
            'limit': 13,
            'points': 0
        },
        'settlement': {
            'recipe': {
                'resources': {
                    'wool': 1,
                    'grain': 1,
                    'brick': 1,
                    'lumber': 1
                },
                'buildings': {},
            },
            'placement': 'corner',
            'limit': 6,
            'points': 1
        },
        'city': {
            'recipe': {
                'resources': {
                    'grain': 2,
                    'ore': 3
                },
                'buildings': {
                    'settlement': 1  # Requires one settlement to upgrade to a city
                },
            },
            'placement': 'corner',
            'limit': 4,
            'points': 2
        },
        'development_card': {
            'recipe': {
                'resources': {
                    'grain': 1,
                    'ore': 1,
                    'wool': 1
                },
                'buildings': {},
            },
            'placement': None,
            'limit': 5,
            'points': 0
        }
    },
    'resources': 
                [
                'ore', 'lumber', 'grain',
                'wool','brick', 'wool',
                'grain', 'lumber', 'wool',
                ],

    'numbers': 
            [
            7,7,7,
            7,7,7,
            7,7,7,
            ],

    'layout': 
                [
                (-1,1),(0,1),(1,1), 
                (-1,0),(0,0),(1,0), 
                (-1,-1),(0,-1),(1,-1)
                ]
}

standard_board_config_big = {
    'playercount':4,
    'points_to_win':12,
    'thief':False,
    'resource_types': ['lumber', 'grain', 'ore', 'wool', 'brick'],
    'buildings': {
        'road': {
            'recipe': {
                'resources': {
                    'lumber': 1,
                    'brick': 1,
                },
                'buildings': {},
            },
            'placement': 'edge',
            'limit': 13,
            'points': 0
        },
        'settlement': {
            'recipe': {
                'resources': {
                    'wool': 1,
                    'grain': 1,
                    'brick': 1,
                    'lumber': 1
                },
                'buildings': {},
            },
            'placement': 'corner',
            'limit': 6,
            'points': 1
        },
        'city': {
            'recipe': {
                'resources': {
                    'grain': 2,
                    'ore': 3
                },
                'buildings': {
                    'settlement': 1  # Requires one settlement to upgrade to a city
                },
            },
            'placement': 'corner',
            'limit': 4,
            'points': 2
        },
        'development_card': {
            'recipe': {
                'resources': {
                    'grain': 1,
                    'ore': 1,
                    'wool': 1
                },
                'buildings': {},
            },
            'placement': None,
            'limit': 5,
            'points': 0
        }
    },
    "resources": [
        "desert",
        "grain",
        "brick",
        "lumber",
        "grain",
        "grain",
        "grain",
        "brick",
        "brick",
        "desert",
        "lumber",
        "desert",
        "desert",
        "brick",
        "lumber",
        "lumber",
        "desert",
        "wool",
        "lumber",
        "wool",
        "ore",
        "lumber",
        "grain",
        "ore",
        "ore",
        "brick",
        "brick",
        "ore",
        "wool",
        "desert",
        "lumber",
        "lumber",
        "grain",
        "wool",
        "wool",
        "wool",
        "lumber",
        "ore",
        "brick",
        "lumber",
        "lumber",
        "lumber",
        "brick",
        "desert",
        "brick",
        "desert",
        "wool",
        "grain",
        "brick",
        "desert",
        "desert",
        "grain",
        "brick",
        "ore",
        "brick",
        "grain",
        "grain",
        "desert",
        "brick",
        "lumber",
        "lumber",
        "grain",
        "wool",
        "lumber",
        "brick",
        "desert",
        "ore",
        "brick",
        "desert",
        "brick",
        "wool",
        "lumber",
        "wool",
        "ore",
        "desert",
        "grain",
        "ore",
        "wool",
        "lumber",
        "brick",
        "lumber",
        "lumber",
        "wool",
        "ore",
        "desert",
        "ore",
        "desert",
        "brick",
        "brick",
        "ore",
        "lumber",
        "lumber",
        "lumber",
        "wool",
        "brick",
        "lumber",
        "desert",
        "brick",
        "lumber",
        "wool",
        "brick",
        "lumber",
        "wool",
        "desert",
        "desert",
        "grain",
        "wool",
        "ore",
        "grain",
        "ore",
        "grain",
        "wool",
        "brick",
        "grain",
        "wool",
        "lumber",
        "wool",
        "wool",
        "desert",
        "lumber",
        "lumber",
        "brick",
        "lumber",
        "grain",
        "brick",
        "desert",
        "grain",
        "wool",
        "lumber",
        "desert",
        "grain",
        "wool",
        "ore",
        "lumber",
        "grain",
        "lumber",
        "ore",
        "desert",
        "brick",
        "desert",
        "desert",
        "brick",
        "brick",
        "desert",
        "ore",
        "brick",
        "wool",
        "wool",
        "lumber",
        "grain",
        "grain",
        "grain",
        "wool",
        "brick",
        "grain",
        "ore",
        "wool",
        "ore",
        "ore",
        "desert",
        "ore",
        "brick",
        "lumber",
        "ore",
        "ore",
        "brick",
        "lumber",
        "grain",
        "wool",
        "ore",
        "brick",
        "ore",
        "desert",
        "wool",
        "grain",
        "grain",
        "ore",
        "grain",
        "ore",
        "brick",
        "ore",
        "wool",
        "desert",
        "ore",
        "brick",
        "grain",
        "ore",
        "ore",
        "wool",
        "grain",
        "ore",
        "ore",
        "ore",
        "brick",
        "brick",
        "brick",
        "brick",
        "wool",
        "brick",
        "wool",
        "grain",
        "desert",
        "lumber",
        "brick",
        "desert",
        "desert",
        "desert",
        "grain",
        "grain",
        "ore",
        "wool",
        "lumber",
        "ore",
        "desert",
        "wool",
        "grain",
        "brick",
        "lumber",
        "ore",
        "lumber",
        "brick",
        "lumber",
        "wool",
        "lumber",
        "ore",
        "ore",
        "wool",
        "grain",
        "wool",
        "ore",
        "lumber",
        "wool",
        "desert",
        "lumber",
        "wool",
        "brick",
        "wool",
        "desert",
        "desert",
        "lumber",
        "wool",
        "ore",
        "wool",
        "brick",
        "brick",
        "desert",
        "grain",
        "ore",
        "lumber",
        "grain",
        "lumber",
        "lumber",
        "brick",
        "wool",
        "grain",
        "grain",
        "wool",
        "brick",
        "lumber",
        "wool",
        "wool",
        "desert",
        "lumber",
        "wool",
        "lumber",
        "lumber",
        "ore",
        "lumber",
        "lumber",
        "desert",
        "grain",
        "grain",
        "wool",
        "grain",
        "wool",
        "brick",
        "wool",
        "desert",
        "wool",
        "wool",
        "wool",
        "ore",
        "desert",
        "desert",
        "desert",
        "grain",
        "grain",
        "wool",
        "wool",
        "grain",
        "wool",
        "lumber",
        "grain",
        "desert",
        "wool",
        "brick",
        "grain",
        "grain",
        "wool",
        "ore",
        "ore",
        "wool",
        "desert",
        "brick",
        "grain",
        "desert",
        "desert",
        "brick",
        "brick",
        "lumber",
        "grain",
        "grain",
        "wool",
        "desert",
        "ore",
        "desert",
        "brick",
        "wool",
        "desert",
        "desert",
        "desert",
        "lumber",
        "wool",
        "lumber",
        "ore",
        "desert",
        "wool",
        "lumber",
        "brick",
        "ore",
        "ore",
        "wool",
        "brick",
        "desert",
        "wool",
        "lumber",
        "brick",
        "ore",
        "lumber",
        "brick",
        "desert",
        "grain",
        "brick",
        "brick",
        "brick",
        "ore",
        "grain",
        "ore",
        "ore",
        "desert",
        "grain",
        "lumber",
        "brick",
        "grain",
        "lumber",
        "wool",
        "brick",
        "wool",
        "ore",
        "desert",
        "desert",
        "ore",
        "desert",
        "grain",
        "desert",
        "ore",
        "wool",
        "grain",
        "wool",
        "lumber",
        "wool",
        "wool",
        "desert",
        "lumber",
        "lumber",
        "lumber",
        "ore",
        "lumber",
        "lumber",
        "lumber",
        "lumber",
        "wool",
        "lumber",
        "brick",
        "grain",
        "grain",
        "wool",
        "wool",
        "lumber",
        "brick",
        "brick",
        "ore",
        "wool",
        "lumber",
        "lumber",
        "lumber",
        "brick",
        "desert",
        "ore",
        "wool",
        "ore",
        "desert",
        "lumber",
        "brick",
        "lumber",
        "wool",
        "desert",
        "desert",
        "desert",
        "desert",
        "grain",
        "brick",
        "ore",
        "ore",
        "desert",
        "wool",
        "lumber",
        "lumber",
        "lumber",
        "grain",
        "desert",
        "desert",
        "ore",
        "desert",
        "lumber",
        "ore",
        "brick",
        "desert",
        "wool",
        "grain",
        "lumber",
        "desert",
        "lumber",
        "grain",
        "ore",
        "wool",
        "lumber",
        "ore",
        "lumber",
        "lumber",
        "grain",
        "brick",
        "desert",
        "desert",
        "grain",
        "brick",
        "ore",
        "brick",
        "desert",
        "ore",
        "desert",
        "desert",
        "lumber",
        "brick",
        "ore",
        "grain",
        "desert",
        "desert",
        "brick",
        "desert",
        "lumber",
        "desert",
        "wool",
        "lumber",
        "brick",
        "brick",
        "desert",
        "ore",
        "brick",
        "lumber",
        "ore",
        "grain",
        "grain",
        "ore",
        "desert",
        "desert",
        "grain",
        "ore",
        "desert",
        "lumber",
        "desert",
        "brick",
        "lumber",
        "desert",
        "desert",
        "lumber",
        "lumber",
        "wool",
        "brick",
        "desert",
        "desert",
        "brick",
        "grain",
        "grain",
        "lumber",
        "wool",
        "wool",
        "ore",
        "ore",
        "lumber",
        "ore",
        "lumber",
        "lumber",
        "lumber",
        "ore",
        "desert",
        "desert",
        "lumber",
        "wool",
        "desert",
        "lumber",
        "wool",
        "lumber",
        "wool",
        "grain",
        "wool",
        "brick",
        "brick",
        "desert",
        "grain",
        "wool",
        "wool",
        "lumber",
        "grain",
        "ore",
        "grain",
        "desert",
        "lumber",
        "wool",
        "grain",
        "wool",
        "wool",
        "grain",
        "brick",
        "lumber",
        "desert",
        "grain",
        "lumber",
        "brick",
        "lumber",
        "brick",
        "brick",
        "ore",
        "lumber",
        "ore",
        "desert",
        "brick",
        "brick",
        "lumber",
        "lumber",
        "wool",
        "wool",
        "desert",
        "desert",
        "ore",
        "lumber",
        "ore",
        "desert",
        "brick",
        "brick",
        "lumber",
        "grain",
        "ore",
        "lumber",
        "lumber",
        "grain",
        "ore",
        "grain",
        "desert",
        "ore",
        "desert",
        "grain",
        "wool",
        "grain",
        "grain",
        "desert",
        "desert",
        "lumber",
        "desert",
        "wool",
        "desert",
        "ore",
        "brick",
        "brick",
        "desert",
        "brick",
        "desert",
        "brick",
        "desert",
        "grain",
        "ore",
        "desert",
        "lumber",
        "ore",
        "lumber",
        "desert",
        "ore",
        "desert",
        "grain",
        "wool",
        "brick",
        "wool",
        "grain",
        "lumber",
        "lumber",
        "ore",
        "desert",
        "lumber",
        "desert",
        "lumber",
        "wool",
        "ore",
        "brick",
        "grain",
        "brick",
        "wool",
        "grain",
        "lumber",
        "grain",
        "lumber",
        "wool",
        "lumber",
        "grain",
        "wool",
        "grain",
        "brick",
        "desert",
        "grain",
        "brick",
        "wool",
        "desert",
        "ore",
        "brick",
        "brick",
        "ore",
        "desert",
        "ore",
        "grain",
        "grain",
        "grain",
        "ore",
        "wool",
        "grain",
        "desert",
        "ore",
        "grain",
        "brick",
        "wool",
        "desert",
        "desert",
        "lumber",
        "grain",
        "brick",
        "desert",
        "ore",
        "wool",
        "grain",
        "grain",
        "desert",
        "lumber",
        "wool",
        "brick",
        "wool",
        "brick",
        "grain",
        "ore",
        "desert",
        "wool",
        "lumber",
        "ore",
        "ore",
        "lumber",
        "grain",
        "ore",
        "desert",
        "lumber",
        "grain",
        "desert",
        "brick",
        "desert",
        "brick",
        "ore",
        "ore",
        "lumber",
        "wool",
        "wool",
        "grain",
        "grain",
        "ore",
        "desert",
        "desert",
        "wool",
        "lumber",
        "grain",
        "desert",
        "ore",
        "lumber",
        "desert",
        "desert",
        "brick",
        "grain",
        "lumber",
        "grain",
        "grain",
        "wool",
        "brick",
        "lumber",
        "lumber",
        "lumber",
        "ore",
        "wool",
        "ore",
        "grain",
        "lumber",
        "brick",
        "desert",
        "desert",
        "grain",
        "desert",
        "lumber",
        "desert",
        "wool",
        "grain",
        "brick",
        "wool",
        "brick",
        "grain",
        "ore",
        "ore",
        "grain",
        "desert",
        "ore",
        "lumber",
        "wool",
        "lumber",
        "wool",
        "grain",
        "lumber",
        "grain",
        "lumber",
        "grain",
        "wool",
        "ore",
        "brick",
        "desert",
        "ore",
        "lumber",
        "lumber",
        "brick",
        "wool",
        "brick",
        "brick",
        "lumber",
        "wool",
        "wool",
        "desert",
        "desert",
        "wool",
        "lumber",
        "desert",
        "lumber",
        "lumber",
        "ore",
        "ore",
        "ore",
        "lumber",
        "wool",
        "brick",
        "desert",
        "lumber",
        "ore",
        "wool",
        "grain",
        "lumber",
        "ore",
        "ore",
        "lumber",
        "grain",
        "wool",
        "ore",
        "lumber",
        "ore",
        "wool",
        "desert",
        "ore",
        "ore",
        "wool",
        "lumber",
        "grain",
        "lumber",
        "grain",
        "grain",
        "ore",
        "desert",
        "lumber",
        "brick",
        "desert",
        "wool",
        "ore",
        "desert",
        "ore",
        "brick",
        "wool",
        "ore",
        "brick",
        "ore",
        "desert",
        "ore",
        "ore",
        "desert",
        "lumber",
        "brick",
        "ore",
        "grain",
        "grain",
        "brick",
        "desert",
        "grain",
        "desert",
        "brick",
        "brick",
        "desert",
        "grain",
        "wool",
        "lumber",
        "wool",
        "grain",
        "grain",
        "desert",
        "ore",
        "desert",
        "lumber",
        "ore",
        "lumber",
        "brick",
        "wool",
        "desert",
        "grain",
        "lumber",
        "lumber",
        "desert",
        "grain",
        "wool",
        "desert",
        "wool",
        "ore",
        "desert",
        "brick",
        "ore",
        "lumber",
        "desert",
        "desert",
        "grain",
        "lumber",
        "wool",
        "wool",
        "grain",
        "desert",
        "grain",
        "wool",
        "grain",
        "grain",
        "lumber",
        "desert",
        "brick",
        "desert",
        "brick",
        "grain",
        "brick",
        "wool",
        "grain",
        "grain",
        "wool",
        "ore",
        "desert",
        "ore",
        "lumber",
        "lumber",
        "grain",
        "brick",
        "lumber",
        "wool",
        "brick",
        "wool",
        "wool",
        "brick",
        "lumber",
        "ore",
        "ore",
        "wool",
        "lumber",
        "wool",
        "ore",
        "lumber",
        "desert",
        "desert",
        "wool",
        "lumber",
        "ore",
        "brick",
        "desert",
        "ore",
        "ore",
        "brick",
        "grain",
        "desert",
        "ore",
        "wool",
        "brick",
        "brick",
        "desert",
        "desert",
        "desert",
        "grain",
        "lumber",
        "grain",
        "brick",
        "desert",
        "brick",
        "desert",
        "lumber",
        "wool",
        "grain",
        "brick",
        "grain",
        "lumber",
        "lumber",
        "lumber",
        "lumber",
        "desert",
        "wool",
        "lumber",
        "brick",
        "brick",
        "desert",
        "grain",
        "grain",
        "desert",
        "lumber",
        "ore",
        "desert",
        "desert",
        "brick",
        "grain",
        "desert",
        "lumber",
        "desert",
        "desert",
        "ore",
        "lumber",
        "lumber",
        "lumber",
        "wool",
        "desert",
        "grain",
        "lumber",
        "brick",
        "brick",
        "grain",
        "wool",
        "grain",
        "grain",
        "ore",
        "ore",
        "ore",
        "lumber",
        "grain",
        "ore",
        "ore",
        "wool",
        "wool",
        "brick",
        "desert",
        "brick",
        "wool",
        "wool",
        "ore",
        "ore",
        "brick",
        "wool",
        "desert",
        "ore",
        "desert",
        "lumber",
        "wool",
        "grain",
        "desert",
        "grain",
        "brick",
        "lumber",
        "ore",
        "wool",
        "desert",
        "brick",
        "desert",
        "wool",
        "lumber",
        "lumber",
        "desert",
        "grain",
        "grain",
        "brick",
        "desert",
        "wool",
        "wool",
        "grain",
        "ore",
        "desert",
        "grain",
        "grain",
        "grain",
        "brick",
        "desert",
        "desert",
        "ore",
        "brick",
        "wool",
        "grain",
        "brick",
        "desert",
        "desert",
        "brick",
        "lumber",
        "lumber",
        "wool",
        "brick",
        "ore",
        "brick",
        "desert",
        "desert",
        "desert",
        "desert",
        "lumber",
        "desert",
        "ore",
        "grain",
        "brick",
        "brick",
        "wool",
        "brick",
        "grain",
        "lumber",
        "lumber",
        "grain",
        "wool",
        "lumber",
        "wool",
        "desert",
        "brick",
        "grain",
        "wool",
        "brick",
        "wool",
        "wool",
        "lumber",
        "grain",
        "desert",
        "wool",
        "ore",
        "ore",
        "lumber",
        "lumber",
        "grain",
        "brick",
        "grain",
        "ore",
        "brick",
        "ore",
        "grain",
        "wool",
        "desert",
        "wool",
        "brick",
        "lumber",
        "brick",
        "wool",
        "lumber",
        "desert",
        "grain",
        "wool",
        "brick",
        "lumber",
        "ore",
        "brick",
        "grain",
        "desert",
        "ore",
        "ore",
        "wool",
        "lumber",
        "lumber",
        "grain",
        "brick",
        "wool",
        "lumber",
        "grain",
        "lumber",
        "ore",
        "grain",
        "wool",
        "lumber",
        "desert",
        "grain",
        "brick",
        "desert",
        "ore",
        "brick",
        "ore",
        "grain",
        "ore",
        "wool",
        "grain",
        "brick",
        "lumber",
        "lumber",
        "grain",
        "desert",
        "ore",
        "ore",
        "lumber",
        "lumber",
        "brick",
        "brick",
        "grain",
        "ore",
        "grain",
        "lumber",
        "lumber",
        "ore",
        "ore",
        "desert",
        "wool",
        "wool",
        "wool",
        "desert",
        "ore",
        "wool",
        "brick",
        "brick",
        "grain",
        "ore",
        "brick",
        "lumber",
        "wool",
        "brick",
        "lumber",
        "desert",
        "grain",
        "desert",
        "lumber",
        "lumber",
        "ore",
        "wool",
        "wool",
        "brick",
        "desert",
        "wool",
        "brick",
        "brick",
        "ore",
        "desert",
        "lumber",
        "grain",
        "brick",
        "lumber",
        "ore",
        "grain",
        "ore",
        "brick",
        "desert",
        "ore",
        "ore",
        "grain",
        "ore",
        "ore",
        "lumber",
        "grain",
        "ore",
        "desert",
        "desert",
        "desert",
        "lumber",
        "grain",
        "wool",
        "lumber",
        "ore",
        "ore",
        "grain",
        "brick",
        "grain",
        "desert",
        "brick",
        "wool",
        "grain",
        "brick",
        "desert",
        "lumber",
        "grain",
        "grain",
        "ore",
        "lumber",
        "desert",
        "wool",
        "desert",
        "grain",
        "wool",
        "grain",
        "ore",
        "wool",
        "ore",
        "brick",
        "brick",
        "grain",
        "desert",
        "brick",
        "lumber",
        "brick",
        "brick",
        "wool",
        "grain",
        "grain",
        "wool",
        "wool",
        "ore",
        "wool",
        "wool",
        "ore",
        "lumber",
        "desert",
        "lumber",
        "grain",
        "wool",
        "grain",
        "ore",
        "lumber",
        "ore",
        "grain",
        "wool",
        "grain",
        "ore",
        "wool",
        "brick",
        "brick",
        "ore",
        "desert",
        "ore",
        "desert",
        "brick",
        "lumber",
        "brick",
        "wool",
        "brick",
        "lumber",
        "lumber",
        "desert",
        "ore",
        "desert",
        "brick",
        "ore",
        "lumber",
        "lumber",
        "ore",
        "desert",
        "ore",
        "wool",
        "lumber",
        "lumber",
        "desert",
        "brick",
        "grain",
        "desert",
        "desert",
        "desert",
        "ore",
        "grain",
        "desert",
        "wool",
        "ore",
        "ore",
        "desert",
        "ore",
        "desert",
        "brick",
        "ore",
        "wool",
        "wool",
        "brick",
        "wool",
        "wool",
        "ore",
        "ore",
        "wool",
        "grain",
        "grain",
        "wool",
        "desert",
        "desert",
        "desert",
        "desert",
        "ore",
        "grain",
        "ore",
        "desert",
        "brick",
        "desert",
        "lumber",
        "ore",
        "brick",
        "lumber",
        "ore",
        "grain",
        "brick",
        "wool",
        "brick",
        "brick",
        "desert",
        "lumber",
        "brick",
        "brick",
        "grain",
        "lumber",
        "grain",
        "lumber",
        "brick",
        "lumber",
        "lumber",
        "wool",
        "brick",
        "lumber",
        "desert",
        "wool",
        "desert",
        "lumber",
        "wool",
        "grain",
        "desert",
        "ore",
        "brick",
        "brick",
        "lumber",
        "wool",
        "desert",
        "grain",
        "brick",
        "brick",
        "brick",
        "lumber",
        "brick",
        "ore",
        "brick",
        "wool",
        "wool",
        "desert",
        "ore",
        "grain",
        "brick",
        "wool",
        "grain",
        "desert",
        "desert",
        "grain",
        "desert",
        "brick",
        "brick",
        "ore",
        "lumber",
        "grain",
        "grain",
        "grain",
        "grain",
        "desert",
        "lumber",
        "ore",
        "desert",
        "wool",
        "desert",
        "desert",
        "grain",
        "grain",
        "ore",
        "lumber",
        "wool",
        "wool",
        "brick",
        "ore",
        "grain",
        "desert",
        "wool",
        "wool",
        "brick",
        "wool",
        "ore",
        "grain",
        "wool",
        "desert",
        "brick",
        "desert",
        "desert",
        "ore",
        "lumber",
        "wool",
        "brick",
        "wool",
        "wool",
        "brick",
        "wool",
        "brick",
        "lumber",
        "ore",
        "grain",
        "wool",
        "brick",
        "ore",
        "desert",
        "wool",
        "desert",
        "lumber",
        "lumber",
        "lumber",
        "desert",
        "desert",
        "brick",
        "ore",
        "grain",
        "desert",
        "wool",
        "brick",
        "ore",
        "brick",
        "wool",
        "wool",
        "brick",
        "brick",
        "wool",
        "wool",
        "wool",
        "desert",
        "lumber",
        "grain",
        "grain",
        "lumber",
        "wool",
        "grain",
        "brick",
        "wool",
        "grain",
        "wool",
        "brick",
        "ore",
        "ore",
        "desert",
        "desert",
        "brick",
        "grain",
        "grain",
        "lumber",
        "brick",
        "lumber",
        "ore",
        "brick",
        "grain",
        "lumber",
        "desert",
        "ore",
        "grain",
        "grain",
        "desert",
        "lumber",
        "desert",
        "lumber",
        "ore",
        "ore",
        "brick",
        "ore",
        "lumber",
        "brick",
        "wool",
        "desert",
        "lumber",
        "grain",
        "grain",
        "brick",
        "grain",
        "ore",
        "desert",
        "brick",
        "brick",
        "ore",
        "desert",
        "wool",
        "ore",
        "ore",
        "brick",
        "desert",
        "grain",
        "grain",
        "lumber",
        "brick",
        "lumber",
        "desert",
        "grain",
        "lumber",
        "desert",
        "grain",
        "ore",
        "grain",
        "lumber",
        "desert",
        "ore",
        "desert",
        "brick",
        "ore",
        "desert",
        "ore",
        "wool",
        "lumber",
        "wool",
        "grain",
        "grain",
        "desert",
        "brick",
        "ore",
        "lumber",
        "grain",
        "grain",
        "desert",
        "ore",
        "lumber",
        "grain",
        "grain",
        "brick",
        "grain",
        "brick",
        "brick",
        "lumber",
        "ore",
        "lumber",
        "grain",
        "ore",
        "lumber",
        "wool",
        "wool",
        "desert",
        "desert",
        "ore",
        "desert",
        "lumber",
        "wool",
        "ore",
        "wool",
        "brick",
        "desert",
        "wool",
        "desert",
        "grain",
        "ore",
        "grain",
        "lumber",
        "brick",
        "ore",
        "desert",
        "brick",
        "ore",
        "wool",
        "grain",
        "wool",
        "wool",
        "brick",
        "ore",
        "lumber",
        "desert",
        "brick",
        "desert",
        "desert",
        "lumber",
        "grain",
        "brick",
        "brick",
        "desert",
        "desert",
        "wool",
        "desert",
        "brick",
        "desert",
        "ore",
        "brick",
        "brick",
        "desert",
        "desert",
        "desert",
        "lumber",
        "lumber",
        "lumber",
        "wool",
        "brick",
        "grain",
        "ore",
        "wool",
        "wool",
        "desert",
        "grain",
        "wool",
        "lumber",
        "grain",
        "lumber",
        "wool",
        "desert",
        "desert",
        "grain",
        "grain",
        "lumber",
        "brick",
        "ore",
        "brick",
        "desert",
        "desert",
        "ore",
        "ore",
        "wool",
        "lumber",
        "ore",
        "wool",
        "wool",
        "brick",
        "wool",
        "lumber",
        "grain",
        "desert",
        "ore",
        "wool",
        "ore",
        "wool",
        "desert",
        "ore",
        "desert",
        "desert",
        "ore",
        "ore",
        "lumber",
        "grain",
        "wool",
        "ore",
        "ore",
        "ore",
        "grain",
        "lumber",
        "grain",
        "grain",
        "lumber",
        "grain",
        "brick",
        "grain",
        "grain",
        "wool",
        "grain",
        "brick",
        "brick",
        "lumber",
        "wool",
        "grain",
        "grain",
        "wool",
        "brick",
        "brick",
        "grain",
        "brick",
        "lumber",
        "wool",
        "grain",
        "ore",
        "grain",
        "brick",
        "grain",
        "desert",
        "ore",
        "brick",
        "desert",
        "ore",
        "grain",
        "desert",
        "brick",
        "desert",
        "grain",
        "grain",
        "lumber",
        "grain",
        "ore",
        "desert",
        "desert",
        "grain",
        "desert",
        "desert",
        "wool",
        "lumber",
        "lumber",
        "grain",
        "lumber",
        "ore",
        "desert",
        "brick",
        "grain",
        "wool",
        "grain",
        "wool",
        "brick",
        "grain",
        "brick",
        "brick",
        "grain",
        "lumber",
        "brick",
        "wool",
        "desert",
        "desert",
        "brick",
        "lumber",
        "wool",
        "brick",
        "desert",
        "grain",
        "grain",
        "brick",
        "lumber",
        "brick",
        "lumber",
        "grain",
        "grain",
        "desert",
        "grain",
        "grain",
        "grain",
        "ore",
        "lumber",
        "wool",
        "wool",
        "grain",
        "grain",
        "wool",
        "ore",
        "lumber",
        "grain",
        "lumber",
        "lumber",
        "desert",
        "lumber",
        "grain",
        "brick",
        "ore",
        "grain",
        "ore",
        "grain",
        "brick",
        "ore",
        "ore",
        "brick",
        "ore",
        "desert",
        "lumber",
        "desert",
        "lumber",
        "lumber",
        "desert",
        "desert",
        "grain",
        "grain",
        "brick",
        "ore",
        "ore",
        "wool",
        "wool",
        "brick",
        "ore",
        "wool",
        "ore",
        "desert",
        "ore",
        "brick",
        "desert",
        "wool",
        "ore",
        "grain",
        "grain",
        "grain",
        "desert",
        "grain",
        "desert",
        "brick",
        "wool",
        "ore",
        "grain",
        "ore",
        "brick",
        "wool",
        "brick",
        "grain",
        "ore",
        "brick",
        "grain",
        "desert",
        "brick",
        "ore",
        "brick",
        "brick",
        "grain",
        "lumber",
        "brick",
        "grain",
        "desert",
        "brick",
        "grain",
        "lumber",
        "ore",
        "wool",
        "lumber",
        "desert",
        "desert",
        "brick",
        "brick",
        "ore",
        "wool",
        "ore",
        "brick",
        "grain",
        "grain",
        "lumber",
        "lumber",
        "ore",
        "desert",
        "desert",
        "wool",
        "ore",
        "lumber",
        "brick",
        "brick",
        "desert",
        "wool",
        "desert",
        "desert",
        "desert",
        "lumber",
        "ore",
        "grain",
        "wool",
        "desert",
        "brick",
        "brick",
        "desert",
        "lumber",
        "lumber",
        "ore",
        "lumber",
        "lumber",
        "brick",
        "grain",
        "wool",
        "ore",
        "ore",
        "grain",
        "desert",
        "lumber",
        "grain",
        "lumber",
        "wool",
        "desert",
        "ore",
        "wool",
        "wool",
        "lumber",
        "grain",
        "brick",
        "ore",
        "grain",
        "wool",
        "brick",
        "desert",
        "brick",
        "wool",
        "lumber",
        "wool",
        "grain",
        "brick",
        "desert",
        "wool",
        "brick",
        "grain",
        "grain",
        "lumber",
        "grain",
        "desert",
        "lumber",
        "lumber",
        "desert",
        "desert",
        "brick",
        "lumber",
        "brick",
        "ore",
        "lumber",
        "ore",
        "grain",
        "ore",
        "brick",
        "grain",
        "wool",
        "ore",
        "lumber",
        "grain",
        "lumber",
        "grain",
        "desert",
        "ore",
        "lumber",
        "grain",
        "grain",
        "grain",
        "desert",
        "grain",
        "wool",
        "brick",
        "wool",
        "ore",
        "lumber",
        "brick",
        "ore",
        "brick",
        "desert",
        "lumber",
        "lumber",
        "lumber",
        "grain",
        "lumber",
        "wool",
        "grain",
        "lumber",
        "brick",
        "brick",
        "lumber",
        "grain",
        "wool",
        "desert",
        "brick",
        "desert",
        "ore",
        "brick",
        "wool",
        "desert",
        "desert",
        "grain",
        "brick",
        "ore",
        "wool",
        "wool",
        "wool",
        "grain",
        "grain",
        "brick",
        "ore",
        "ore",
        "ore",
        "ore",
        "ore",
        "ore",
        "ore",
        "lumber",
        "desert",
        "grain",
        "lumber",
        "brick",
        "grain",
        "grain",
        "wool",
        "grain",
        "ore",
        "ore",
        "lumber",
        "lumber",
        "wool",
        "ore",
        "wool",
        "grain",
        "ore",
        "wool",
        "lumber",
        "lumber",
        "lumber",
        "desert",
        "brick",
        "desert",
        "wool",
        "grain",
        "wool",
        "lumber",
        "lumber",
        "desert",
        "desert",
        "wool",
        "grain",
        "wool",
        "wool",
        "grain",
        "brick",
        "lumber",
        "ore",
        "desert",
        "lumber",
        "brick",
        "wool",
        "brick",
        "desert",
        "brick",
        "ore",
        "wool",
        "lumber",
        "brick",
        "wool",
        "desert",
        "ore",
        "brick",
        "wool",
        "ore",
        "ore",
        "lumber",
        "desert",
        "wool",
        "grain",
        "ore",
        "ore",
        "grain",
        "ore",
        "grain",
        "brick",
        "desert",
        "lumber",
        "lumber",
        "ore",
        "wool",
        "wool",
        "wool",
        "lumber",
        "grain",
        "wool",
        "wool",
        "ore",
        "ore",
        "lumber",
        "lumber",
        "brick",
        "brick",
        "brick",
        "desert",
        "desert",
        "desert",
        "lumber",
        "desert",
        "lumber",
        "desert",
        "lumber",
        "wool",
        "desert",
        "desert",
        "desert",
        "ore",
        "desert",
        "wool",
        "ore",
        "desert",
        "desert",
        "wool",
        "wool",
        "ore",
        "grain",
        "wool",
        "grain",
        "desert",
        "grain",
        "wool",
        "desert",
        "ore",
        "ore",
        "desert",
        "lumber",
        "ore",
        "lumber",
        "wool",
        "desert",
        "desert",
        "desert",
        "desert",
        "ore",
        "wool",
        "wool",
        "brick",
        "brick",
        "grain",
        "wool",
        "desert",
        "desert",
        "wool",
        "brick",
        "brick",
        "ore",
        "brick",
        "desert",
        "lumber",
        "lumber",
        "ore",
        "desert",
        "desert",
        "lumber",
        "brick",
        "grain",
        "brick",
        "brick",
        "lumber",
        "ore",
        "lumber",
        "ore",
        "lumber",
        "lumber",
        "grain",
        "ore",
        "desert",
        "brick",
        "ore",
        "ore",
        "desert",
        "brick",
        "wool",
        "wool",
        "ore",
        "ore",
        "ore",
        "brick",
        "brick",
        "desert",
        "wool",
        "ore",
        "ore",
        "lumber",
        "brick",
        "desert",
        "brick",
        "brick",
        "brick",
        "brick",
        "desert",
        "lumber",
        "brick",
        "brick",
        "wool",
        "lumber",
        "brick",
        "ore",
        "wool",
        "lumber",
        "grain",
        "lumber",
        "lumber",
        "grain",
        "grain",
        "lumber",
        "brick",
        "lumber",
        "wool",
        "grain",
        "lumber",
        "lumber",
        "brick",
        "desert",
        "brick",
        "ore",
        "wool",
        "grain",
        "lumber",
        "wool",
        "lumber",
        "wool",
        "ore",
        "desert",
        "wool",
        "desert",
        "lumber",
        "wool",
        "wool",
        "wool",
        "grain",
        "lumber",
        "lumber",
        "ore",
        "lumber",
        "grain",
        "brick",
        "ore",
        "grain",
        "grain",
        "lumber",
        "ore",
        "brick",
        "wool",
        "wool",
        "grain",
        "lumber",
        "lumber",
        "ore",
        "lumber",
        "grain",
        "lumber",
        "lumber",
        "wool",
        "lumber",
        "desert",
        "lumber",
        "brick",
        "lumber",
        "brick",
        "desert",
        "ore",
        "wool",
        "ore",
        "desert",
        "ore",
        "lumber",
        "ore",
        "ore",
        "brick",
        "lumber",
        "grain",
        "desert",
        "desert",
        "brick",
        "ore",
        "lumber",
        "wool",
        "grain",
        "lumber",
        "ore",
        "wool",
        "lumber",
        "lumber",
        "brick",
        "desert",
        "grain",
        "desert",
        "lumber",
        "lumber",
        "grain",
        "brick",
        "grain",
        "grain",
        "wool",
        "wool",
        "grain",
        "wool",
        "brick",
        "brick",
        "ore",
        "wool",
        "desert",
        "grain",
        "brick",
        "ore",
        "ore",
        "grain",
        "wool",
        "lumber",
        "grain",
        "grain",
        "desert",
        "desert",
        "ore",
        "ore",
        "grain",
        "desert",
        "brick",
        "desert",
        "wool",
        "brick",
        "desert",
        "grain",
        "brick",
        "ore",
        "lumber",
        "grain",
        "ore",
        "ore",
        "grain",
        "wool",
        "grain",
        "lumber",
        "grain",
        "desert",
        "grain",
        "wool",
        "lumber",
        "brick",
        "grain",
        "wool",
        "wool",
        "wool",
        "desert",
        "wool",
        "lumber",
        "desert",
        "wool",
        "brick",
        "brick",
        "grain",
        "lumber",
        "wool",
        "brick",
        "ore",
        "lumber",
        "desert",
        "brick",
        "lumber",
        "lumber",
        "lumber",
        "brick",
        "ore",
        "lumber",
        "lumber",
        "desert",
        "grain",
        "desert",
        "brick",
        "grain",
        "brick",
        "ore",
        "grain",
        "ore",
        "brick",
        "brick",
        "ore",
        "ore",
        "grain",
        "brick",
        "wool",
        "ore",
        "grain",
        "grain",
        "lumber",
        "grain",
        "desert",
        "desert",
        "ore",
        "lumber",
        "ore",
        "grain",
        "ore",
        "brick",
        "grain",
        "ore",
        "ore",
        "grain",
        "desert",
        "grain",
        "ore",
        "ore",
        "desert",
        "grain",
        "ore",
        "ore",
        "wool",
        "ore",
        "brick",
        "ore",
        "grain",
        "wool",
        "wool",
        "brick",
        "brick",
        "ore",
        "brick",
        "ore",
        "brick",
        "brick",
        "lumber",
        "desert",
        "ore",
        "ore",
        "wool",
        "wool",
        "brick",
        "grain",
        "desert",
        "wool",
        "ore",
        "grain",
        "brick",
        "brick",
        "ore",
        "ore",
        "lumber",
        "brick",
        "ore",
        "desert",
        "wool",
        "grain",
        "lumber",
        "wool",
        "ore",
        "wool",
        "ore",
        "ore",
        "desert",
        "brick",
        "desert",
        "ore",
        "grain",
        "wool",
        "wool",
        "desert",
        "lumber",
        "wool",
        "lumber",
        "grain",
        "grain",
        "lumber",
        "brick",
        "desert",
        "grain",
        "desert",
        "desert",
        "desert",
        "wool",
        "grain",
        "grain",
        "ore",
        "brick",
        "brick",
        "desert",
        "brick",
        "brick",
        "brick",
        "wool",
        "lumber",
        "grain",
        "grain",
        "grain",
        "lumber",
        "lumber",
        "lumber",
        "brick",
        "grain",
        "brick",
        "brick",
        "lumber",
        "desert",
        "desert",
        "desert",
        "desert",
        "lumber",
        "grain",
        "lumber",
        "wool",
        "ore",
        "brick",
        "brick",
        "desert",
        "lumber",
        "brick",
        "desert",
        "brick",
        "ore",
        "brick",
        "desert",
        "brick",
        "desert",
        "desert",
        "grain",
        "wool",
        "wool",
        "lumber",
        "brick",
        "grain",
        "desert",
        "wool",
        "ore",
        "grain",
        "grain",
        "grain",
        "brick",
        "lumber",
        "wool",
        "lumber",
        "grain",
        "wool",
        "wool",
        "brick",
        "lumber",
        "brick",
        "brick",
        "desert",
        "desert",
        "grain",
        "ore",
        "desert",
        "brick",
        "wool",
        "desert"
    ],
    "numbers": [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None
    ],
    "layout": [
        (
            0, -25
        ),
        (
            1, -25
        ),
        (
            2, -25
        ),
        (
            3, -25
        ),
        (
            4, -25
        ),
        (
            5, -25
        ),
        (
            6, -25
        ),
        (
            7, -25
        ),
        (
            8, -25
        ),
        (
            9, -25
        ),
        (
            10, -25
        ),
        (
            11, -25
        ),
        (
            12, -25
        ),
        (
            13, -25
        ),
        (
            14, -25
        ),
        (
            15, -25
        ),
        (
            16, -25
        ),
        (
            17, -25
        ),
        (
            18, -25
        ),
        (
            19, -25
        ),
        (
            20, -25
        ),
        (
            21, -25
        ),
        (
            22, -25
        ),
        (
            23, -25
        ),
        (
            24, -25
        ),
        (
            25, -25
        ),
        (
            26, -25
        ),
        (
            27, -25
        ),
        (
            28, -25
        ),
        (
            29, -25
        ),
        (
            30, -25
        ),
        (
            31, -25
        ),
        (
            32, -25
        ),
        (
            33, -25
        ),
        (
            34, -25
        ),
        (
            35, -25
        ),
        (
            36, -25
        ),
        (
            37, -25
        ),
        (
            38, -25
        ),
        (
            39, -25
        ),
        (
            40, -25
        ),
        (
            41, -25
        ),
        (
            42, -25
        ),
        (
            43, -25
        ),
        (
            44, -25
        ),
        (
            45, -25
        ),
        (
            46, -25
        ),
        (
            47, -25
        ),
        (
            48, -25
        ),
        (
            49, -25
        ),
        (
            0, -24
        ),
        (
            1, -24
        ),
        (
            2, -24
        ),
        (
            3, -24
        ),
        (
            4, -24
        ),
        (
            5, -24
        ),
        (
            6, -24
        ),
        (
            7, -24
        ),
        (
            8, -24
        ),
        (
            9, -24
        ),
        (
            10, -24
        ),
        (
            11, -24
        ),
        (
            12, -24
        ),
        (
            13, -24
        ),
        (
            14, -24
        ),
        (
            15, -24
        ),
        (
            16, -24
        ),
        (
            17, -24
        ),
        (
            18, -24
        ),
        (
            19, -24
        ),
        (
            20, -24
        ),
        (
            21, -24
        ),
        (
            22, -24
        ),
        (
            23, -24
        ),
        (
            24, -24
        ),
        (
            25, -24
        ),
        (
            26, -24
        ),
        (
            27, -24
        ),
        (
            28, -24
        ),
        (
            29, -24
        ),
        (
            30, -24
        ),
        (
            31, -24
        ),
        (
            32, -24
        ),
        (
            33, -24
        ),
        (
            34, -24
        ),
        (
            35, -24
        ),
        (
            36, -24
        ),
        (
            37, -24
        ),
        (
            38, -24
        ),
        (
            39, -24
        ),
        (
            40, -24
        ),
        (
            41, -24
        ),
        (
            42, -24
        ),
        (
            43, -24
        ),
        (
            44, -24
        ),
        (
            45, -24
        ),
        (
            46, -24
        ),
        (
            47, -24
        ),
        (
            48, -24
        ),
        (
            49, -24
        ),
        (-1, -23),
        (
            0, -23
        ),
        (
            1, -23
        ),
        (
            2, -23
        ),
        (
            3, -23
        ),
        (
            4, -23
        ),
        (
            5, -23
        ),
        (
            6, -23
        ),
        (
            7, -23
        ),
        (
            8, -23
        ),
        (
            9, -23
        ),
        (
            10, -23
        ),
        (
            11, -23
        ),
        (
            12, -23
        ), (
            13, -23
        ), (
            14, -23
        ), (
            15, -23
        ), (
            16, -23
        ), (
            17, -23
        ), (
            18, -23
        ), (
            19, -23
        ), (
            20, -23
        ), (
            21, -23
        ), (
            22, -23
        ), (
            23, -23
        ), (
            24, -23
        ), (
            25, -23
        ), (
            26, -23
        ), (
            27, -23
        ), (
            28, -23
        ), (
            29, -23
        ), (
            30, -23
        ), (
            31, -23
        ), (
            32, -23
        ), (
            33, -23
        ), (
            34, -23
        ), (
            35, -23
        ), (
            36, -23
        ), (
            37, -23
        ), (
            38, -23
        ), (
            39, -23
        ), (
            40, -23
        ), (
            41, -23
        ), (
            42, -23
        ), (
            43, -23
        ), (
            44, -23
        ), (
            45, -23
        ), (
            46, -23
        ), (
            47, -23
        ), (
            48, -23
        ), (-1, -22), (
            0, -22
        ), (
            1, -22
        ), (
            2, -22
        ), (
            3, -22
        ), (
            4, -22
        ), (
            5, -22
        ), (
            6, -22
        ), (
            7, -22
        ), (
            8, -22
        ), (
            9, -22
        ), (
            10, -22
        ), (
            11, -22
        ), (
            12, -22
        ), (
            13, -22
        ), (
            14, -22
        ), (
            15, -22
        ), (
            16, -22
        ), (
            17, -22
        ), (
            18, -22
        ), (
            19, -22
        ), (
            20, -22
        ), (
            21, -22
        ), (
            22, -22
        ), (
            23, -22
        ), (
            24, -22
        ), (
            25, -22
        ), (
            26, -22
        ), (
            27, -22
        ), (
            28, -22
        ), (
            29, -22
        ), (
            30, -22
        ), (
            31, -22
        ), (
            32, -22
        ), (
            33, -22
        ), (
            34, -22
        ), (
            35, -22
        ), (
            36, -22
        ), (
            37, -22
        ), (
            38, -22
        ), (
            39, -22
        ), (
            40, -22
        ), (
            41, -22
        ), (
            42, -22
        ), (
            43, -22
        ), (
            44, -22
        ), (
            45, -22
        ), (
            46, -22
        ), (
            47, -22
        ), (
            48, -22
        ), (-2, -21), (-1, -21), (
            0, -21
        ), (
            1, -21
        ), (
            2, -21
        ), (
            3, -21
        ), (
            4, -21
        ), (
            5, -21
        ), (
            6, -21
        ), (
            7, -21
        ), (
            8, -21
        ), (
            9, -21
        ), (
            10, -21
        ), (
            11, -21
        ), (
            12, -21
        ), (
            13, -21
        ), (
            14, -21
        ), (
            15, -21
        ), (
            16, -21
        ), (
            17, -21
        ), (
            18, -21
        ), (
            19, -21
        ), (
            20, -21
        ), (
            21, -21
        ), (
            22, -21
        ), (
            23, -21
        ), (
            24, -21
        ), (
            25, -21
        ), (
            26, -21
        ), (
            27, -21
        ), (
            28, -21
        ), (
            29, -21
        ), (
            30, -21
        ), (
            31, -21
        ), (
            32, -21
        ), (
            33, -21
        ), (
            34, -21
        ), (
            35, -21
        ), (
            36, -21
        ), (
            37, -21
        ), (
            38, -21
        ), (
            39, -21
        ), (
            40, -21
        ), (
            41, -21
        ), (
            42, -21
        ), (
            43, -21
        ), (
            44, -21
        ), (
            45, -21
        ), (
            46, -21
        ), (
            47, -21
        ), (-2, -20), (-1, -20), (
            0, -20
        ), (
            1, -20
        ), (
            2, -20
        ), (
            3, -20
        ), (
            4, -20
        ), (
            5, -20
        ), (
            6, -20
        ), (
            7, -20
        ), (
            8, -20
        ), (
            9, -20
        ), (
            10, -20
        ), (
            11, -20
        ), (
            12, -20
        ), (
            13, -20
        ), (
            14, -20
        ), (
            15, -20
        ), (
            16, -20
        ), (
            17, -20
        ), (
            18, -20
        ), (
            19, -20
        ), (
            20, -20
        ), (
            21, -20
        ), (
            22, -20
        ), (
            23, -20
        ), (
            24, -20
        ), (
            25, -20
        ), (
            26, -20
        ), (
            27, -20
        ), (
            28, -20
        ), (
            29, -20
        ), (
            30, -20
        ), (
            31, -20
        ), (
            32, -20
        ), (
            33, -20
        ), (
            34, -20
        ), (
            35, -20
        ), (
            36, -20
        ), (
            37, -20
        ), (
            38, -20
        ), (
            39, -20
        ), (
            40, -20
        ), (
            41, -20
        ), (
            42, -20
        ), (
            43, -20
        ), (
            44, -20
        ), (
            45, -20
        ), (
            46, -20
        ), (
            47, -20
        ), (-3, -19), (-2, -19), (-1, -19), (
            0, -19
        ), (
            1, -19
        ), (
            2, -19
        ), (
            3, -19
        ), (
            4, -19
        ), (
            5, -19
        ), (
            6, -19
        ), (
            7, -19
        ), (
            8, -19
        ), (
            9, -19
        ), (
            10, -19
        ), (
            11, -19
        ), (
            12, -19
        ), (
            13, -19
        ), (
            14, -19
        ), (
            15, -19
        ), (
            16, -19
        ), (
            17, -19
        ), (
            18, -19
        ), (
            19, -19
        ), (
            20, -19
        ), (
            21, -19
        ), (
            22, -19
        ), (
            23, -19
        ), (
            24, -19
        ), (
            25, -19
        ), (
            26, -19
        ), (
            27, -19
        ), (
            28, -19
        ), (
            29, -19
        ), (
            30, -19
        ), (
            31, -19
        ), (
            32, -19
        ), (
            33, -19
        ), (
            34, -19
        ), (
            35, -19
        ), (
            36, -19
        ), (
            37, -19
        ), (
            38, -19
        ), (
            39, -19
        ), (
            40, -19
        ), (
            41, -19
        ), (
            42, -19
        ), (
            43, -19
        ), (
            44, -19
        ), (
            45, -19
        ), (
            46, -19
        ), (-3, -18), (-2, -18), (-1, -18), (
            0, -18
        ), (
            1, -18
        ), (
            2, -18
        ), (
            3, -18
        ), (
            4, -18
        ), (
            5, -18
        ), (
            6, -18
        ), (
            7, -18
        ), (
            8, -18
        ), (
            9, -18
        ), (
            10, -18
        ), (
            11, -18
        ), (
            12, -18
        ), (
            13, -18
        ), (
            14, -18
        ), (
            15, -18
        ), (
            16, -18
        ), (
            17, -18
        ), (
            18, -18
        ), (
            19, -18
        ), (
            20, -18
        ), (
            21, -18
        ), (
            22, -18
        ), (
            23, -18
        ), (
            24, -18
        ), (
            25, -18
        ), (
            26, -18
        ), (
            27, -18
        ), (
            28, -18
        ), (
            29, -18
        ), (
            30, -18
        ), (
            31, -18
        ), (
            32, -18
        ), (
            33, -18
        ), (
            34, -18
        ), (
            35, -18
        ), (
            36, -18
        ), (
            37, -18
        ), (
            38, -18
        ), (
            39, -18
        ), (
            40, -18
        ), (
            41, -18
        ), (
            42, -18
        ), (
            43, -18
        ), (
            44, -18
        ), (
            45, -18
        ), (
            46, -18
        ), (-4, -17), (-3, -17), (-2, -17), (-1, -17), (
            0, -17
        ), (
            1, -17
        ), (
            2, -17
        ), (
            3, -17
        ), (
            4, -17
        ), (
            5, -17
        ), (
            6, -17
        ), (
            7, -17
        ), (
            8, -17
        ), (
            9, -17
        ), (
            10, -17
        ), (
            11, -17
        ), (
            12, -17
        ), (
            13, -17
        ), (
            14, -17
        ), (
            15, -17
        ), (
            16, -17
        ), (
            17, -17
        ), (
            18, -17
        ), (
            19, -17
        ), (
            20, -17
        ), (
            21, -17
        ), (
            22, -17
        ), (
            23, -17
        ), (
            24, -17
        ), (
            25, -17
        ), (
            26, -17
        ), (
            27, -17
        ), (
            28, -17
        ), (
            29, -17
        ), (
            30, -17
        ), (
            31, -17
        ), (
            32, -17
        ), (
            33, -17
        ), (
            34, -17
        ), (
            35, -17
        ), (
            36, -17
        ), (
            37, -17
        ), (
            38, -17
        ), (
            39, -17
        ), (
            40, -17
        ), (
            41, -17
        ), (
            42, -17
        ), (
            43, -17
        ), (
            44, -17
        ), (
            45, -17
        ), (-4, -16), (-3, -16), (-2, -16), (-1, -16), (
            0, -16
        ), (
            1, -16
        ), (
            2, -16
        ), (
            3, -16
        ), (
            4, -16
        ), (
            5, -16
        ), (
            6, -16
        ), (
            7, -16
        ), (
            8, -16
        ), (
            9, -16
        ), (
            10, -16
        ), (
            11, -16
        ), (
            12, -16
        ), (
            13, -16
        ), (
            14, -16
        ), (
            15, -16
        ), (
            16, -16
        ), (
            17, -16
        ), (
            18, -16
        ), (
            19, -16
        ), (
            20, -16
        ), (
            21, -16
        ), (
            22, -16
        ), (
            23, -16
        ), (
            24, -16
        ), (
            25, -16
        ), (
            26, -16
        ), (
            27, -16
        ), (
            28, -16
        ), (
            29, -16
        ), (
            30, -16
        ), (
            31, -16
        ), (
            32, -16
        ), (
            33, -16
        ), (
            34, -16
        ), (
            35, -16
        ), (
            36, -16
        ), (
            37, -16
        ), (
            38, -16
        ), (
            39, -16
        ), (
            40, -16
        ), (
            41, -16
        ), (
            42, -16
        ), (
            43, -16
        ), (
            44, -16
        ), (
            45, -16
        ), (-5, -15), (-4, -15), (-3, -15), (-2, -15), (-1, -15), (
            0, -15
        ), (
            1, -15
        ), (
            2, -15
        ), (
            3, -15
        ), (
            4, -15
        ), (
            5, -15
        ), (
            6, -15
        ), (
            7, -15
        ), (
            8, -15
        ), (
            9, -15
        ), (
            10, -15
        ), (
            11, -15
        ), (
            12, -15
        ), (
            13, -15
        ), (
            14, -15
        ), (
            15, -15
        ), (
            16, -15
        ), (
            17, -15
        ), (
            18, -15
        ), (
            19, -15
        ), (
            20, -15
        ), (
            21, -15
        ), (
            22, -15
        ), (
            23, -15
        ), (
            24, -15
        ), (
            25, -15
        ), (
            26, -15
        ), (
            27, -15
        ), (
            28, -15
        ), (
            29, -15
        ), (
            30, -15
        ), (
            31, -15
        ), (
            32, -15
        ), (
            33, -15
        ), (
            34, -15
        ), (
            35, -15
        ), (
            36, -15
        ), (
            37, -15
        ), (
            38, -15
        ), (
            39, -15
        ), (
            40, -15
        ), (
            41, -15
        ), (
            42, -15
        ), (
            43, -15
        ), (
            44, -15
        ), (-5, -14), (-4, -14), (-3, -14), (-2, -14), (-1, -14), (
            0, -14
        ), (
            1, -14
        ), (
            2, -14
        ), (
            3, -14
        ), (
            4, -14
        ), (
            5, -14
        ), (
            6, -14
        ), (
            7, -14
        ), (
            8, -14
        ), (
            9, -14
        ), (
            10, -14
        ), (
            11, -14
        ), (
            12, -14
        ), (
            13, -14
        ), (
            14, -14
        ), (
            15, -14
        ), (
            16, -14
        ), (
            17, -14
        ), (
            18, -14
        ), (
            19, -14
        ), (
            20, -14
        ), (
            21, -14
        ), (
            22, -14
        ), (
            23, -14
        ), (
            24, -14
        ), (
            25, -14
        ), (
            26, -14
        ), (
            27, -14
        ), (
            28, -14
        ), (
            29, -14
        ), (
            30, -14
        ), (
            31, -14
        ), (
            32, -14
        ), (
            33, -14
        ), (
            34, -14
        ), (
            35, -14
        ), (
            36, -14
        ), (
            37, -14
        ), (
            38, -14
        ), (
            39, -14
        ), (
            40, -14
        ), (
            41, -14
        ), (
            42, -14
        ), (
            43, -14
        ), (
            44, -14
        ), (-6, -13), (-5, -13), (-4, -13), (-3, -13), (-2, -13), (-1, -13), (
            0, -13
        ), (
            1, -13
        ), (
            2, -13
        ), (
            3, -13
        ), (
            4, -13
        ), (
            5, -13
        ), (
            6, -13
        ), (
            7, -13
        ), (
            8, -13
        ), (
            9, -13
        ), (
            10, -13
        ), (
            11, -13
        ), (
            12, -13
        ), (
            13, -13
        ), (
            14, -13
        ), (
            15, -13
        ), (
            16, -13
        ), (
            17, -13
        ), (
            18, -13
        ), (
            19, -13
        ), (
            20, -13
        ), (
            21, -13
        ), (
            22, -13
        ), (
            23, -13
        ), (
            24, -13
        ), (
            25, -13
        ), (
            26, -13
        ), (
            27, -13
        ), (
            28, -13
        ), (
            29, -13
        ), (
            30, -13
        ), (
            31, -13
        ), (
            32, -13
        ), (
            33, -13
        ), (
            34, -13
        ), (
            35, -13
        ), (
            36, -13
        ), (
            37, -13
        ), (
            38, -13
        ), (
            39, -13
        ), (
            40, -13
        ), (
            41, -13
        ), (
            42, -13
        ), (
            43, -13
        ), (-6, -12), (-5, -12), (-4, -12), (-3, -12), (-2, -12), (-1, -12), (
            0, -12
        ), (
            1, -12
        ), (
            2, -12
        ), (
            3, -12
        ), (
            4, -12
        ), (
            5, -12
        ), (
            6, -12
        ), (
            7, -12
        ), (
            8, -12
        ), (
            9, -12
        ), (
            10, -12
        ), (
            11, -12
        ), (
            12, -12
        ), (
            13, -12
        ), (
            14, -12
        ), (
            15, -12
        ), (
            16, -12
        ), (
            17, -12
        ), (
            18, -12
        ), (
            19, -12
        ), (
            20, -12
        ), (
            21, -12
        ), (
            22, -12
        ), (
            23, -12
        ), (
            24, -12
        ), (
            25, -12
        ), (
            26, -12
        ), (
            27, -12
        ), (
            28, -12
        ), (
            29, -12
        ), (
            30, -12
        ), (
            31, -12
        ), (
            32, -12
        ), (
            33, -12
        ), (
            34, -12
        ), (
            35, -12
        ), (
            36, -12
        ), (
            37, -12
        ), (
            38, -12
        ), (
            39, -12
        ), (
            40, -12
        ), (
            41, -12
        ), (
            42, -12
        ), (
            43, -12
        ), (-7, -11), (-6, -11), (-5, -11), (-4, -11), (-3, -11), (-2, -11), (-1, -11), (
            0, -11
        ), (
            1, -11
        ), (
            2, -11
        ), (
            3, -11
        ), (
            4, -11
        ), (
            5, -11
        ), (
            6, -11
        ), (
            7, -11
        ), (
            8, -11
        ), (
            9, -11
        ), (
            10, -11
        ), (
            11, -11
        ), (
            12, -11
        ), (
            13, -11
        ), (
            14, -11
        ), (
            15, -11
        ), (
            16, -11
        ), (
            17, -11
        ), (
            18, -11
        ), (
            19, -11
        ), (
            20, -11
        ), (
            21, -11
        ), (
            22, -11
        ), (
            23, -11
        ), (
            24, -11
        ), (
            25, -11
        ), (
            26, -11
        ), (
            27, -11
        ), (
            28, -11
        ), (
            29, -11
        ), (
            30, -11
        ), (
            31, -11
        ), (
            32, -11
        ), (
            33, -11
        ), (
            34, -11
        ), (
            35, -11
        ), (
            36, -11
        ), (
            37, -11
        ), (
            38, -11
        ), (
            39, -11
        ), (
            40, -11
        ), (
            41, -11
        ), (
            42, -11
        ), (-7, -10), (-6, -10), (-5, -10), (-4, -10), (-3, -10), (-2, -10), (-1, -10), (
            0, -10
        ), (
            1, -10
        ), (
            2, -10
        ), (
            3, -10
        ), (
            4, -10
        ), (
            5, -10
        ), (
            6, -10
        ), (
            7, -10
        ), (
            8, -10
        ), (
            9, -10
        ), (
            10, -10
        ), (
            11, -10
        ), (
            12, -10
        ), (
            13, -10
        ), (
            14, -10
        ), (
            15, -10
        ), (
            16, -10
        ), (
            17, -10
        ), (
            18, -10
        ), (
            19, -10
        ), (
            20, -10
        ), (
            21, -10
        ), (
            22, -10
        ), (
            23, -10
        ), (
            24, -10
        ), (
            25, -10
        ), (
            26, -10
        ), (
            27, -10
        ), (
            28, -10
        ), (
            29, -10
        ), (
            30, -10
        ), (
            31, -10
        ), (
            32, -10
        ), (
            33, -10
        ), (
            34, -10
        ), (
            35, -10
        ), (
            36, -10
        ), (
            37, -10
        ), (
            38, -10
        ), (
            39, -10
        ), (
            40, -10
        ), (
            41, -10
        ), (
            42, -10
        ), (-8, -9), (-7, -9), (-6, -9), (-5, -9), (-4, -9), (-3, -9), (-2, -9), (-1, -9), (
            0, -9
        ), (
            1, -9
        ), (
            2, -9
        ), (
            3, -9
        ), (
            4, -9
        ), (
            5, -9
        ), (
            6, -9
        ), (
            7, -9
        ), (
            8, -9
        ), (
            9, -9
        ), (
            10, -9
        ), (
            11, -9
        ), (
            12, -9
        ), (
            13, -9
        ), (
            14, -9
        ), (
            15, -9
        ), (
            16, -9
        ), (
            17, -9
        ), (
            18, -9
        ), (
            19, -9
        ), (
            20, -9
        ), (
            21, -9
        ), (
            22, -9
        ), (
            23, -9
        ), (
            24, -9
        ), (
            25, -9
        ), (
            26, -9
        ), (
            27, -9
        ), (
            28, -9
        ), (
            29, -9
        ), (
            30, -9
        ), (
            31, -9
        ), (
            32, -9
        ), (
            33, -9
        ), (
            34, -9
        ), (
            35, -9
        ), (
            36, -9
        ), (
            37, -9
        ), (
            38, -9
        ), (
            39, -9
        ), (
            40, -9
        ), (
            41, -9
        ), (-8, -8), (-7, -8), (-6, -8), (-5, -8), (-4, -8), (-3, -8), (-2, -8), (-1, -8), (
            0, -8
        ), (
            1, -8
        ), (
            2, -8
        ), (
            3, -8
        ), (
            4, -8
        ), (
            5, -8
        ), (
            6, -8
        ), (
            7, -8
        ), (
            8, -8
        ), (
            9, -8
        ), (
            10, -8
        ), (
            11, -8
        ), (
            12, -8
        ), (
            13, -8
        ), (
            14, -8
        ), (
            15, -8
        ), (
            16, -8
        ), (
            17, -8
        ), (
            18, -8
        ), (
            19, -8
        ), (
            20, -8
        ), (
            21, -8
        ), (
            22, -8
        ), (
            23, -8
        ), (
            24, -8
        ), (
            25, -8
        ), (
            26, -8
        ), (
            27, -8
        ), (
            28, -8
        ), (
            29, -8
        ), (
            30, -8
        ), (
            31, -8
        ), (
            32, -8
        ), (
            33, -8
        ), (
            34, -8
        ), (
            35, -8
        ), (
            36, -8
        ), (
            37, -8
        ), (
            38, -8
        ), (
            39, -8
        ), (
            40, -8
        ), (
            41, -8
        ), (-9, -7), (-8, -7), (-7, -7), (-6, -7), (-5, -7), (-4, -7), (-3, -7), (-2, -7), (-1, -7), (
            0, -7
        ), (
            1, -7
        ), (
            2, -7
        ), (
            3, -7
        ), (
            4, -7
        ), (
            5, -7
        ), (
            6, -7
        ), (
            7, -7
        ), (
            8, -7
        ), (
            9, -7
        ), (
            10, -7
        ), (
            11, -7
        ), (
            12, -7
        ), (
            13, -7
        ), (
            14, -7
        ), (
            15, -7
        ), (
            16, -7
        ), (
            17, -7
        ), (
            18, -7
        ), (
            19, -7
        ), (
            20, -7
        ), (
            21, -7
        ), (
            22, -7
        ), (
            23, -7
        ), (
            24, -7
        ), (
            25, -7
        ), (
            26, -7
        ), (
            27, -7
        ), (
            28, -7
        ), (
            29, -7
        ), (
            30, -7
        ), (
            31, -7
        ), (
            32, -7
        ), (
            33, -7
        ), (
            34, -7
        ), (
            35, -7
        ), (
            36, -7
        ), (
            37, -7
        ), (
            38, -7
        ), (
            39, -7
        ), (
            40, -7
        ), (-9, -6), (-8, -6), (-7, -6), (-6, -6), (-5, -6), (-4, -6), (-3, -6), (-2, -6), (-1, -6), (
            0, -6
        ), (
            1, -6
        ), (
            2, -6
        ), (
            3, -6
        ), (
            4, -6
        ), (
            5, -6
        ), (
            6, -6
        ), (
            7, -6
        ), (
            8, -6
        ), (
            9, -6
        ), (
            10, -6
        ), (
            11, -6
        ), (
            12, -6
        ), (
            13, -6
        ), (
            14, -6
        ), (
            15, -6
        ), (
            16, -6
        ), (
            17, -6
        ), (
            18, -6
        ), (
            19, -6
        ), (
            20, -6
        ), (
            21, -6
        ), (
            22, -6
        ), (
            23, -6
        ), (
            24, -6
        ), (
            25, -6
        ), (
            26, -6
        ), (
            27, -6
        ), (
            28, -6
        ), (
            29, -6
        ), (
            30, -6
        ), (
            31, -6
        ), (
            32, -6
        ), (
            33, -6
        ), (
            34, -6
        ), (
            35, -6
        ), (
            36, -6
        ), (
            37, -6
        ), (
            38, -6
        ), (
            39, -6
        ), (
            40, -6
        ), (-10, -5), (-9, -5), (-8, -5), (-7, -5), (-6, -5), (-5, -5), (-4, -5), (-3, -5), (-2, -5), (-1, -5), (
            0, -5
        ), (
            1, -5
        ), (
            2, -5
        ), (
            3, -5
        ), (
            4, -5
        ), (
            5, -5
        ), (
            6, -5
        ), (
            7, -5
        ), (
            8, -5
        ), (
            9, -5
        ), (
            10, -5
        ), (
            11, -5
        ), (
            12, -5
        ), (
            13, -5
        ), (
            14, -5
        ), (
            15, -5
        ), (
            16, -5
        ), (
            17, -5
        ), (
            18, -5
        ), (
            19, -5
        ), (
            20, -5
        ), (
            21, -5
        ), (
            22, -5
        ), (
            23, -5
        ), (
            24, -5
        ), (
            25, -5
        ), (
            26, -5
        ), (
            27, -5
        ), (
            28, -5
        ), (
            29, -5
        ), (
            30, -5
        ), (
            31, -5
        ), (
            32, -5
        ), (
            33, -5
        ), (
            34, -5
        ), (
            35, -5
        ), (
            36, -5
        ), (
            37, -5
        ), (
            38, -5
        ), (
            39, -5
        ), (-10, -4), (-9, -4), (-8, -4), (-7, -4), (-6, -4), (-5, -4), (-4, -4), (-3, -4), (-2, -4), (-1, -4), (
            0, -4
        ), (
            1, -4
        ), (
            2, -4
        ), (
            3, -4
        ), (
            4, -4
        ), (
            5, -4
        ), (
            6, -4
        ), (
            7, -4
        ), (
            8, -4
        ), (
            9, -4
        ), (
            10, -4
        ), (
            11, -4
        ), (
            12, -4
        ), (
            13, -4
        ), (
            14, -4
        ), (
            15, -4
        ), (
            16, -4
        ), (
            17, -4
        ), (
            18, -4
        ), (
            19, -4
        ), (
            20, -4
        ), (
            21, -4
        ), (
            22, -4
        ), (
            23, -4
        ), (
            24, -4
        ), (
            25, -4
        ), (
            26, -4
        ), (
            27, -4
        ), (
            28, -4
        ), (
            29, -4
        ), (
            30, -4
        ), (
            31, -4
        ), (
            32, -4
        ), (
            33, -4
        ), (
            34, -4
        ), (
            35, -4
        ), (
            36, -4
        ), (
            37, -4
        ), (
            38, -4
        ), (
            39, -4
        ), (-11, -3), (-10, -3), (-9, -3), (-8, -3), (-7, -3), (-6, -3), (-5, -3), (-4, -3), (-3, -3), (-2, -3), (-1, -3), (
            0, -3
        ), (
            1, -3
        ), (
            2, -3
        ), (
            3, -3
        ), (
            4, -3
        ), (
            5, -3
        ), (
            6, -3
        ), (
            7, -3
        ), (
            8, -3
        ), (
            9, -3
        ), (
            10, -3
        ), (
            11, -3
        ), (
            12, -3
        ), (
            13, -3
        ), (
            14, -3
        ), (
            15, -3
        ), (
            16, -3
        ), (
            17, -3
        ), (
            18, -3
        ), (
            19, -3
        ), (
            20, -3
        ), (
            21, -3
        ), (
            22, -3
        ), (
            23, -3
        ), (
            24, -3
        ), (
            25, -3
        ), (
            26, -3
        ), (
            27, -3
        ), (
            28, -3
        ), (
            29, -3
        ), (
            30, -3
        ), (
            31, -3
        ), (
            32, -3
        ), (
            33, -3
        ), (
            34, -3
        ), (
            35, -3
        ), (
            36, -3
        ), (
            37, -3
        ), (
            38, -3
        ), (-11, -2), (-10, -2), (-9, -2), (-8, -2), (-7, -2), (-6, -2), (-5, -2), (-4, -2), (-3, -2), (-2, -2), (-1, -2), (
            0, -2
        ), (
            1, -2
        ), (
            2, -2
        ), (
            3, -2
        ), (
            4, -2
        ), (
            5, -2
        ), (
            6, -2
        ), (
            7, -2
        ), (
            8, -2
        ), (
            9, -2
        ), (
            10, -2
        ), (
            11, -2
        ), (
            12, -2
        ), (
            13, -2
        ), (
            14, -2
        ), (
            15, -2
        ), (
            16, -2
        ), (
            17, -2
        ), (
            18, -2
        ), (
            19, -2
        ), (
            20, -2
        ), (
            21, -2
        ), (
            22, -2
        ), (
            23, -2
        ), (
            24, -2
        ), (
            25, -2
        ), (
            26, -2
        ), (
            27, -2
        ), (
            28, -2
        ), (
            29, -2
        ), (
            30, -2
        ), (
            31, -2
        ), (
            32, -2
        ), (
            33, -2
        ), (
            34, -2
        ), (
            35, -2
        ), (
            36, -2
        ), (
            37, -2
        ), (
            38, -2
        ), (-12, -1), (-11, -1), (-10, -1), (-9, -1), (-8, -1), (-7, -1), (-6, -1), (-5, -1), (-4, -1), (-3, -1), (-2, -1), (-1, -1), (
            0, -1
        ), (
            1, -1
        ), (
            2, -1
        ), (
            3, -1
        ), (
            4, -1
        ), (
            5, -1
        ), (
            6, -1
        ), (
            7, -1
        ), (
            8, -1
        ), (
            9, -1
        ), (
            10, -1
        ), (
            11, -1
        ), (
            12, -1
        ), (
            13, -1
        ), (
            14, -1
        ), (
            15, -1
        ), (
            16, -1
        ), (
            17, -1
        ), (
            18, -1
        ), (
            19, -1
        ), (
            20, -1
        ), (
            21, -1
        ), (
            22, -1
        ), (
            23, -1
        ), (
            24, -1
        ), (
            25, -1
        ), (
            26, -1
        ), (
            27, -1
        ), (
            28, -1
        ), (
            29, -1
        ), (
            30, -1
        ), (
            31, -1
        ), (
            32, -1
        ), (
            33, -1
        ), (
            34, -1
        ), (
            35, -1
        ), (
            36, -1
        ), (
            37, -1
        ), (-12,
            0
        ), (-11,
            0
        ), (-10,
            0
        ), (-9,
            0
        ), (-8,
            0
        ), (-7,
            0
        ), (-6,
            0
        ), (-5,
            0
        ), (-4,
            0
        ), (-3,
            0
        ), (-2,
            0
        ), (-1,
            0
        ), (
            0,
            0
        ), (
            1,
            0
        ), (
            2,
            0
        ), (
            3,
            0
        ), (
            4,
            0
        ), (
            5,
            0
        ), (
            6,
            0
        ), (
            7,
            0
        ), (
            8,
            0
        ), (
            9,
            0
        ), (
            10,
            0
        ), (
            11,
            0
        ), (
            12,
            0
        ), (
            13,
            0
        ), (
            14,
            0
        ), (
            15,
            0
        ), (
            16,
            0
        ), (
            17,
            0
        ), (
            18,
            0
        ), (
            19,
            0
        ), (
            20,
            0
        ), (
            21,
            0
        ), (
            22,
            0
        ), (
            23,
            0
        ), (
            24,
            0
        ), (
            25,
            0
        ), (
            26,
            0
        ), (
            27,
            0
        ), (
            28,
            0
        ), (
            29,
            0
        ), (
            30,
            0
        ), (
            31,
            0
        ), (
            32,
            0
        ), (
            33,
            0
        ), (
            34,
            0
        ), (
            35,
            0
        ), (
            36,
            0
        ), (
            37,
            0
        ), (-13,
            1
        ), (-12,
            1
        ), (-11,
            1
        ), (-10,
            1
        ), (-9,
            1
        ), (-8,
            1
        ), (-7,
            1
        ), (-6,
            1
        ), (-5,
            1
        ), (-4,
            1
        ), (-3,
            1
        ), (-2,
            1
        ), (-1,
            1
        ), (
            0,
            1
        ), (
            1,
            1
        ), (
            2,
            1
        ), (
            3,
            1
        ), (
            4,
            1
        ), (
            5,
            1
        ), (
            6,
            1
        ), (
            7,
            1
        ), (
            8,
            1
        ), (
            9,
            1
        ), (
            10,
            1
        ), (
            11,
            1
        ), (
            12,
            1
        ), (
            13,
            1
        ), (
            14,
            1
        ), (
            15,
            1
        ), (
            16,
            1
        ), (
            17,
            1
        ), (
            18,
            1
        ), (
            19,
            1
        ), (
            20,
            1
        ), (
            21,
            1
        ), (
            22,
            1
        ), (
            23,
            1
        ), (
            24,
            1
        ), (
            25,
            1
        ), (
            26,
            1
        ), (
            27,
            1
        ), (
            28,
            1
        ), (
            29,
            1
        ), (
            30,
            1
        ), (
            31,
            1
        ), (
            32,
            1
        ), (
            33,
            1
        ), (
            34,
            1
        ), (
            35,
            1
        ), (
            36,
            1
        ), (-13,
            2
        ), (-12,
            2
        ), (-11,
            2
        ), (-10,
            2
        ), (-9,
            2
        ), (-8,
            2
        ), (-7,
            2
        ), (-6,
            2
        ), (-5,
            2
        ), (-4,
            2
        ), (-3,
            2
        ), (-2,
            2
        ), (-1,
            2
        ), (
            0,
            2
        ), (
            1,
            2
        ), (
            2,
            2
        ), (
            3,
            2
        ), (
            4,
            2
        ), (
            5,
            2
        ), (
            6,
            2
        ), (
            7,
            2
        ), (
            8,
            2
        ), (
            9,
            2
        ), (
            10,
            2
        ), (
            11,
            2
        ), (
            12,
            2
        ), (
            13,
            2
        ), (
            14,
            2
        ), (
            15,
            2
        ), (
            16,
            2
        ), (
            17,
            2
        ), (
            18,
            2
        ), (
            19,
            2
        ), (
            20,
            2
        ), (
            21,
            2
        ), (
            22,
            2
        ), (
            23,
            2
        ), (
            24,
            2
        ), (
            25,
            2
        ), (
            26,
            2
        ), (
            27,
            2
        ), (
            28,
            2
        ), (
            29,
            2
        ), (
            30,
            2
        ), (
            31,
            2
        ), (
            32,
            2
        ), (
            33,
            2
        ), (
            34,
            2
        ), (
            35,
            2
        ), (
            36,
            2
        ), (-14,
            3
        ), (-13,
            3
        ), (-12,
            3
        ), (-11,
            3
        ), (-10,
            3
        ), (-9,
            3
        ), (-8,
            3
        ), (-7,
            3
        ), (-6,
            3
        ), (-5,
            3
        ), (-4,
            3
        ), (-3,
            3
        ), (-2,
            3
        ), (-1,
            3
        ), (
            0,
            3
        ), (
            1,
            3
        ), (
            2,
            3
        ), (
            3,
            3
        ), (
            4,
            3
        ), (
            5,
            3
        ), (
            6,
            3
        ), (
            7,
            3
        ), (
            8,
            3
        ), (
            9,
            3
        ), (
            10,
            3
        ), (
            11,
            3
        ), (
            12,
            3
        ), (
            13,
            3
        ), (
            14,
            3
        ), (
            15,
            3
        ), (
            16,
            3
        ), (
            17,
            3
        ), (
            18,
            3
        ), (
            19,
            3
        ), (
            20,
            3
        ), (
            21,
            3
        ), (
            22,
            3
        ), (
            23,
            3
        ), (
            24,
            3
        ), (
            25,
            3
        ), (
            26,
            3
        ), (
            27,
            3
        ), (
            28,
            3
        ), (
            29,
            3
        ), (
            30,
            3
        ), (
            31,
            3
        ), (
            32,
            3
        ), (
            33,
            3
        ), (
            34,
            3
        ), (
            35,
            3
        ), (-14,
            4
        ), (-13,
            4
        ), (-12,
            4
        ), (-11,
            4
        ), (-10,
            4
        ), (-9,
            4
        ), (-8,
            4
        ), (-7,
            4
        ), (-6,
            4
        ), (-5,
            4
        ), (-4,
            4
        ), (-3,
            4
        ), (-2,
            4
        ), (-1,
            4
        ), (
            0,
            4
        ), (
            1,
            4
        ), (
            2,
            4
        ), (
            3,
            4
        ), (
            4,
            4
        ), (
            5,
            4
        ), (
            6,
            4
        ), (
            7,
            4
        ), (
            8,
            4
        ), (
            9,
            4
        ), (
            10,
            4
        ), (
            11,
            4
        ), (
            12,
            4
        ), (
            13,
            4
        ), (
            14,
            4
        ), (
            15,
            4
        ), (
            16,
            4
        ), (
            17,
            4
        ), (
            18,
            4
        ), (
            19,
            4
        ), (
            20,
            4
        ), (
            21,
            4
        ), (
            22,
            4
        ), (
            23,
            4
        ), (
            24,
            4
        ), (
            25,
            4
        ), (
            26,
            4
        ), (
            27,
            4
        ), (
            28,
            4
        ), (
            29,
            4
        ), (
            30,
            4
        ), (
            31,
            4
        ), (
            32,
            4
        ), (
            33,
            4
        ), (
            34,
            4
        ), (
            35,
            4
        ), (-15,
            5
        ), (-14,
            5
        ), (-13,
            5
        ), (-12,
            5
        ), (-11,
            5
        ), (-10,
            5
        ), (-9,
            5
        ), (-8,
            5
        ), (-7,
            5
        ), (-6,
            5
        ), (-5,
            5
        ), (-4,
            5
        ), (-3,
            5
        ), (-2,
            5
        ), (-1,
            5
        ), (
            0,
            5
        ), (
            1,
            5
        ), (
            2,
            5
        ), (
            3,
            5
        ), (
            4,
            5
        ), (
            5,
            5
        ), (
            6,
            5
        ), (
            7,
            5
        ), (
            8,
            5
        ), (
            9,
            5
        ), (
            10,
            5
        ), (
            11,
            5
        ), (
            12,
            5
        ), (
            13,
            5
        ), (
            14,
            5
        ), (
            15,
            5
        ), (
            16,
            5
        ), (
            17,
            5
        ), (
            18,
            5
        ), (
            19,
            5
        ), (
            20,
            5
        ), (
            21,
            5
        ), (
            22,
            5
        ), (
            23,
            5
        ), (
            24,
            5
        ), (
            25,
            5
        ), (
            26,
            5
        ), (
            27,
            5
        ), (
            28,
            5
        ), (
            29,
            5
        ), (
            30,
            5
        ), (
            31,
            5
        ), (
            32,
            5
        ), (
            33,
            5
        ), (
            34,
            5
        ), (-15,
            6
        ), (-14,
            6
        ), (-13,
            6
        ), (-12,
            6
        ), (-11,
            6
        ), (-10,
            6
        ), (-9,
            6
        ), (-8,
            6
        ), (-7,
            6
        ), (-6,
            6
        ), (-5,
            6
        ), (-4,
            6
        ), (-3,
            6
        ), (-2,
            6
        ), (-1,
            6
        ), (
            0,
            6
        ), (
            1,
            6
        ), (
            2,
            6
        ), (
            3,
            6
        ), (
            4,
            6
        ), (
            5,
            6
        ), (
            6,
            6
        ), (
            7,
            6
        ), (
            8,
            6
        ), (
            9,
            6
        ), (
            10,
            6
        ), (
            11,
            6
        ), (
            12,
            6
        ), (
            13,
            6
        ), (
            14,
            6
        ), (
            15,
            6
        ), (
            16,
            6
        ), (
            17,
            6
        ), (
            18,
            6
        ), (
            19,
            6
        ), (
            20,
            6
        ), (
            21,
            6
        ), (
            22,
            6
        ), (
            23,
            6
        ), (
            24,
            6
        ), (
            25,
            6
        ), (
            26,
            6
        ), (
            27,
            6
        ), (
            28,
            6
        ), (
            29,
            6
        ), (
            30,
            6
        ), (
            31,
            6
        ), (
            32,
            6
        ), (
            33,
            6
        ), (
            34,
            6
        ), (-16,
            7
        ), (-15,
            7
        ), (-14,
            7
        ), (-13,
            7
        ), (-12,
            7
        ), (-11,
            7
        ), (-10,
            7
        ), (-9,
            7
        ), (-8,
            7
        ), (-7,
            7
        ), (-6,
            7
        ), (-5,
            7
        ), (-4,
            7
        ), (-3,
            7
        ), (-2,
            7
        ), (-1,
            7
        ), (
            0,
            7
        ), (
            1,
            7
        ), (
            2,
            7
        ), (
            3,
            7
        ), (
            4,
            7
        ), (
            5,
            7
        ), (
            6,
            7
        ), (
            7,
            7
        ), (
            8,
            7
        ), (
            9,
            7
        ), (
            10,
            7
        ), (
            11,
            7
        ), (
            12,
            7
        ), (
            13,
            7
        ), (
            14,
            7
        ), (
            15,
            7
        ), (
            16,
            7
        ), (
            17,
            7
        ), (
            18,
            7
        ), (
            19,
            7
        ), (
            20,
            7
        ), (
            21,
            7
        ), (
            22,
            7
        ), (
            23,
            7
        ), (
            24,
            7
        ), (
            25,
            7
        ), (
            26,
            7
        ), (
            27,
            7
        ), (
            28,
            7
        ), (
            29,
            7
        ), (
            30,
            7
        ), (
            31,
            7
        ), (
            32,
            7
        ), (
            33,
            7
        ), (-16,
            8
        ), (-15,
            8
        ), (-14,
            8
        ), (-13,
            8
        ), (-12,
            8
        ), (-11,
            8
        ), (-10,
            8
        ), (-9,
            8
        ), (-8,
            8
        ), (-7,
            8
        ), (-6,
            8
        ), (-5,
            8
        ), (-4,
            8
        ), (-3,
            8
        ), (-2,
            8
        ), (-1,
            8
        ), (
            0,
            8
        ), (
            1,
            8
        ), (
            2,
            8
        ), (
            3,
            8
        ), (
            4,
            8
        ), (
            5,
            8
        ), (
            6,
            8
        ), (
            7,
            8
        ), (
            8,
            8
        ), (
            9,
            8
        ), (
            10,
            8
        ), (
            11,
            8
        ), (
            12,
            8
        ), (
            13,
            8
        ), (
            14,
            8
        ), (
            15,
            8
        ), (
            16,
            8
        ), (
            17,
            8
        ), (
            18,
            8
        ), (
            19,
            8
        ), (
            20,
            8
        ), (
            21,
            8
        ), (
            22,
            8
        ), (
            23,
            8
        ), (
            24,
            8
        ), (
            25,
            8
        ), (
            26,
            8
        ), (
            27,
            8
        ), (
            28,
            8
        ), (
            29,
            8
        ), (
            30,
            8
        ), (
            31,
            8
        ), (
            32,
            8
        ), (
            33,
            8
        ), (-17,
            9
        ), (-16,
            9
        ), (-15,
            9
        ), (-14,
            9
        ), (-13,
            9
        ), (-12,
            9
        ), (-11,
            9
        ), (-10,
            9
        ), (-9,
            9
        ), (-8,
            9
        ), (-7,
            9
        ), (-6,
            9
        ), (-5,
            9
        ), (-4,
            9
        ), (-3,
            9
        ), (-2,
            9
        ), (-1,
            9
        ), (
            0,
            9
        ), (
            1,
            9
        ), (
            2,
            9
        ), (
            3,
            9
        ), (
            4,
            9
        ), (
            5,
            9
        ), (
            6,
            9
        ), (
            7,
            9
        ), (
            8,
            9
        ), (
            9,
            9
        ), (
            10,
            9
        ), (
            11,
            9
        ), (
            12,
            9
        ), (
            13,
            9
        ), (
            14,
            9
        ), (
            15,
            9
        ), (
            16,
            9
        ), (
            17,
            9
        ), (
            18,
            9
        ), (
            19,
            9
        ), (
            20,
            9
        ), (
            21,
            9
        ), (
            22,
            9
        ), (
            23,
            9
        ), (
            24,
            9
        ), (
            25,
            9
        ), (
            26,
            9
        ), (
            27,
            9
        ), (
            28,
            9
        ), (
            29,
            9
        ), (
            30,
            9
        ), (
            31,
            9
        ), (
            32,
            9
        ), (-17,
            10
        ), (-16,
            10
        ), (-15,
            10
        ), (-14,
            10
        ), (-13,
            10
        ), (-12,
            10
        ), (-11,
            10
        ), (-10,
            10
        ), (-9,
            10
        ), (-8,
            10
        ), (-7,
            10
        ), (-6,
            10
        ), (-5,
            10
        ), (-4,
            10
        ), (-3,
            10
        ), (-2,
            10
        ), (-1,
            10
        ), (
            0,
            10
        ), (
            1,
            10
        ), (
            2,
            10
        ), (
            3,
            10
        ), (
            4,
            10
        ), (
            5,
            10
        ), (
            6,
            10
        ), (
            7,
            10
        ), (
            8,
            10
        ), (
            9,
            10
        ), (
            10,
            10
        ), (
            11,
            10
        ), (
            12,
            10
        ), (
            13,
            10
        ), (
            14,
            10
        ), (
            15,
            10
        ), (
            16,
            10
        ), (
            17,
            10
        ), (
            18,
            10
        ), (
            19,
            10
        ), (
            20,
            10
        ), (
            21,
            10
        ), (
            22,
            10
        ), (
            23,
            10
        ), (
            24,
            10
        ), (
            25,
            10
        ), (
            26,
            10
        ), (
            27,
            10
        ), (
            28,
            10
        ), (
            29,
            10
        ), (
            30,
            10
        ), (
            31,
            10
        ), (
            32,
            10
        ), (-18,
            11
        ), (-17,
            11
        ), (-16,
            11
        ), (-15,
            11
        ), (-14,
            11
        ), (-13,
            11
        ), (-12,
            11
        ), (-11,
            11
        ), (-10,
            11
        ), (-9,
            11
        ), (-8,
            11
        ), (-7,
            11
        ), (-6,
            11
        ), (-5,
            11
        ), (-4,
            11
        ), (-3,
            11
        ), (-2,
            11
        ), (-1,
            11
        ), (
            0,
            11
        ), (
            1,
            11
        ), (
            2,
            11
        ), (
            3,
            11
        ), (
            4,
            11
        ), (
            5,
            11
        ), (
            6,
            11
        ), (
            7,
            11
        ), (
            8,
            11
        ), (
            9,
            11
        ), (
            10,
            11
        ), (
            11,
            11
        ), (
            12,
            11
        ), (
            13,
            11
        ), (
            14,
            11
        ), (
            15,
            11
        ), (
            16,
            11
        ), (
            17,
            11
        ), (
            18,
            11
        ), (
            19,
            11
        ), (
            20,
            11
        ), (
            21,
            11
        ), (
            22,
            11
        ), (
            23,
            11
        ), (
            24,
            11
        ), (
            25,
            11
        ), (
            26,
            11
        ), (
            27,
            11
        ), (
            28,
            11
        ), (
            29,
            11
        ), (
            30,
            11
        ), (
            31,
            11
        ), (-18,
            12
        ), (-17,
            12
        ), (-16,
            12
        ), (-15,
            12
        ), (-14,
            12
        ), (-13,
            12
        ), (-12,
            12
        ), (-11,
            12
        ), (-10,
            12
        ), (-9,
            12
        ), (-8,
            12
        ), (-7,
            12
        ), (-6,
            12
        ), (-5,
            12
        ), (-4,
            12
        ), (-3,
            12
        ), (-2,
            12
        ), (-1,
            12
        ), (
            0,
            12
        ), (
            1,
            12
        ), (
            2,
            12
        ), (
            3,
            12
        ), (
            4,
            12
        ), (
            5,
            12
        ), (
            6,
            12
        ), (
            7,
            12
        ), (
            8,
            12
        ), (
            9,
            12
        ), (
            10,
            12
        ), (
            11,
            12
        ), (
            12,
            12
        ), (
            13,
            12
        ), (
            14,
            12
        ), (
            15,
            12
        ), (
            16,
            12
        ), (
            17,
            12
        ), (
            18,
            12
        ), (
            19,
            12
        ), (
            20,
            12
        ), (
            21,
            12
        ), (
            22,
            12
        ), (
            23,
            12
        ), (
            24,
            12
        ), (
            25,
            12
        ), (
            26,
            12
        ), (
            27,
            12
        ), (
            28,
            12
        ), (
            29,
            12
        ), (
            30,
            12
        ), (
            31,
            12
        ), (-19,
            13
        ), (-18,
            13
        ), (-17,
            13
        ), (-16,
            13
        ), (-15,
            13
        ), (-14,
            13
        ), (-13,
            13
        ), (-12,
            13
        ), (-11,
            13
        ), (-10,
            13
        ), (-9,
            13
        ), (-8,
            13
        ), (-7,
            13
        ), (-6,
            13
        ), (-5,
            13
        ), (-4,
            13
        ), (-3,
            13
        ), (-2,
            13
        ), (-1,
            13
        ), (
            0,
            13
        ), (
            1,
            13
        ), (
            2,
            13
        ), (
            3,
            13
        ), (
            4,
            13
        ), (
            5,
            13
        ), (
            6,
            13
        ), (
            7,
            13
        ), (
            8,
            13
        ), (
            9,
            13
        ), (
            10,
            13
        ), (
            11,
            13
        ), (
            12,
            13
        ), (
            13,
            13
        ), (
            14,
            13
        ), (
            15,
            13
        ), (
            16,
            13
        ), (
            17,
            13
        ), (
            18,
            13
        ), (
            19,
            13
        ), (
            20,
            13
        ), (
            21,
            13
        ), (
            22,
            13
        ), (
            23,
            13
        ), (
            24,
            13
        ), (
            25,
            13
        ), (
            26,
            13
        ), (
            27,
            13
        ), (
            28,
            13
        ), (
            29,
            13
        ), (
            30,
            13
        ), (-19,
            14
        ), (-18,
            14
        ), (-17,
            14
        ), (-16,
            14
        ), (-15,
            14
        ), (-14,
            14
        ), (-13,
            14
        ), (-12,
            14
        ), (-11,
            14
        ), (-10,
            14
        ), (-9,
            14
        ), (-8,
            14
        ), (-7,
            14
        ), (-6,
            14
        ), (-5,
            14
        ), (-4,
            14
        ), (-3,
            14
        ), (-2,
            14
        ), (-1,
            14
        ), (
            0,
            14
        ), (
            1,
            14
        ), (
            2,
            14
        ), (
            3,
            14
        ), (
            4,
            14
        ), (
            5,
            14
        ), (
            6,
            14
        ), (
            7,
            14
        ), (
            8,
            14
        ), (
            9,
            14
        ), (
            10,
            14
        ), (
            11,
            14
        ), (
            12,
            14
        ), (
            13,
            14
        ), (
            14,
            14
        ), (
            15,
            14
        ), (
            16,
            14
        ), (
            17,
            14
        ), (
            18,
            14
        ), (
            19,
            14
        ), (
            20,
            14
        ), (
            21,
            14
        ), (
            22,
            14
        ), (
            23,
            14
        ), (
            24,
            14
        ), (
            25,
            14
        ), (
            26,
            14
        ), (
            27,
            14
        ), (
            28,
            14
        ), (
            29,
            14
        ), (
            30,
            14
        ), (-20,
            15
        ), (-19,
            15
        ), (-18,
            15
        ), (-17,
            15
        ), (-16,
            15
        ), (-15,
            15
        ), (-14,
            15
        ), (-13,
            15
        ), (-12,
            15
        ), (-11,
            15
        ), (-10,
            15
        ), (-9,
            15
        ), (-8,
            15
        ), (-7,
            15
        ), (-6,
            15
        ), (-5,
            15
        ), (-4,
            15
        ), (-3,
            15
        ), (-2,
            15
        ), (-1,
            15
        ), (
            0,
            15
        ), (
            1,
            15
        ), (
            2,
            15
        ), (
            3,
            15
        ), (
            4,
            15
        ), (
            5,
            15
        ), (
            6,
            15
        ), (
            7,
            15
        ), (
            8,
            15
        ), (
            9,
            15
        ), (
            10,
            15
        ), (
            11,
            15
        ), (
            12,
            15
        ), (
            13,
            15
        ), (
            14,
            15
        ), (
            15,
            15
        ), (
            16,
            15
        ), (
            17,
            15
        ), (
            18,
            15
        ), (
            19,
            15
        ), (
            20,
            15
        ), (
            21,
            15
        ), (
            22,
            15
        ), (
            23,
            15
        ), (
            24,
            15
        ), (
            25,
            15
        ), (
            26,
            15
        ), (
            27,
            15
        ), (
            28,
            15
        ), (
            29,
            15
        ), (-20,
            16
        ), (-19,
            16
        ), (-18,
            16
        ), (-17,
            16
        ), (-16,
            16
        ), (-15,
            16
        ), (-14,
            16
        ), (-13,
            16
        ), (-12,
            16
        ), (-11,
            16
        ), (-10,
            16
        ), (-9,
            16
        ), (-8,
            16
        ), (-7,
            16
        ), (-6,
            16
        ), (-5,
            16
        ), (-4,
            16
        ), (-3,
            16
        ), (-2,
            16
        ), (-1,
            16
        ), (
            0,
            16
        ), (
            1,
            16
        ), (
            2,
            16
        ), (
            3,
            16
        ), (
            4,
            16
        ), (
            5,
            16
        ), (
            6,
            16
        ), (
            7,
            16
        ), (
            8,
            16
        ), (
            9,
            16
        ), (
            10,
            16
        ), (
            11,
            16
        ), (
            12,
            16
        ), (
            13,
            16
        ), (
            14,
            16
        ), (
            15,
            16
        ), (
            16,
            16
        ), (
            17,
            16
        ), (
            18,
            16
        ), (
            19,
            16
        ), (
            20,
            16
        ), (
            21,
            16
        ), (
            22,
            16
        ), (
            23,
            16
        ), (
            24,
            16
        ), (
            25,
            16
        ), (
            26,
            16
        ), (
            27,
            16
        ), (
            28,
            16
        ), (
            29,
            16
        ), (-21,
            17
        ), (-20,
            17
        ), (-19,
            17
        ), (-18,
            17
        ), (-17,
            17
        ), (-16,
            17
        ), (-15,
            17
        ), (-14,
            17
        ), (-13,
            17
        ), (-12,
            17
        ), (-11,
            17
        ), (-10,
            17
        ), (-9,
            17
        ), (-8,
            17
        ), (-7,
            17
        ), (-6,
            17
        ), (-5,
            17
        ), (-4,
            17
        ), (-3,
            17
        ), (-2,
            17
        ), (-1,
            17
        ), (
            0,
            17
        ), (
            1,
            17
        ), (
            2,
            17
        ), (
            3,
            17
        ), (
            4,
            17
        ), (
            5,
            17
        ), (
            6,
            17
        ), (
            7,
            17
        ), (
            8,
            17
        ), (
            9,
            17
        ), (
            10,
            17
        ), (
            11,
            17
        ), (
            12,
            17
        ), (
            13,
            17
        ), (
            14,
            17
        ), (
            15,
            17
        ), (
            16,
            17
        ), (
            17,
            17
        ), (
            18,
            17
        ), (
            19,
            17
        ), (
            20,
            17
        ), (
            21,
            17
        ), (
            22,
            17
        ), (
            23,
            17
        ), (
            24,
            17
        ), (
            25,
            17
        ), (
            26,
            17
        ), (
            27,
            17
        ), (
            28,
            17
        ), (-21,
            18
        ), (-20,
            18
        ), (-19,
            18
        ), (-18,
            18
        ), (-17,
            18
        ), (-16,
            18
        ), (-15,
            18
        ), (-14,
            18
        ), (-13,
            18
        ), (-12,
            18
        ), (-11,
            18
        ), (-10,
            18
        ), (-9,
            18
        ), (-8,
            18
        ), (-7,
            18
        ), (-6,
            18
        ), (-5,
            18
        ), (-4,
            18
        ), (-3,
            18
        ), (-2,
            18
        ), (-1,
            18
        ), (
            0,
            18
        ), (
            1,
            18
        ), (
            2,
            18
        ), (
            3,
            18
        ), (
            4,
            18
        ), (
            5,
            18
        ), (
            6,
            18
        ), (
            7,
            18
        ), (
            8,
            18
        ), (
            9,
            18
        ), (
            10,
            18
        ), (
            11,
            18
        ), (
            12,
            18
        ), (
            13,
            18
        ), (
            14,
            18
        ), (
            15,
            18
        ), (
            16,
            18
        ), (
            17,
            18
        ), (
            18,
            18
        ), (
            19,
            18
        ), (
            20,
            18
        ), (
            21,
            18
        ), (
            22,
            18
        ), (
            23,
            18
        ), (
            24,
            18
        ), (
            25,
            18
        ), (
            26,
            18
        ), (
            27,
            18
        ), (
            28,
            18
        ), (-22,
            19
        ), (-21,
            19
        ), (-20,
            19
        ), (-19,
            19
        ), (-18,
            19
        ), (-17,
            19
        ), (-16,
            19
        ), (-15,
            19
        ), (-14,
            19
        ), (-13,
            19
        ), (-12,
            19
        ), (-11,
            19
        ), (-10,
            19
        ), (-9,
            19
        ), (-8,
            19
        ), (-7,
            19
        ), (-6,
            19
        ), (-5,
            19
        ), (-4,
            19
        ), (-3,
            19
        ), (-2,
            19
        ), (-1,
            19
        ), (
            0,
            19
        ), (
            1,
            19
        ), (
            2,
            19
        ), (
            3,
            19
        ), (
            4,
            19
        ), (
            5,
            19
        ), (
            6,
            19
        ), (
            7,
            19
        ), (
            8,
            19
        ), (
            9,
            19
        ), (
            10,
            19
        ), (
            11,
            19
        ), (
            12,
            19
        ), (
            13,
            19
        ), (
            14,
            19
        ), (
            15,
            19
        ), (
            16,
            19
        ), (
            17,
            19
        ), (
            18,
            19
        ), (
            19,
            19
        ), (
            20,
            19
        ), (
            21,
            19
        ), (
            22,
            19
        ), (
            23,
            19
        ), (
            24,
            19
        ), (
            25,
            19
        ), (
            26,
            19
        ), (
            27,
            19
        ), (-22,
            20
        ), (-21,
            20
        ), (-20,
            20
        ), (-19,
            20
        ), (-18,
            20
        ), (-17,
            20
        ), (-16,
            20
        ), (-15,
            20
        ), (-14,
            20
        ), (-13,
            20
        ), (-12,
            20
        ), (-11,
            20
        ), (-10,
            20
        ), (-9,
            20
        ), (-8,
            20
        ), (-7,
            20
        ), (-6,
            20
        ), (-5,
            20
        ), (-4,
            20
        ), (-3,
            20
        ), (-2,
            20
        ), (-1,
            20
        ), (
            0,
            20
        ), (
            1,
            20
        ), (
            2,
            20
        ), (
            3,
            20
        ), (
            4,
            20
        ), (
            5,
            20
        ), (
            6,
            20
        ), (
            7,
            20
        ), (
            8,
            20
        ), (
            9,
            20
        ), (
            10,
            20
        ), (
            11,
            20
        ), (
            12,
            20
        ), (
            13,
            20
        ), (
            14,
            20
        ), (
            15,
            20
        ), (
            16,
            20
        ), (
            17,
            20
        ), (
            18,
            20
        ), (
            19,
            20
        ), (
            20,
            20
        ), (
            21,
            20
        ), (
            22,
            20
        ), (
            23,
            20
        ), (
            24,
            20
        ), (
            25,
            20
        ), (
            26,
            20
        ), (
            27,
            20
        ), (-23,
            21
        ), (-22,
            21
        ), (-21,
            21
        ), (-20,
            21
        ), (-19,
            21
        ), (-18,
            21
        ), (-17,
            21
        ), (-16,
            21
        ), (-15,
            21
        ), (-14,
            21
        ), (-13,
            21
        ), (-12,
            21
        ), (-11,
            21
        ), (-10,
            21
        ), (-9,
            21
        ), (-8,
            21
        ), (-7,
            21
        ), (-6,
            21
        ), (-5,
            21
        ), (-4,
            21
        ), (-3,
            21
        ), (-2,
            21
        ), (-1,
            21
        ), (
            0,
            21
        ), (
            1,
            21
        ), (
            2,
            21
        ), (
            3,
            21
        ), (
            4,
            21
        ), (
            5,
            21
        ), (
            6,
            21
        ), (
            7,
            21
        ), (
            8,
            21
        ), (
            9,
            21
        ), (
            10,
            21
        ), (
            11,
            21
        ), (
            12,
            21
        ), (
            13,
            21
        ), (
            14,
            21
        ), (
            15,
            21
        ), (
            16,
            21
        ), (
            17,
            21
        ), (
            18,
            21
        ), (
            19,
            21
        ), (
            20,
            21
        ), (
            21,
            21
        ), (
            22,
            21
        ), (
            23,
            21
        ), (
            24,
            21
        ), (
            25,
            21
        ), (
            26,
            21
        ), (-23,
            22
        ), (-22,
            22
        ), (-21,
            22
        ), (-20,
            22
        ), (-19,
            22
        ), (-18,
            22
        ), (-17,
            22
        ), (-16,
            22
        ), (-15,
            22
        ), (-14,
            22
        ), (-13,
            22
        ), (-12,
            22
        ), (-11,
            22
        ), (-10,
            22
        ), (-9,
            22
        ), (-8,
            22
        ), (-7,
            22
        ), (-6,
            22
        ), (-5,
            22
        ), (-4,
            22
        ), (-3,
            22
        ), (-2,
            22
        ), (-1,
            22
        ), (
            0,
            22
        ), (
            1,
            22
        ), (
            2,
            22
        ), (
            3,
            22
        ), (
            4,
            22
        ), (
            5,
            22
        ), (
            6,
            22
        ), (
            7,
            22
        ), (
            8,
            22
        ), (
            9,
            22
        ), (
            10,
            22
        ), (
            11,
            22
        ), (
            12,
            22
        ), (
            13,
            22
        ), (
            14,
            22
        ), (
            15,
            22
        ), (
            16,
            22
        ), (
            17,
            22
        ), (
            18,
            22
        ), (
            19,
            22
        ), (
            20,
            22
        ), (
            21,
            22
        ), (
            22,
            22
        ), (
            23,
            22
        ), (
            24,
            22
        ), (
            25,
            22
        ), (
            26,
            22
        ), (-24,
            23
        ), (-23,
            23
        ), (-22,
            23
        ), (-21,
            23
        ), (-20,
            23
        ), (-19,
            23
        ), (-18,
            23
        ), (-17,
            23
        ), (-16,
            23
        ), (-15,
            23
        ), (-14,
            23
        ), (-13,
            23
        ), (-12,
            23
        ), (-11,
            23
        ), (-10,
            23
        ), (-9,
            23
        ), (-8,
            23
        ), (-7,
            23
        ), (-6,
            23
        ), (-5,
            23
        ), (-4,
            23
        ), (-3,
            23
        ), (-2,
            23
        ), (-1,
            23
        ), (
            0,
            23
        ), (
            1,
            23
        ), (
            2,
            23
        ), (
            3,
            23
        ), (
            4,
            23
        ), (
            5,
            23
        ), (
            6,
            23
        ), (
            7,
            23
        ), (
            8,
            23
        ), (
            9,
            23
        ), (
            10,
            23
        ), (
            11,
            23
        ), (
            12,
            23
        ), (
            13,
            23
        ), (
            14,
            23
        ), (
            15,
            23
        ), (
            16,
            23
        ), (
            17,
            23
        ), (
            18,
            23
        ), (
            19,
            23
        ), (
            20,
            23
        ), (
            21,
            23
        ), (
            22,
            23
        ), (
            23,
            23
        ), (
            24,
            23
        ), (
            25,
            23
        )
    ]
}




