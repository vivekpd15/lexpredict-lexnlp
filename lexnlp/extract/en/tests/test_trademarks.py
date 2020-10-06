#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Trademark unit tests for English.

This module implements unit tests for the Trademark extraction functionality in English.

Todo:
    * Better testing for exact test in return sources
    * More pathological and difficult cases
"""

# Project imports
from lexnlp.extract.en.trademarks import get_trademarks
from lexnlp.tests import lexnlp_tests

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/1.7.0/LICENSE"
__version__ = "1.7.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


def test_trademarks():
    lexnlp_tests.test_extraction_func_on_test_data(get_trademarks)
