#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Condition unit tests for English.

This module implements unit tests for the condition extraction functionality in English.

Todo:
    * Better testing for exact test in return sources
    * More pathological and difficult cases
"""

# Imports

from lexnlp.extract.en.conditions import get_conditions
from lexnlp.tests import lexnlp_tests

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/1.7.0/LICENSE"
__version__ = "1.7.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


def test_condition_fixed_example():
    lexnlp_tests.test_extraction_func_on_test_data(get_conditions,
                                                   actual_data_converter=lambda t: [elem[0] for elem in t],
                                                   test_only_expected_in=True)
