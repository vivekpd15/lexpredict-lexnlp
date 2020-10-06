from unittest import TestCase

from lexnlp.extract.common.annotations.ratio_annotation import RatioAnnotation
from lexnlp.extract.en.ratios import get_ratios, get_ratio_annotations
from lexnlp.tests.typed_annotations_tests import TypedAnnotationsTester

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/1.7.0/LICENSE"
__version__ = "1.7.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class TestRatiosPlain(TestCase):

    def test_ratios(self):
        text = "Ratio of not greater than 3.0:1.5.."
        ds = list(get_ratios(text))
        self.assertEqual(1, len(ds))

        ants = list(get_ratio_annotations(text))
        self.assertEqual(1, len(ants))
        self.assertEqual('en', ants[0].locale)
        self.assertEqual(3.0, ants[0].left)
        self.assertEqual(1.5, ants[0].right)
        self.assertEqual(2.0, ants[0].ratio)

    def test_ratio_slash(self):
        text = "Ratio of not greater than 3/1.."
        ants = list(get_ratio_annotations(text))
        self.assertEqual(1, len(ants))

    def test_file_samples(self):
        tester = TypedAnnotationsTester()
        tester.test_and_raise_errors(
            get_ratio_annotations,
            'lexnlp/typed_annotations/en/ratio/ratios.txt',
            RatioAnnotation)
