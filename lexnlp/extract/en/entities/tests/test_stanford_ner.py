#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Name unit tests for English.

This module implements unit tests for the name extraction functionality in English.

Todo:
    * Better testing for exact test in return sources
    * More pathological and difficult cases
"""

# Imports
import pytest

from lexnlp import is_stanford_enabled
from lexnlp.tests import lexnlp_tests

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/1.7.0/LICENSE"
__version__ = "1.7.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


@pytest.mark.skipif(not is_stanford_enabled(), reason="Stanford is disabled.")
def test_stanford_name_example_in():
    from lexnlp.extract.en.entities.stanford_ner import get_persons
    lexnlp_tests.test_extraction_func_on_test_data(get_persons,
                                                   expected_data_converter=lambda row: row[0],
                                                   test_only_expected_in=True)


@pytest.mark.skipif(not is_stanford_enabled(), reason="Stanford is disabled.")
def test_stanford_org_example_in():
    from lexnlp.extract.en.entities.stanford_ner import get_organizations
    lexnlp_tests.test_extraction_func_on_test_data(get_organizations,
                                                   expected_data_converter=lambda row: row[0],
                                                   test_only_expected_in=True)


@pytest.mark.skipif(not is_stanford_enabled(), reason="Stanford is disabled.")
def test_stanford_locations():
    """
    Test Stanford NER location extraction.
    :return:
    """
    from lexnlp.extract.en.entities.stanford_ner import get_locations
    lexnlp_tests.test_extraction_func_on_test_data(get_locations)
