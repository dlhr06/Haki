import pytest
from haki_parser import parse_expression

def test_parse_expression_1():
    assert parse_expression('read_pdf cv.pdf')
    assert parse_expression('read_pdf cv2.pdf')
