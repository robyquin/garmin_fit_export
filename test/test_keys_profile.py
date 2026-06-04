#!python

"""
Profile validation test.

:Author: Roberto Quintiliani
:Copyright: Copyright (c) Roberto Quintiliani
:License: to be defined

"""

import pytest
import garmin_fit_sdk as gfs


def test_version():
    assert gfs.__version__ == '21.205.0'


@pytest.mark.parametrize('key', ('8', '29', '33', '37', '44', '65'))
def test_file_definition(key):
    print("Process: {}".format(key))
    list_def_file = gfs.Profile['types']['file']
    if (key in list_def_file.keys()):
        assert False, "'{}' already exists!".format(key)
    else:
        assert True


@pytest.mark.parametrize('key', ('record_units', 'record_description'))
def test_enum_definition(key):
    print("Process: {}".format(key))
    list_def_enum = gfs.Profile['types']
    if (key in list_def_enum.keys()):
        assert False, "'{}' already exists!".format(key)
    else:
        assert True


@pytest.mark.parametrize('key', (['LOCATION', '29', 29], ['RECORD2', '114', 114], ['CLUB', '173', 173]))
def test_mesg_definition(key):
    print("Process: {}".format(key))
    list_def = [
        gfs.Profile['mesg_num'],
        gfs.Profile['types']['mesg_num'],
        gfs.Profile['messages']
    ]
    for k in range(0, 3):
        if (key[k] in list_def[k].keys()):
            assert False, "'{}' already exists!".format(key[k])
        else:
            assert True


@pytest.mark.parametrize('key', ([20, 140], [313, 253], [27, 18]))
def test_fields_integration(key):
    print("Process: {}".format(key))
    list_def = gfs.Profile['messages'][key[0]]['fields']
    if (key[1] in list_def.keys()):
        assert False, "Profile['messages']['{}']['fields']['{}'] already exists!".format(key[0], key[1])
    else:
        assert True
