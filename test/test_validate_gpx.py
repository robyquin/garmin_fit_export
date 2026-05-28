#!python

import pytest
from pathlib import Path
from lxml import etree

# Carica lo schema master
schema_doc = etree.parse("./test/master_validation.xsd")
schema = etree.XMLSchema(schema_doc)


@pytest.mark.parametrize('xml_path', Path('.').rglob('*.gpx'))
def test_validation_gpx(xml_path):
    print("Process: {}".format(xml_path))
    gpx_doc = etree.parse(xml_path)

    if schema.validate(gpx_doc):
        assert True
    else:
        print(schema.error_log)
        assert False
