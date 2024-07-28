import pytest
from haki_parser import parse_expression

def test_parse_expression_1():
    assert parse_expression('read_pdf CV_AndrewTest.pdf')
    assert parse_expression('read_pdf CV_AndrewTest.pdf')
