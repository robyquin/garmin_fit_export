#!python
"""
Unofficial, but necessary, profile updates (garmin_fit_sdk)

:Author: Roberto Quintiliani
:Copyright: Copyright (c) Roberto Quintiliani
:License: GPLv3 - see LICENSE

"""

import garmin_fit_sdk as gfs

# File definition
gfs.Profile['types']['file']['8'] = 'location'  # Directory=Location
gfs.Profile['types']['file']['29'] = 'record'  # Directory=Record
gfs.Profile['types']['file']['33'] = 'mltsport'  # Directory=MltSport
gfs.Profile['types']['file']['37'] = 'club'  # Directory=Club
gfs.Profile['types']['file']['44'] = 'metric'  # Directory=Metric
gfs.Profile['types']['file']['65'] = 'calendar'  # Directory=Calendar

# enum definition
gfs.Profile['types']['record_units'] = {
    '0': 'ms',
    '1': 'cm',
    '2': 'm',
    '3': 'W',
}

gfs.Profile['types']['record_description'] = {
    '0': 'none',
    '3': 'ascent',
    '40000': 'longer',
}

# Message definition
gfs.Profile['mesg_num']['LOCATION'] = 29
gfs.Profile['types']['mesg_num']['29'] = 'location_mesgs'
gfs.Profile['messages'][29] = {
    'num': "29",
    'name': "location",
    'messages_key': "location_mesgs",
    'fields': {
        0: {
            'num': 2,
            'name': "label",
            'type': "string",
            'base_type': "string",
            'array': "true",
            'scale': [1],
            'offset': [0],
            'units': "",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        1: {
            'num': 1,
            'name': "position_lat",
            'type': "sint32",
            'base_type': "sint32",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "semicircles",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        2: {
            'num': 2,
            'name': "position_long",
            'type': "sint32",
            'base_type': "sint32",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "semicircles",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        3: {
            'num': 3,
            'name': "icon",
            'type': "uint16",
            'base_type': "uint16",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        254: {
            'num': 254,
            'name': "message_index",
            'type': "message_index",
            'base_type': "uint16",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
    }
}

gfs.Profile['mesg_num']['RECORD2'] = 114
gfs.Profile['types']['mesg_num']['114'] = 'record2_mesgs'
gfs.Profile['messages'][114] = {
    'num': "114",
    'name': "record",
    'messages_key': "record2_mesgs",
    'fields': {
        0: {
            'num': 0,
            'name': "record_units",
            'type': "record_units",
            'base_type': "enum",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        7: {
            'num': 7,
            'name': "record_description",
            'type': "record_description",
            'base_type': "enum",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        1: {
            'num': 1,
            'name': "sport",
            'type': "sport",
            'base_type': "enum",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        2: {
            'num': 2,
            'name': "target",
            'type': "uint32",
            'base_type': "uint32",
            'array': "false",
            'scale': [100],
            'offset': [0],
            'units': "m",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        3: {
            'num': 3,
            'name': "limit_inf",
            'type': "uint32",
            'base_type': "uint32",
            'array': "false",
            'scale': [100],
            'offset': [0],
            'units': "m",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        4: {
            'num': 4,
            'name': "limit_sup",
            'type': "uint32",
            'base_type': "uint32",
            'array': "false",
            'scale': [100],
            'offset': [0],
            'units': "m",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        5: {
            'num': 5,
            'name': "record",
            'type': "uint32",
            'base_type': "uint32",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "s",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        253: {
            'num': 253,
            'name': "timestamp",
            'type': "date_time",
            'base_type': "uint32",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "s",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
        254: {
            'num': 254,
            'name': "message_index",
            'type': "message_index",
            'base_type': "uint16",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
    }
}

gfs.Profile['mesg_num']['CLUB'] = 173
gfs.Profile['types']['mesg_num']['173'] = 'club_mesgs'
gfs.Profile['messages'][173] = {
    'num': "173",
    'name': "club",
    'messages_key': "club_mesgs",
    'fields': {
        253: {
            'num': 253,
            'name': "timestamp",
            'type': "date_time",
            'base_type': "uint32",
            'array': "false",
            'scale': [1],
            'offset': [0],
            'units': "s",
            'bits': [],
            'components': [],
            'is_accumulated': False,
            'has_components': False,
            'sub_fields': []
        },
    }
}

# Fields integration
gfs.Profile['messages'][20]['fields'][140] = {
    'num': 140,
    'name': "pendence_speed",
    'type': "uint32",
    'base_type': "uint32",
    'array': "false",
    'scale': [1000],
    'offset': [0],
    'units': "m/s",
    'bits': [],
    'components': [],
    'is_accumulated': False,
    'has_components': False,
    'sub_fields': []
}

gfs.Profile['messages'][313]['fields'][253] = {
    'num': 253,
    'name': "timestamp",
    'type': "date_time",
    'base_type': "uint32",
    'array': "false",
    'scale': [1],
    'offset': [0],
    'units': "s",
    'bits': [],
    'components': [],
    'is_accumulated': False,
    'has_components': False,
    'sub_fields': []
}

gfs.Profile['messages'][27]['fields'][18] = {
    'num': 18,
    'name': "target_index",
    'type': "target_index",
    'base_type': "uint16",
    'array': "false",
    'scale': [1],
    'offset': [0],
    'units': "",
    'bits': [],
    'components': [],
    'is_accumulated': False,
    'has_components': False,
    'sub_fields': []
}
