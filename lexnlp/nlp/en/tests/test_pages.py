#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Imports

from lexnlp.nlp.en.segments.pages import get_pages
from lexnlp.tests import lexnlp_tests

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/1.7.0/LICENSE"
__version__ = "1.7.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


def test_page_examples():
    for (_i, text, _input_args, expected) in lexnlp_tests.iter_test_data_text_and_tuple():
        def remove_blankspace(r):
            return r.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t", "")

        # Get list of pages
        page_list = list(lexnlp_tests.benchmark_extraction_func(get_pages, text))
        assert len(page_list) == len(expected)
        clean_result = [remove_blankspace(p) for p in expected]
        for page in page_list:
            assert remove_blankspace(page) in clean_result
