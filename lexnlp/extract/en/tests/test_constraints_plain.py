from unittest import TestCase

from lexnlp.extract.common.annotations.constraint_annotation import ConstraintAnnotation
from lexnlp.extract.en.constraints import get_constraints, get_constraint_annotations
from lexnlp.tests.typed_annotations_tests import TypedAnnotationsTester

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/1.7.0/LICENSE"
__version__ = "1.7.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class TestConstraintsPlain(TestCase):

    def test_constraints(self):
        text = 'My kung-fu is no less than yours'
        cs = list(get_constraints(text))
        self.assertEqual(1, len(cs))

        ant = list(get_constraint_annotations(text))[0]
        self.assertEqual((0, len('My kung-fu is no less than ')), ant.coords)
        cite = ant.get_cite()
        self.assertEqual('/en/constraint/no less than/my kung-fu is', cite)

    def test_file_samples(self):
        tester = TypedAnnotationsTester()
        tester.test_and_raise_errors(
            get_constraint_annotations,
            'lexnlp/typed_annotations/en/constraint/constraints.txt',
            ConstraintAnnotation)
