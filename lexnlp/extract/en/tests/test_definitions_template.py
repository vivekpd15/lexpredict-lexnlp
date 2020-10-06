from unittest import TestCase

from lexnlp.extract.common.annotations.definition_annotation import DefinitionAnnotation
from lexnlp.extract.en.definitions import get_definition_annotations
from lexnlp.tests.typed_annotations_tests import TypedAnnotationsTester

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/1.7.0/LICENSE"
__version__ = "1.7.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class TestDefinitionsTemplate(TestCase):

    def test_file_samples(self):
        tester = TypedAnnotationsTester()
        tester.test_and_raise_errors(
            get_definitions_sorted,
            'lexnlp/typed_annotations/en/definition/definitions.txt',
            DefinitionAnnotation)


def get_definitions_sorted(text: str):
    annotations = list(get_definition_annotations(text))
    annotations.sort(key=lambda a: a.coords[0])
    return annotations
