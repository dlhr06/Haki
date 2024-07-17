from lark import Lark
from evaluator import Evaluator
from grammar import grammar

parser = Lark(grammar, parser='lalr', transformer=Evaluator())

def parse_expression(expression):
    try:
        return parser.parse(expression)
    except Exception as e:
        return f'Error: {e}'
