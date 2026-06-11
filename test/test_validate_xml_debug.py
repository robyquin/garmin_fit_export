#!python

"""
Gpx validation test.

:Author: Roberto Quintiliani
:Copyright: Copyright (c) Roberto Quintiliani
:License: GPLv3 - see LICENSE

"""

import pytest
from pathlib import Path
from lxml import etree


@pytest.mark.parametrize('xml_path', Path('.').rglob('*.fit_debug.xml'))
def test_validation_xml_debug(xml_path):
    print("Process: {}".format(xml_path))
    try:
        etree.parse(xml_path)
        assert True
    except etree.XMLSyntaxError:
        assert False, xml_path
